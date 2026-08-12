import json
import os

WALLET_FILE = "secure_application/outputs/wallets.json"

def load_wallets():
    if not os.path.exists(WALLET_FILE):
        return {}

    with open(WALLET_FILE, "r") as file:
        return json.load(file)


def save_wallets(wallets):
    with open(WALLET_FILE, "w") as file:
        json.dump(wallets, file, indent=4)


def create_wallet(owner):
    wallets = load_wallets()

    wallet_id = "W" + str(len(wallets) + 1).zfill(3)

    wallets[wallet_id] = {
        "owner": owner,
        "balance": 1000.0
    }

    save_wallets(wallets)

    print("\nWallet created successfully!")
    print("Wallet ID:", wallet_id)
    print("Owner:", owner)
    print("Initial balance: 1000.0")


def get_balance(wallet_id):
    wallets = load_wallets()

    if wallet_id not in wallets:
        print("Wallet not found.")
        return

    print("\nWallet:", wallet_id)
    print("Owner:", wallets[wallet_id]["owner"])
    print("Balance:", wallets[wallet_id]["balance"])
