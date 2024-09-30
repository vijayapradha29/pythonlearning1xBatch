class Father:
    bank_bal=100
    def one_bhk(self):
        print("Use it Son")
class Son(Father):
    pass
s=Son()
print(s.bank_bal)
s.one_bhk()