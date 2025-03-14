import unittest
from datetime import datetime
from banking import Transaction, Account

class TestTransaction(unittest.TestCase):

    def test_transaction(self):
        now = datetime.now()
        transaction = Transaction(100)
        self.assertEqual(transaction.amount, 100)
        self.assertTrue(transaction.timestamp <= now)

    def test_time(self):
        custom_time = datetime(2025, 1, 1)
        transaction = Transaction(110, custom_time)
        self.assertEqual(transaction.timestamp, custom_time)

    def test_transaction_repr_str(self):
        transaction = Transaction(120, datetime(2025, 1, 2))
        expected_repr = f"Transaction(120.0, datetime.datetime(2025, 1, 2, 0, 0))"
        self.assertEqual(repr(transaction), expected_repr)
        self.assertEqual(str(transaction), "2025-01-02: +$120.00")

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_and_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50.0)

    def test_account_repr_str(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertIn("Account Balance: $50.00", str(self.account))
        self.assertTrue(repr(self.account).startswith("Account(transactions=["))

if __name__ == '__main__':
    unittest.main()
