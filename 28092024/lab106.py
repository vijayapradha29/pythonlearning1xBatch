#bank:
class Bankaccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        # print(self.balance)
    def withdraw(self,amount):
        self._balance=self.balance-amount
        # print(self._balance)
    def check_balance(self):
        self.__balance=self._balance
        # print(self.__balance)
        # self.__balance==self._balance
        print("Your Balance is:",self.__balance)
    # def is_authenticated_true(self,isAuth):
    #     if isAuth:
    #         self.check_balance()
    #     else:
    #         print("You are not Authenticated")

jp_chase=Bankaccount()
jp_chase.deposit(1000)
jp_chase.withdraw(6000)

# jp_chase.is_authenticated_true(True)
jp_chase.check_balance()