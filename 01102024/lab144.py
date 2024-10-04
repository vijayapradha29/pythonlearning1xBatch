#polymorphism:
class Summattion:
    def sum(self,*args):
        ans=0
        for i in args:
            ans+=i
        return ans
summation=Summattion()
print(summation.sum(1,2,3,5,6,78,99))