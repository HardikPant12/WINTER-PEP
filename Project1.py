"""
Design

"""

class BankAccount:
    def __init__(self,account_num,name,balance):
        self.account_num = account_num
        self.name = name
        self._balance= balance

    def deposite(self,amount):
        self._balance += amount
        return self._balance
    def withdraw(self,ammount):
        if(ammount<self._balance):
            self._balance-=ammount
            return self._balance
        else:
            return "Insufficient balance"
    def get_balance(self):
        return self._balance
    def calculate_intrest(self):
        pass

class SavingAccount(BankAccount):
    def calculate_intrest(self):
        intrest = self._balance *0.04
        return intrest

class CurrentAccount(BankAccount):
    def calculate_instrest(self):
        return 0;
class BankApp:
    def __init__(self):
        self.account = None
    def create_account(self,acc_no,name,balance,acc_type):
        if (acc_type =="saving "):
            self.account = SavingAccount(acc_no,name,balance)
        else:
            self.account = CurrentAccount(acc_no,name,balance)
        return "Account Created Successfully"
    def deposite_money(self,amount):
        return self.account.deposite(amount)
    def withdraw_money(self,amount):
        return self.account.withdraw(amount)
    def check_balance(self):
        return self.account.get_balance()
    def get_intrest(self):
        return self.account.calculate_intrest()

app = BankApp()
print(app.create_account(101,"Hardik",100000,"current"))
print("Balance after depositing = ",app.deposite_money(10000))
print("balance after Withdraw = ",app.withdraw_money(500000))
print("current balance = ",app.check_balance())
print("Intrest earned = ",app.get_intrest())


