# PersonalBudgetApp

Overview:
Personal Budget Tool is a sophisticated desktop application designed to manage personal finances with efficacy. Leveraging the simplicity of a GUI interface and the reliability of SQLite databases, this application ensures both ease-of-use and data integrity.

Features:
User-Friendly Interface
Streamlined interface provides an intuitive user experience.
Purposefully designed to ensure that users can quickly and effortlessly input or retrieve information.

Comprehensive Transaction Management
Add Income: Allows users to enter sources of income, providing a comprehensive financial overview.
Add Expense: Enables precise tracking of expenditures to monitor and evaluate spending habits.
View Transactions: Retrieves a full list of past transactions, aiding users in reviewing their financial history at a glance.
View Balance: Quick access to the current balance provides users with an immediate understanding of their financial standing.

Database Integration
Integration with SQLite ensures:
Reliability: Minimized risk of data corruption.
Data Integrity: Reliable storage mechanism to ensure data remains consistent and accurate.
Security: Data is stored locally, safeguarding user information.

Setup and Usage

Clone the Repository:
git clone https://github.com/JB0610/PersonalBudgetApp
cd PersonalBudgetApp

Install Dependencies:
Ensure you have Python installed, then run:
pip install -r requirements.txt

Launch the Application:
python app_gui.py

Database Schema
For those interested in the underlying data structure:

Table: transactions
id: A unique identifier for each transaction.
description: A brief description of the transaction.
amount: The monetary value associated with the transaction.
transaction_type: Categorization indicating whether the transaction is an income or an expense.

Contact & Feedback
For any queries, suggestions, or feedback, feel free to reach out.

Justin Burkhalter: A passionate software developer dedicated to creating meaningful and efficient applications. Connect with me on GitHub or LinkedIn.
