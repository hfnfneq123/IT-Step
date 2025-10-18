class BankAccount:
    def __init__(self, name, nban, balance=0.0):
        self.name = name
        self.nban = nban
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сума поповнення повинна перевищувати 0грн!")

    def withdraw(self, amount):
        if self.balance < amount:
            print("На рахунку не достатньо коштів!")
        elif amount <= 0:
            print("Сума зняття повинна перевищувати 0грн!")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Рахунок №{self.nban} | Власник: {self.name} | Баланс: {self.balance:.2f}€"



class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, name, nban, balance=0.0):
        account = BankAccount(name, nban, balance)
        self.accounts.append(account)
        print(f"🏦 Рахунок створено для {name}, номер рахунку: (№{nban}).")
        return account

    def find_acc(self, nban):
        for acc in self.accounts:
            if acc.nban == nban:
                return acc
        return None

    def transfer(self, from_acc_number, to_acc_number, amount):
        from_acc = self.find_acc(from_acc_number)
        to_acc = self.find_acc(to_acc_number)
        if not from_acc or not to_acc:
            print("Рахунок не знайдено!")
            return

        if from_acc.balance < amount:
            print("На рахунку не достатньо коштів для виконання транзакції!")
            return

        if amount <= 0:
            print("Сума транзакції повинна перевищувати 0грн!")
            return

        from_acc.balance -= amount
        to_acc.balance += amount
        print(f"Переказано {amount:.2f}€ з рахунку №{from_acc_number} на №{to_acc_number}.")

    def show_all_accounts(self):
        """Вивести всі рахунки в банку"""
        print(f"\n=== Список рахунків у банку '{self.name}' ===")
        for acc in self.accounts:
            print(acc)

my_bank = Bank("Ukr Bank")
acc1 = my_bank.add_account( "Artem", "UA001", 100)
acc2 = my_bank.add_account( "Anna", "UA002", 200)

acc1.deposit(500)
acc2.withdraw(100)

my_bank.transfer("UA001", "UA002", 100)

my_bank.show_all_accounts()



