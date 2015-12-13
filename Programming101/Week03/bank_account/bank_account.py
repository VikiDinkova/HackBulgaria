class BankAccount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = ['Account was created']

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        self.history.append(
            "__int__ check -> {}{}".format(self.balance, self.currency)
        )
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.history.append(
            "Deposited {}{}".format(amount, self.currency)
        )

    def get_balance(self):
        self.history.append(
            "Balance check -> {}{}".format(self.balance, self.currency)
        )
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            self.history.append(
                "Withdraw for {}{} failed".format(amount, self.currency)
            )
            return False
        else:
            self.balance -= amount
            self.history.append(
                "{}{} was withdrawed".format(amount, self.currency)
            )
            return True

    def transfer_to(self, account, amount):
        if account.currency != self.currency or self.balance < amount:
            return False
        else:
            self.balance -= amount
            account.balance += amount
            account.history.append(
                "Transfer from {} for {}{}".format(self.name, amount, self.currency)
            )
            self.history.append(
                "Transfer to {} for {}{}".format(account.name, amount, self.currency)
            )
            return True

    def get_history(self):
        return self.history
