import sys
class customer:
    bankname = 'STAATEE BANK OF INDIA'
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance + amt
        print('the remaing amount is',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('the aount is out of ur balance')
            sys.exit()
        self.balance = self.balance - amt
        print('the reaming amount is ',self.balance)
print('welcome to STATE BANK OF INDIA')
name = input('enter your name')
c = customer(name)
while True:
    print('d-Deposit\nw-withdrwal\ne-exit')
    option = input('chosse your option')
    if option=='d' or option =='D':
        amt = float(input('enter the amount'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt = float(input('enter the amount'))
        c.withdraw(amt)
    elif option =='e' or option=='E':
        print('thanks for banking')
        sys.exit()
    else:
        print('invalid option')