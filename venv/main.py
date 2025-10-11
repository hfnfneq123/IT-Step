class BankAccount:
    def __init__(self, owner_name, account_number, balance=0.0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Поповнення рахунку"""
        if amount > 0:
            self.balance += amount
            print(f"✅ {self.owner_name}, ваш рахунок поповнено на {amount:.2f}€.")
        else:
            print("❌ Сума для поповнення має бути більшою за 0.")

    def withdraw(self, amount):
        """Зняття коштів"""
        if amount <= 0:
            print("❌ Сума для зняття має бути більшою за 0.")
        elif amount > self.balance:
            print(f"⚠️ Недостатньо коштів на рахунку {self.account_number}.")
        else:
            self.balance -= amount
            print(f"💸 {self.owner_name}, знято {amount:.2f}€. Поточний баланс: {self.balance:.2f}€")

    def __str__(self):
        return f"Рахунок №{self.account_number} | Власник: {self.owner_name} | Баланс: {self.balance:.2f}€"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, owner_name, account_number, initial_balance=0.0):
        """Створення нового банківського рахунку"""
        account = BankAccount(owner_name, account_number, initial_balance)
        self.accounts.append(account)
        print(f"🏦 Рахунок створено для {owner_name} (№{account_number}).")
        return account

    def find_account(self, account_number):
        """Пошук рахунку за номером"""
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def transfer(self, from_acc_number, to_acc_number, amount):
        """Переказ коштів між рахунками"""
        from_acc = self.find_account(from_acc_number)
        to_acc = self.find_account(to_acc_number)

        if not from_acc or not to_acc:
            print("❌ Один із рахунків не знайдено.")
            return

        if from_acc.balance < amount:
            print(f"⚠️ Недостатньо коштів на рахунку {from_acc.account_number}.")
            return

        if amount <= 0:
            print("❌ Сума переказу має бути більшою за 0.")
            return

        from_acc.balance -= amount
        to_acc.balance += amount
        print(f"🔁 Переказано {amount:.2f}€ з рахунку №{from_acc_number} на №{to_acc_number}.")

    def show_all_accounts(self):
        """Вивести всі рахунки в банку"""
        print(f"\n=== Список рахунків у банку '{self.name}' ===")
        for acc in self.accounts:
            print(acc)


# === Приклад використання ===

    # Створюємо банк
my_bank = Bank("Bank of Python")

    # Створюємо рахунки
acc1 = my_bank.create_account("Артем", "UA001", 500)
acc2 = my_bank.create_account("Олена", "UA002", 300)

    # Поповнення та зняття коштів
acc1.deposit(200)
acc2.withdraw(100)

    # Переказ між рахунками
my_bank.transfer("UA001", "UA002", 250)

    # Вивід усіх рахунків
my_bank.show_all_accounts()

