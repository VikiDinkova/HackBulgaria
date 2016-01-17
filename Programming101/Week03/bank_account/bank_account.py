class BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        self._name = name
        self._balance = balance
        self._currency = currency
        self._history = ['Account was created']

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(
            self._name,
            self._balance,
            self._currency
        )

    def __int__(self):
        self._history.append(
            "__int__ check -> {}{}".format(self._balance, self._currency)
        )
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()
        else:
            self._balance += amount
            self._history.append(
                "Deposited {}{}".format(amount, self._currency)
            )

    def balance(self):
        self._history.append(
            "Balance check -> {}{}".format(self._balance, self._currency)
        )
        return self._balance

    def withdraw(self, amount):
        if self._balance < amount:
            self._history.append(
                "Withdraw for {}{} failed".format(amount, self._currency)
            )
            return False
        else:
            self._balance -= amount
            self._history.append(
                "{}{} was withdrawed".format(amount, self._currency)
            )
            return True

    def transfer_to(self, account, amount):
        if account._currency != self._currency or self._balance < amount:
            return False
        else:
            self._balance -= amount
            account._balance += amount
            account._history.append(
                "Transfer from {} for {}{}".format(self._name, amount, self._currency)
            )
            self._history.append(
                "Transfer to {} for {}{}".format(account._name, amount, self._currency)
            )
            return True

    def history(self):
        return self._history
