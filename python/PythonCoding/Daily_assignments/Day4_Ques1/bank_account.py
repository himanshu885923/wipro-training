class BankAccount:

    def __init__(self, acc_no, name, balance):
        self.__account_number = acc_no
        self.__holder_name = name
        self.__balance = balance

    def get_account_number(self):
        return  self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def set_holder_name(self, name):
        self.__holder_name = name

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid withdrawal amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")

    def display(self):
        print("\n--- Account Details ---")
        print("Account No:", self.__account_number)
        print("Name:", self.__holder_name)
        print("Balance:", self.__balance)
