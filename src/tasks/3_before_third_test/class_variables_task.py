print()
class Bank_account:
    
    account_number: int = 93000000000
    interest_rate: float = 4/100
    
    
    def __init__(self, owner: str, balance: float):
        
        self.balance = balance * (1 - self.interest_rate)
        self.owner = owner
        
        Bank_account.account_number += 1
        self.a_nr = Bank_account.account_number
    
    def set_balance(self, amount: float):
        self.balance += amount
    
    def take_balance(self, amount: float):
        
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("You cannot take more money then what the current balance has.")
    
    def show_info(self):
        print(f"Account Number: {self.a_nr} | Balance: {round(self.balance, 2)} | Interest Rate: {self.interest_rate}")


class Savings_account(Bank_account):

    def __init__(self, owner: str, balance: float):
        super().__init__(owner, balance)
        
        self.interest_rate = 6/100
        self.total_takes = 0
    
    def take_balance(self, amount: float):
        
        if self.total_takes < 12:
            
            if self.balance - amount >= 0:
                
                self.balance -= amount
                self.total_takes += 1
                
            else:
                print("You cannot take more money then what the current balance has.")
            
            
        else:
            print(f"ERROR! You can only take out balance 12 times within a year.")
        


class BSU_account(Bank_account):
    
    def __init__(self, owner: str, balance: float):
        super().__init__(owner, balance)
        
        self.interest_rate = 8/100
    
    def take_balance(self, amount = 0):
        amount = 0
        self.balance = amount
        
        

jimmy_account = BSU_account("Jimmy", 32903292309023390)
jimmy_account.take_balance()
jimmy_account.show_info()
