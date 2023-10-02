class Transaction:
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' or 'expense'

    def __str__(self):
        return f"{self.description}: {self.amount} ({self.transaction_type})"
