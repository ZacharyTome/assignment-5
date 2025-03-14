from datetime import datetime

class Transaction:
    def __init__(self, amount, timestamp=None):
        self.amount = float(amount)
        self.timestamp = timestamp if timestamp else datetime.now()

    def __repr__(self):
        return f"Transaction({self.amount}, {repr(self.timestamp)})"

    def __str__(self):
        sign = "+" if self.amount >= 0 else "-"
        return f"{self.timestamp.strftime('%Y-%m-%d')}: {sign}${abs(self.amount):,.2f}"


class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        amount = abs(float(amount))
        self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        amount = -abs(float(amount))
        self.transactions.append(Transaction(amount))

    def get_balance(self):
        return sum(t.amount for t in self.transactions)

    def __repr__(self):
        return f"Account(transactions={self.transactions})"

    def __str__(self):
        transactions_str = "\n".join(str(t) for t in self.transactions)
        return f"{transactions_str}\nAccount Balance: ${self.get_balance():,.2f}"
