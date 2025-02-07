class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение: {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Ошибка: недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие: {amount}. Новый баланс: {self.balance}")
