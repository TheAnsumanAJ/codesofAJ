class BankAccount:
    def __init__(self,accno,balance):
        self.acc=accno
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit Success!")
    def withdaw(self,amount):
        self.balance-=amount
        print("Withdrawl Succes!")
    def display(self):
        print("Balance is:",self.balance)
obj=BankAccount(19,5000)
print("Account created!")
obj.display()
obj.deposit(5000)
obj.display()
obj.withdaw(3000)
obj.display()