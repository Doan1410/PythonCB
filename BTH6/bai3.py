class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber=accountNumber
        self.name= name
        self.balance= balance

    def Desposit(self, value):
        self.balance += value
        print("da nap ",value)
            
    def Withdrawal(self, value):
        if value>0:
            self.balance = self.balance - value
            print("da tru ", value)
        else:
            print("so tien tru phai lon hon 0 ")
    
    def banlFee(self):
        fee = self.balance*0.05
        self.balance -= fee
        print("da tru phi ngan hang ", fee)

    def display(self):
        print("So tai khoan :", self.accountNumber)
        print("Ten :", self.name)
        print("So du :", self.balance)

a = BankAccount("001", " Doan Ngo", 30000)
a.display()
print("-"*30)
a.Desposit(3000)
a.display()
print("-"*30)
a.Withdrawal(2000)
a.display()
print("-"*30)
a.banlFee()
a.display()