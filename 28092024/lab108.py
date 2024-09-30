#bank:
class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def _withdraw(self,amount):
        self.balance-=amount
    def __check_balance(self):
        print("Your Balance is:",self.balance)
    def is_authentication(self,isAuth):
        if isAuth:
            self.__check_balance()
        else:
            print("You are not Authenticated")
    def do_withdraw(self):
        jp_chase._withdraw(6000)

jp_chase=BankAccount()
jp_chase.deposit(1000)
jp_chase.do_withdraw()
jp_chase.is_authentication(True)
