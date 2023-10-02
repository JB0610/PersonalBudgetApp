from functions import add_income, add_expense, view_all_transactions, compute_balance, delete_transaction
from storage import load_transactions, save_transactions

transactions = []

if __name__ == "__main__":
    transactions.extend(load_transactions())

    while True:
        print("\nPersonal Budgeting Tool")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Balance")
        print("5. Delete a Transaction")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter income description: ")
            amt = float(input("Enter amount: "))
            add_income(desc, amt)
            save_transactions(transactions)  # Save after adding income
        elif choice == "2":
            desc = input("Enter expense description: ")
            amt = float(input("Enter amount: "))
            add_expense(desc, amt)
            save_transactions(transactions)  # Save after adding expense
        elif choice == "3":
            view_all_transactions()
        elif choice == "4":
            print(f"Balance: {compute_balance()}")
        elif choice == "5":
            view_all_transactions()
            index = int(input("Enter the index of the transaction to delete: "))
            delete_transaction(index)
            save_transactions(transactions)  # Save after deleting a transaction
        elif choice == "6":
            break
