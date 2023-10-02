from models import Transaction
transactions = []

def add_income(description, amount):
    income = Transaction(description, amount, "income")
    transactions.append(income)

def add_expense(description, amount):
    expense = Transaction(description, amount, "expense")
    transactions.append(expense)

def view_all_transactions():
    for transaction in transactions:
        print(transaction)

def compute_balance():
    income = sum(t.amount for t in transactions if t.transaction_type == "income")
    expense = sum(t.amount for t in transactions if t.transaction_type == "expense")
    return income - expense

def delete_transaction(index):
    if 0 <= index < len(transactions):
        del transactions[index]
    else:
        print("Invalid index!")
