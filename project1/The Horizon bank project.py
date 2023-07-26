# Step 1: Create an empty dictionary to store account information
bank_accounts = {}

# Step 2: Function to create accounts
def create_account(account_number, customer_name, initial_balance=0):
    if account_number in bank_accounts:
        return "Account already exists!"
    bank_accounts[account_number] = {
        "name": customer_name,
        "balance": initial_balance,
        "transaction_history": []
    }
    return "Account created successfully."

# Step 3: Function to deposit funds
def deposit(account_number, amount):
    if account_number in bank_accounts:
        bank_accounts[account_number]["balance"] += amount
        bank_accounts[account_number]["transaction_history"].append(f"Deposited {amount}")
        return "Deposit successful."
    return "Account not found."

# Step 4: Function to withdraw funds
def withdraw(account_number, amount):
    if account_number in bank_accounts:
        if bank_accounts[account_number]["balance"] >= amount:
            bank_accounts[account_number]["balance"] -= amount
            bank_accounts[account_number]["transaction_history"].append(f"Withdrew {amount}")
            return "Withdrawal successful."
        return "Insufficient balance."
    return "Account not found."

# Step 5: Function to check account balance
def check_balance(account_number):
    if account_number in bank_accounts:
        return bank_accounts[account_number]["balance"]
    return "Account not found."

# Step 6: Function to view transaction history
def view_transaction_history(account_number):
    if account_number in bank_accounts:
        return bank_accounts[account_number]["transaction_history"]
    return "Account not found."

# Step 7: Main program to interact with the bank operations
def main():
    while True:
        print("\nWelcome to Horizon Bank!")
        print("1. Create Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Account Balance")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance (optional, default is 0): "))
            print(create_account(account_number, customer_name, initial_balance))
        
        elif choice == 2:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            print(deposit(account_number, amount))
        
        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            print(withdraw(account_number, amount))
        
        elif choice == 4:
            account_number = input("Enter account number: ")
            print("Account Balance:", check_balance(account_number))
        
        elif choice == 5:
            account_number = input("Enter account number: ")
            print("Transaction History:")
            for transaction in view_transaction_history(account_number):
                print(transaction)
        
        elif choice == 6:
            print("Thank you for using Horizon Bank!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
