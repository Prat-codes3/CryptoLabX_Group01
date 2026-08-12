import json
import os

TRANSACTION_FILE = "secure_application/outputs/transactions.json"
WALLET_FILE = "secure_application/outputs/wallets.json"


def load_transactions():
    if not os.path.exists(TRANSACTION_FILE):
        return []

    with open(TRANSACTION_FILE, "r") as file:
        return json.load(file)


def save_transactions(transactions):
    with open(TRANSACTION_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def request_transaction(sender, receiver, amount):
    transactions = load_transactions()

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid transaction amount.")
        return

    wallets = {}

    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as file:
            wallets = json.load(file)

    if sender not in wallets:
        print("Sender wallet does not exist.")
        return

    if receiver not in wallets:
        print("Receiver wallet does not exist.")
        return

    if wallets[sender]["balance"] < amount:
        print("Insufficient balance.")
        return

    wallets[sender]["balance"] -= amount
    wallets[receiver]["balance"] += amount

    with open(WALLET_FILE, "w") as file:
        json.dump(wallets, file, indent=4)

    transaction = {
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print("\nTransaction completed successfully.")


def view_transaction_history(wallet_id):
    transactions = load_transactions()

    print("\nTransaction History")

    found = False

    for transaction in transactions:
        if (
            transaction["sender"] == wallet_id
            or transaction["receiver"] == wallet_id
        ):
            print(transaction)
            found = True

    if not found:
        print("No transactions found.")
