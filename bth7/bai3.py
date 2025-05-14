class Account:
    def __init__(self,balance) :
        self.balance=balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, value):
        self.balance += value
        print( "Da cong : ", value)

    def wirhdraw(self, value):
        self.balance -=  value
        print("Da tru: " ,value)

class SavingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def wirhdraw(self, value):
        if value <= self.balance:
            super().wirhdraw(value)
        else:
            print("Ko du tien")

class CheckingAccount(Account):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit=limit
    
    def wirhdraw(self, value):
        if self.get_balance() - value >= -self.limit:
            super().wirhdraw(value)
        else:
            print("Ko du tien")

a = CheckingAccount(20000,1000)
a.wirhdraw(22000)
print( a.get_balance())