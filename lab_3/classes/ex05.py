class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if self.balance - money >= 0: self.balance -= money
        else: print(f'doesn\'t enough, you have only - {self.balance}tg')
    
    def __str__(self):
        return f'name: {self.owner} \nbalance: {self.balance}'

me = Account('Daryn', 5000)
print(me)

me.deposit(400)
print(me)

me.withdraw(3000)
print(me)

me.withdraw(7000)
print(me)
