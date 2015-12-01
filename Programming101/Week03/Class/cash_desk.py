from group import group


class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return 'A {0}$ bill'.format(self.amount)

    def __repr__(self):
        return 'A {0}$ bill'.format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(str(self.amount))


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def total(self):
        sum_ = 0
        for bill in self.bills:
            sum_ += int(bill)
        return sum_


# a = Bill(5)
# b = Bill(10)
# c = Bill(5)
# print(str(a))
# print(a)
# print(int(a))
# print(a == c)
# print(a == b)


# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]

# batch = BatchBill(bills)

# for bill in batch:
#     print(bill)

class CashDesk:
    def __init__(self):
        self.money_notes = []

    def take_money(self, money):
        if type(money) is Bill:
            self.money_notes.append(money)
        elif type(money) is BatchBill:
            for bill in money:
                self.money_notes.append(bill)

    def total(self):
        total_sum = 0
        for bill in self.money_notes:
            total_sum += bill.amount
        return total_sum

    def inspect(self):
        value_list = []
        for bill in self.money_notes:
            value_list.append(bill.amount)
        value_list = sorted(value_list)
        value_list = group(value_list)
        print('We have a total of {}$ in the desk'.format(self.total()))
        print('We have the following count of bills, sorted in ascending order:')
        for bill_patch in value_list:
            print('{}$ bills - {} '.format(bill_patch[0], len(bill_patch)))

# values = [10, 20, 50, 100, 100, 100]
# bills = [Bill(value) for value in values]

# batch = BatchBill(bills)

# desk = CashDesk()

# desk.take_money(batch)
# desk.take_money(Bill(10))

# print(desk.total())  # 390
# desk.inspect()