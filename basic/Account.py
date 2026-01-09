class Account:
    def __init__(self, account_num,balance):
        self.__account_num=account_num
        self.__b=balance

    def deposit(self,ammount):
        if ammount>0:
            self.__b+=ammount
            print("new baalnce",self.__b)
        return self.__b
    
    def withdraw_money(self,amount):
        if amount >0 and amount<self.__b:
            self.__b-=amount
        return self.__b
    
    def get_balance(self):
        return self.__b
    
amount=int(input("enter the amount to deposit:"))
account=Account("8718077458882",amount)
account.deposit(1)
try:
    self.__b+=2000000000
except:
    print("cant access directly alert!!!!")
print("the new balance after deposit moeny",account.get_balance())
account.withdraw_money(1)
print("the new balance after withdraw money",account.get_balance())