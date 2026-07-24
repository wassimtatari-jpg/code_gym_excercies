class Banckacount:
    def __init__(self,acount_number,initial_balance=0):
        self.acount_number=acount_number
        self.initial_balance=initial_balance
    def deposit(self,amount):
        if amount>0:
            self.initial_balance+=amount
            print(f"Deposited {amount} and your balance is {self.initial_balance}")
        else:
            print(f"Deposited should be possitive")
    def withdraw(self,amount):
        if 0<amount<=self.initial_balance:
            self.initial_balance-=amount
            print(f"withdraws {amount} and your balance is {self.initial_balance}")
        else:
            print(f'withdraws should be possitive and not exceed the current balance')

acount=Banckacount(100200100300,9800)

acount.deposit(800)
acount.deposit(99)
acount.deposit(520)

acount.withdraw(50)
acount.withdraw(8800)
acount.withdraw(70)