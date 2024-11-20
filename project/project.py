import json
from datetime import datetime


# Load data from the JSON file
def load_data():
    try:
        with open('project_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The data file does not exist. Initializing a new data structure.")
        data = {'users': {}, 'transactions': {}, 'next_user_id': 1}
        save_data(data)
    except json.JSONDecodeError:
        print("Error: Corrupted data file. Starting with a new data structure.")
        data = {'users': {}, 'transactions': {}, 'next_user_id': 1}
        save_data(data)
    return data

# Save data to the JSON file
def save_data(data):
    with open('project_data.json', 'w') as file:
        json.dump(data, file, indent=4)

#ID handlers
def get_next_user_id(data):
    user_id = data['next_user_id']
    data['next_user_id'] += 1
    return str(user_id)

def get_next_transaction_id(user_id, data):
    user_data = data['users'].get(user_id, {})
    transaction_id = user_data.get('next_transaction_id', 1)
    user_data['next_transaction_id'] = transaction_id + 1
    data['users'][user_id] = user_data
    return transaction_id

# User Management
def add_user(user_name, address, phone, data):
    if not user_name or not address:
        print("Error: User name and address are required.")
        return

    user_id = get_next_user_id(data)
    data['users'][user_id] = {
        'user_name': user_name,
        'address': address,
        'phone': phone,
        'next_transaction_id': 1
    }
    data['transactions'][user_id] = []
    print(f"\nUser added with ID: {user_id}")
    save_data(data)

def list_users(data):
    if not data['users']:
        print("\nNo users found.")
    for user_id, user_info in data['users'].items():
        print(f"User ID: {user_id}, Name: {user_info['user_name']}, "
              f"Address: {user_info['address']}, Phone: {user_info['phone']}")

def update_user(user_id, user_name, address, phone, data):
    if user_id not in data['users']:
        print("Error: User ID not found.")
        return
    data['users'][user_id].update({
        'user_name': user_name,
        'address': address,
        'phone': phone
    })
    print(f"User {user_id} updated successfully.")
    save_data(data)

def delete_user(user_id, data):
    if user_id in data['users']:
        del data['users'][user_id]
        del data['transactions'][user_id]
        print("User and associated transactions deleted successfully.")
        data['next_user_id'] -= 1
        save_data(data)
    else:
        print("Error: User ID not found.")

# Financial Transactions
def add_transaction(user_id, transaction_type, amount, data):
    if user_id not in data['users']:
        print("Error: User ID not found.")
        return False

    transaction_id = get_next_transaction_id(user_id, data)
    timestamp = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    data['transactions'][user_id].append({
        'transaction_id': transaction_id,
        'transaction_type': transaction_type,
        'amount': amount,
        'timestamp': timestamp
    })
    save_data(data)
    return True

def deposit(user_id, amount, data):
    if amount <= 0:
        print("Error: Amount must be positive.")
        return
    if add_transaction(user_id, 'deposit', amount, data):
        print("Deposit successful.")

def withdraw(user_id, amount, data):
    current_balance = get_balance(user_id, data)
    if amount <= 0:
        print("Error: Amount must be positive.")
        return
    elif current_balance < amount:
        print("Error: Insufficient balance.")
        return
    if add_transaction(user_id, 'withdraw', -amount, data):
        print("Withdrawal successful.")

def get_balance(user_id, data):
    if user_id not in data['users']:
        print("Error: User ID not found.")
        return 0
    return sum(transaction['amount'] for transaction in data['transactions'][user_id])

def view_transaction_history(user_id, data):
    # Print transaction history in text format
    user_transactions = data['transactions'][user_id]
    if not user_transactions:
        print("No transactions found.")
    else:
        print("\nTransaction History:")
        for transaction in user_transactions:
            print(f"ID: {transaction['transaction_id']}, "
                  f"Type: {transaction['transaction_type']}, "
                  f"Amount: ₹{transaction['amount']}, "
                  f"Timestamp: {transaction['timestamp']}")


# menu
def user_menu(user_id, data):
    # to Ensure user_id is a string to match JSON key
    user_id = str(user_id)

    if user_id not in data['users']:
        print("Error: User ID not found in user_menu.")
        return

    while True:
        print("\n|-|-| USER MENU |-|-|\n")
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: ₹"))
            deposit(user_id, amount, data)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: ₹"))
            withdraw(user_id, amount, data)
        elif choice == "3":
            balance = get_balance(user_id, data)
            print(f"Current balance: ₹{balance}")
        elif choice == "4":
            view_transaction_history(user_id, data)
        elif choice == '5':
            print(".....Returning to main menu")
            break
        else:
            print("\nInvalid input. Please select a valid option.")

def main():
    data = load_data()
    while True:
        print("\n||--- MULTI_USER FINANCE TRACKER ---||\n")
        print("1. List Existing Users")
        print("2. Add a New User")
        print("3. Access your account")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("list of users -->  1")
            list_users(data)
        elif choice == "2":
            name = input("Enter user name: ")
            address = input("Enter address: ")
            phone = input("Enter phone (optional): ")
            add_user(name, address, phone, data)
        elif choice == "3":
            user_id = input("Enter your user ID to access account: ")
            if str(user_id) in data['users']:  # Ensure comparison as strings
                user_menu(user_id, data)
            else:
                print("Error: User ID not found.")
        elif choice == "4":
            user_id = input("Enter user ID to update: ")
            name = input("Enter new user name: ")
            address = input("Enter new address: ")
            phone = input("Enter new phone (optional): ")
            update_user(user_id, name, address, phone, data)
        elif choice == "5":
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id, data)
        elif choice == "6":
            print(".....Exiting the system.\n")
            break
        else:
            print("\nInvalid option. Please try again.")

# Main Program Entry
if __name__ == "__main__":
    main()
