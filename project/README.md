# Multi-User Finance Tracker

#### Video Demo: [Click here](https://youtu.be/QER9ENwCggs?si=cC9E9GyPPnU7MFAn)

## Description:

- **Multi-User Support**: Unique user IDs for transactions like deposits and withdrawals.
- **User Management**: Users can **CREATE**, **READ**, **UPDATE**, and **DELETE** their account details.
- **Transaction Tracking**: Track deposits, withdrawals, and view transaction history.
- **Persistent Data**: All data stored in a JSON file for persistent access.

## Key Features:

- **User CRUD Operations**: Create, update, and delete user accounts.
- **Financial Transactions**: Deposit and withdraw funds, with a transaction log.
- **Balance Calculation**: Automatically calculate balance based on transactions.
- **Transaction History**: View detailed transaction history.

## Concepts Used:

- **Packages**: `datetime`, `JSON` for data handling.
- **Data Structures**: Dictionaries for storing user and transaction data, lists for transaction history.
- **Functions**: Modular functions for user management and transactions.

## How It Works:

1. **Main Menu**: Access options to list, add, update, or delete users, or exit.
2. **User Menu**: Perform transactions (deposit/withdraw), view balance and transaction history.
3. **Persistent Data**: All data is saved to `project_data.json`.

## Requirements:

- Python 3.x
- Basic knowledge of Python functions and file handling.

## Future Improvements:

- **Security**: Add user authentication with passwords.
- **GUI**: Develop a graphical interface.
- **Data Backup**: Implement automatic data backup.
