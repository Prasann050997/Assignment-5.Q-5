
class bank_account:
  def __init__(self, accountNumber, name, balance): # 1000
    self.accountNumber = accountNumber
    self.name = name
    self.balance = balance

  def deposit(self, d):
    self.balance = self.balance + d
  def Withdrawal(self , w): # 500
        if(self.balance < w):
          # 1000 < 500
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w # 1000 - 500 = 500
  def bankFees(self):
    self.balance = (95/100)*self.balance
  def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
newAccount = bank_account(2178514584, "Prasann" , 5000)
newAccount.Withdrawal(300)
newAccount.deposit(200)
newAccount.display()