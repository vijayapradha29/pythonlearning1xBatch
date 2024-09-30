#bank account:
class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self._balance=self.balance+amount
    def withdraw(self,amount):
        self.__balance=self._balance-amount
    def check_details(self):
        print("Your Balance Details are:",self.__balance)

sbi_object=BankAccount()
sbi_object.deposit(10000)
sbi_object.withdraw(5000)
sbi_object.check_details()