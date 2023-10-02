import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, font
from storage import load_transactions, save_transactions
from functions import add_income, add_expense, view_all_transactions, compute_balance, delete_transaction

class BudgetApp:

    def __init__(self, root):
        self.transactions = load_transactions()

        root.title("Personal Budgeting Tool")
        root.geometry("500x400")
        root.configure(bg='#333')

        # Title Label
        title_font = font.Font(size=16, weight="bold")
        self.title_label = ttk.Label(root, text="Personal Budgeting Tool", font=title_font)
        self.title_label.pack(pady=20)

        # Buttons Frame
        buttons_frame = ttk.Frame(root)
        buttons_frame.pack(pady=20)

        # Button Styles
        btn_font = font.Font(size=12)
        style = ttk.Style()
        style.configure("TButton", font=btn_font, padding=10, width=20)

        self.add_income_button = ttk.Button(buttons_frame, text="Add Income", command=self.add_income_dialog)
        self.add_income_button.grid(row=0, column=0, padx=10, pady=10)

        self.add_expense_button = ttk.Button(buttons_frame, text="Add Expense", command=self.add_expense_dialog)
        self.add_expense_button.grid(row=0, column=1, padx=10, pady=10)

        self.view_transactions_button = ttk.Button(buttons_frame, text="View Transactions", command=self.view_transactions_dialog)
        self.view_transactions_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_balance_button = ttk.Button(buttons_frame, text="View Balance", command=self.view_balance_dialog)
        self.view_balance_button.grid(row=1, column=1, padx=10, pady=10)

    def add_income_dialog(self):
        desc = simpledialog.askstring("Income", "Enter income description:")
        if desc:
            amt = simpledialog.askfloat("Income", "Enter amount:")
            if amt:
                add_income(desc, amt)
                self.transactions = load_transactions()
                save_transactions(self.transactions)
                messagebox.showinfo("Success", "Income added successfully!")

    def add_expense_dialog(self):
        desc = simpledialog.askstring("Expense", "Enter expense description:")
        if desc:
            amt = simpledialog.askfloat("Expense", "Enter amount:")
            if amt:
                add_expense(desc, amt)
                self.transactions = load_transactions()
                save_transactions(self.transactions)
                messagebox.showinfo("Success", "Expense added successfully!")

    def view_transactions_dialog(self):
        transactions = view_all_transactions()
        if transactions:
            message = "\n".join(str(t) for t in transactions)
            messagebox.showinfo("Transactions", message)
        else:
            messagebox.showwarning("Transactions", "No transactions found!")

    def view_balance_dialog(self):
        balance = compute_balance()
        messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
