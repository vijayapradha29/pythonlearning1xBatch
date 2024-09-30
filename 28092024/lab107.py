#bank:
class Mybank:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        # print(self.balance)
    def withdraw(self,amount):
        self._balance=self.balance-amount
        # final_amount=self._balance
        # print(self._balance)
    def check_balance(self):
        self.__balance=deposit-withdraw
        print("Your Balance is:",self.__balance)
# #

deposit=int(input("Enter Amount to be Deposited:\n"))
withdraw=int(input("Enter Amount to be Withdrawn:\n"))
#

jp_chase=Mybank()
# jp_chase.deposit=deposit
# jp_chase.withdraw=withdraw
jp_chase.check_balance()
#
