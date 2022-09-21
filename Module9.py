# Isaac Frett 9/21/2022 Module 9 Assignment
# The purpose of this code is to create a functional banking system that 
# alows for creation of checking and savings accounts with features of deposits and withdrawls

# In order to have to program quit
import sys

# This will be the parent class Bank Account
class BankAccount:

    # Initializing attributes for all Bank Accounts
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        
    # This will be our withdrawl function that will allow users to pull money from their account
    def withdrawl(self):
        try:
            self.balance = self.balance - float(input("How much money would you like to withdrawl?"))
            if type(self) == CheckingAccount:
                if self.balance < 50:
                    CheckingAccount.deductFees(self)
                else:
                    None
            else:
                None
            main(self)
        except TypeError:
            print("Please enter a valid number.")
            BankAccount.withdrawl(self)

    # This will be the deposit function for users to add money to their account
    def deposit(self):
        try:
            self.balance += float(input("How much money would you like to deposit?"))
            if self == CheckingAccount:
                CheckingAccount.checkMinimumBalance(self)
            else:
                main(self)
        except ValueError:
            print("Please enter a valid number.")
            BankAccount.deposit(self)

    # This function will be used to obtain the balance of an account at any time
    def getBalance(self):
        print("Your balance: $" + str("{:.2f}".format(self.balance)))
        main(self)

# This will be our checking account which uniquely has fees and minimum balances
class CheckingAccount(BankAccount):

    # initialize atrtibutes for a checking account
    def __init__(self, fees, minimumBalance, accountNumber, balance):
        self.fees = fees
        self.minimumBalance = minimumBalance
        super().__init__(accountNumber=accountNumber, balance=balance)

    # This will be our fees and will be deducted when the account goes below the minimum 
    def deductFees(self):
        self.balance = self.balance - self.fees
        print("Banking fee of $5 deducted from your account for being below the $50 minimum.")

    # This will check the minimum balance of our checking account to make sure users have more than $50
    # However they can still withdrawl money and be charged the fee for going below 50
    def checkMinimumBalance(self):
        if self.balance >= self.minimumBalance:
            print("Your balance of $" + str("{:.2f}".format(self.balance)) + " meets the minimum balance requirement.")
            main(self)
        else:
            print("Your balance of is below the minimum requirement. Please deposit $" + str("{:.2f}".format((50 - self.balance))) + " in order to meet the minimum requirement." )
            BankAccount.deposit(self)

# This is our second child class for a savings account that inherits attributes of a bank account
class SavingsAccount(BankAccount):

    # initialize interest rate and inherit the other attributes
    def __init__(self, interestRate, accountNumber, balance):
        self.interestRate = interestRate
        super().__init__(accountNumber=accountNumber, balance=balance)

    # This will add interest to a savings account once the account is created (normally on a monthly cycle)
    def addInterest(self):
        self.balance = self.balance + (self.balance * self.interestRate)
        print("Your current balance after interest is: $" + str("{:.2f}".format(self.balance)))


# This function will be our intro message and selection for the user to choose from
def run():
    print("What account would you like to make?")
    print("Checking\nSavings\nEnd")
    answer = str(input())
    checking = ["Checking", "checking"]
    savings = ["Savings", "savings"]
    end_program = ["End", "end"]
    if answer in checking:
        try:
            checking1 = CheckingAccount(5, 50, 1234567, float(input("What will your initial deposit be?")))
            checking1.checkMinimumBalance()
            checking1.deductFees()
            main(checking1)
        except ValueError:
            print("Please enter a valid number for a deposit.")
            run()
    elif answer in savings:
        try:
            savings1 = SavingsAccount(0.02, 2345678, float(input("What will your initial deposit be?")))
        except ValueError:
            print("Please enter a valid number for a deposit.")
        else:
            savings1.addInterest()
            main(savings1)
    elif answer in end_program:
        sys.exit()
    else:
        print("Please enter valid response")
        run()


# This function will be the main menu once our account is created allowing the user to perform actions on the account
def main(self):
    print("What action would you like to perform?")
    print("Balance\nDeposit\nWithdrawl\nExit\n")
    answer = str(input())
    balance = ["Balance", "balance"]
    deposit = ["Deposit", "deposit"]
    withdrawl = ["Withdrawl", "withdrawl"]
    exit = ["Exit", "exit"]
    if answer in balance:
        BankAccount.getBalance(self)
    elif answer in deposit:
        BankAccount.deposit(self)
    elif answer in withdrawl:
        BankAccount.withdrawl(self)
    elif answer in exit:
        run()
    else:
        print("Please enter valid response")
        main(self)

run()

# The program keeps the user in it unless they type Exit and End respectively at each prompt in order to quit the program
