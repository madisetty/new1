class BankAccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
       	return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
#	def get_balance(self):
#		return self.balance
fa = BankAccount(10)
fb = BankAccount(20)
print fa.deposit(20)
print fb.deposit(20)
print fa.withdraw(10)
#print fa.display_balance()
#print fa.get_balance()
