class Bankdetails:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
    
amount=Bankdetails('alice',1000)
amount.deposit(500)
print(amount.get_balance())