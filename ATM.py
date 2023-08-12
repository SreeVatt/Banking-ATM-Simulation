import random
class ATM:
  def __init__(self, username, password, balance):
    self.username = username
    self.password = password
    self.balance = balance
  def login(self, entered_username, entered_password):
    return entered_username == self.username and entered_password == self.password
  def generate_otp(self):
    return random.randint(100000, 999999)
  def check_balance(self):
    print("Current Balance: ${}".format(self.balance))
  def contransaction(self,username):
    t = int(input("Do you want to continue the transactions:\n1.Continue Transaction\n2.Exit"))
    if (t == 1):
      self.transaction(username, password)
  def withdraw(self, amount):
    if self.balance >= amount:
      otp = self.generate_otp()
      print("OTP has been sent to your registered mobile number.")
      print('The OTP for your transaction is : ',otp)
      entered_otp = int(input("Enter the OTP received: "))
      if entered_otp == otp:
        self.balance -= amount
        print("Withdrawal successful. Remaining balance: ${}".format(self.balance))
      else:
        print("OTP verification failed. Withdrawal canceled.")
    else:
      print("Insufficient balance.")
  def deposit(self, amount):
    otp = self.generate_otp()
    print("OTP has been sent to your registered mobile number.")
    print('The OTP for your transaction is : ', otp)
    entered_otp = int(input("Enter the OTP received: "))
    if entered_otp == otp:
      self.balance += amount
      print("Deposit successful. Current balance: ${}".format(self.balance))
    else:
      print("OTP verification failed. Deposit canceled.")
  def transaction(self,username, password):
    if self.login(username, password):
      print("1. Check Balance")
      print("2. Withdraw")
      print("3. Deposit")
      print("4. Cancel")
      choice = int(input("Enter your choice: "))
      if (choice == 1):
        self.check_balance()
        self.contransaction(username)
      elif choice == 2:
        amount = float(input("Enter amount to withdraw: $"))
        self.withdraw(amount)
        self.contransaction(username)
      elif choice == 3:
        amount = float(input("Enter amount to deposit: $"))
        self.deposit(amount)
        self.contransaction(username)
    else:
      print("Invalid choice. Exiting")
my_atm = ATM("SreeVathsan", "123", 15000)
username = input("Enter username: ")
password = input("Enter password: ")
my_atm.transaction(username,password)