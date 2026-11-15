class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.__acc_no=acc_no     #because of __ it became a private variable
        print("account number is:",self.__acc_no)
        print("balance is:",self.balance)
    def debit(self,amount):
        self.balance-=amount
    def credit(self,amount):
        self.balance+=amount
    def final_balance(self):
        print("final balance is:",self.balance)
a1=Account(1000,1234)
a1.debit(500)
a1.credit(1000)
a1.final_balance()
print(a1.__acc_no)   #it will give error because it is a private variable
