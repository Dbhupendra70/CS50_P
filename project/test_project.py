import pytest
from datetime import datetime
from project import add_user, get_balance, update_user, deposit, withdraw, add_transaction


mock_data = {
    'users': {
        '1': {'user_name': 'Rajesh Kumar', 'address': 'Sector 17, Chandigarh', 'phone': '9876543210', 'next_transaction_id': 1},
    },
    'transactions': {
        '1': [
            {'transaction_id': 1, 'transaction_type': 'deposit', 'amount': 5000, 'timestamp': '12-11-24 14:32:01'}
        ],
    },
    'next_user_id': 2
}

def test_add_user():
    """test adding a new user."""
    user_name = "Priya Singh"
    address = "Connaught Place, Delhi"
    phone = "9123456789"

    add_user(user_name, address, phone, mock_data)
    user_id = str(mock_data['next_user_id'] - 1)  # get the last added user id

    assert user_id in mock_data['users']
    assert mock_data['users'][user_id]['user_name'] == user_name
    assert mock_data['users'][user_id]['address'] == address

def test_get_balance():
    """test balance calculation."""
    user_id = '1'
    balance = get_balance(user_id, mock_data)
    assert balance == 5000

def test_update_user():
    """test updating user details."""
    user_id = '1'
    new_name = "Rajesh Sharma"
    new_address = "MG Road, Bengaluru"
    new_phone = "9888776655"

    update_user(user_id, new_name, new_address, new_phone, mock_data)

    assert mock_data['users'][user_id]['user_name'] == new_name
    assert mock_data['users'][user_id]['address'] == new_address
    assert mock_data['users'][user_id]['phone'] == new_phone

def test_deposit():
    """test depositing amount to account."""
    user_id = '1'
    initial_balance = get_balance(user_id, mock_data)

    deposit(user_id, 10000, mock_data)  # salary deposit ₹10,000
    updated_balance = get_balance(user_id, mock_data)

    # ensure the timestamp is added in the transaction
    last_transaction = mock_data['transactions'][user_id][-1]
    timestamp = last_transaction['timestamp']
    assert isinstance(datetime.strptime(timestamp, '%d-%m-%y %H:%M:%S'), datetime)

    assert updated_balance == initial_balance + 10000

def test_withdraw():
    """test withdrawing amount from account."""
    user_id = '1'
    initial_balance = get_balance(user_id, mock_data)

    deposit(user_id, 5000, mock_data)  # add ₹5,000 for sufficient balance
    withdraw(user_id, 2000, mock_data)  # withdraw ₹2,000

    updated_balance = get_balance(user_id, mock_data)

    # ensure the timestamp is added in the transaction
    last_transaction = mock_data['transactions'][user_id][-1]
    timestamp = last_transaction['timestamp']
    assert isinstance(datetime.strptime(timestamp, '%d-%m-%y %H:%M:%S'), datetime)

    assert updated_balance == initial_balance + 3000
