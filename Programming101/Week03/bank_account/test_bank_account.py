import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.name = 'viki'
        self.name2 = 'stenly'
        self.balance = 1000000
        self.currency = 'pound'
        self.account = BankAccount(self.name, self.balance, self.currency)
        self.account2 = BankAccount(self.name2, self.balance, self.currency)

    def test_account_init(self):
        self.assertEqual(self.account.name, self.name)
        self.assertEqual(self.account.balance, self.balance)
        self.assertEqual(self.account.currency, self.currency)

    def test_account_str(self):
        self.assertEqual(
            str(self.account),
            "Bank account for {} with balance of {}{}".format(
                self.name,
                self.balance,
                self.currency
            )
        )

    def test_account_int(self):
        self.assertEqual(int(self.account), self.balance)

    def test_get_balance(self):
        self.assertEqual(self.account.balance, self.account.get_balance())

    def test_account_deposit(self):
        deposit_amount = 10000000
        self.account.deposit(deposit_amount)
        self.assertEqual(self.account.balance, self.balance + deposit_amount)

    def test_account_withdraw_success(self):
        initial_balance = self.account.balance
        withdraw_amount = 1
        result = self.account.withdraw(withdraw_amount)
        self.assertTrue(result)
        self.assertEqual(initial_balance - withdraw_amount, self.account.balance)

    def test_account_withdraw_fail(self):
        initial_balance = self.account.balance
        withdraw_amount = 10000000000
        result = self.account.withdraw(withdraw_amount)
        self.assertFalse(result)
        self.assertEqual(initial_balance, self.account.balance)

    def test_account_transfer_to_success(self):
        old_balance1 = self.account.balance
        old_balance2 = self.account2.balance
        transfer_amount = 10000
        result = self.account.transfer_to(self.account2, transfer_amount)
        self.assertTrue(result)
        self.assertEqual(old_balance1 - transfer_amount, self.account.balance)
        self.assertEqual(old_balance2 + transfer_amount, self.account2.balance)

    def test_account_transfer_to_fails_currency(self):
        self.account2.currency = 'BGN'
        transfer_amount = 10000
        result = self.account.transfer_to(self.account2, transfer_amount)
        self.assertFalse(result)

    def test_account_transfer_to_fails_amount(self):
        self.account.balance = 1
        transfer_amount = 10000
        result = self.account.transfer_to(self.account2, transfer_amount)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
