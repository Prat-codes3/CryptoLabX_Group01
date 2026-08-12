current_session = None

# INTENTIONALLY INSECURE:
# A predictable session ID is generated from the wallet ID.
def login(wallet_id):
    global current_session

    current_session = "SESSION_" + wallet_id

    print("\nLogin successful.")
    print("Session ID:", current_session)


def logout():
    global current_session

    current_session = None
    print("\nLogged out successfully.")


def get_current_session():
    return current_session