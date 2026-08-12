import sys

sys.path.append("secure_application/src")

from wallet import create_wallet, get_balance
from transactions import request_transaction, view_transaction_history


print("Testing Cryptocurrency Wallet")
print("--------------------------------")

print("\nTest 1: Wallet Creation")
create_wallet("Alice")

print("\nTest 2: Wallet Creation")
create_wallet("Bob")

print("\nTest 3: Balance Inquiry")
get_balance("W001")

print("\nTest 4: Transaction")
request_transaction("W001", "W002", 100)

print("\nTest 5: Transaction History")
view_transaction_history("W001")

print("\nAll basic tests completed.")