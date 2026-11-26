class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def amount_check(self, amount):
        if not isinstance(amount, int):
            return


    def deposit(self, amount):
        self.amount_check(amount)
        if amount < 0:
            print("Отрицательная сумма пополнения")
            return
        self.__balance += amount


    def withdraw(self, amount):
        self.amount_check(amount)
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount


    def balance_check(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.balance_check())

# print(account.__balance)