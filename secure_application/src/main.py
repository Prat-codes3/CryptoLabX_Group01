from wallet import create_wallet, get_balance
from transactions import request_transaction, view_transaction_history
from session import login, logout, get_current_session


# INTENTIONALLY INSECURE:
# Hardcoded secret stored directly in source code.
ADMIN_SECRET = "CryptoLabX_Admin_12345"


def show_menu():
    print("\n================================")
    print("      CRYPTOCURRENCY WALLET")
    print("================================")
    print("1. Create Wallet")
    print("2. Check Balance")
    print("3. View Transaction History")
    print("4. Request Transaction")
    print("5. Login")
    print("6. Logout")
    print("7. Admin Access")
    print("8. Exit")
    print("================================")


def main():
    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            owner = input("Enter owner name: ")
            create_wallet(owner)

        elif choice == "2":
            wallet_id = input("Enter wallet ID: ")
            get_balance(wallet_id)

        elif choice == "3":
            wallet_id = input("Enter wallet ID: ")
            view_transaction_history(wallet_id)

        elif choice == "4":
            sender = input("Enter sender wallet ID: ")
            receiver = input("Enter receiver wallet ID: ")
            amount = input("Enter amount: ")

            request_transaction(sender, receiver, amount)

        elif choice == "5":
            wallet_id = input("Enter wallet ID: ")
            login(wallet_id)

        elif choice == "6":
            logout()

        elif choice == "7":
            secret = input("Enter admin secret: ")

            if secret == ADMIN_SECRET:
                print("Admin access granted.")
            else:
                print("Invalid admin secret.")

        elif choice == "8":
            print("Exiting application...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()