import sqlite3
from models import Transaction

DB_NAME = "budget_data.db"

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_transactions(transactions):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Clear the existing data
    cursor.execute("DELETE FROM transactions")

    # Insert the current transactions
    for transaction in transactions:
        cursor.execute("INSERT INTO transactions (description, amount, transaction_type) VALUES (?, ?, ?)",
                       (transaction.description, transaction.amount, transaction.transaction_type))

    conn.commit()
    conn.close()


def load_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT description, amount, transaction_type FROM transactions")
    rows = cursor.fetchall()

    transactions = [Transaction(row[0], row[1], row[2]) for row in rows]

    conn.close()

    return transactions


# Initialize the database when the module is imported
init_db()
