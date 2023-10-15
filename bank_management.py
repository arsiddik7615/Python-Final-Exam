from abc import ABC,abstractmethod
import random

class Account(ABC):
    accounts ={}
    transaction_history={}

    def __init__(self,name ,email,address,accType) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.accNo=len(Account.accounts)+1
        self.accType=accType
        self.balance=0
        self.transaction=0
        self.loan_taken=0
        self.loan_limit=2

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            Account.transaction_history[self.accNo] = print(f"Deposited ${amount}")

        else:
            print('\nInvalid amount') 
    def withdraw(self,amount):
        if amount>=0 and amount<=self.balance:
            self.balance-=amount
            Account.transaction_history[self.accNo] = print(f"Withdrawl Amoundt ${amount}")

        else:
            print('Withdrawal amount exceeded')

    def check_balance(self):
        print(f"Available Balance: ${self.balance}")

        
    def loan(self,amount):
        
        if self.loan_limit>0:
            self.loan_taken+=amount
            self.balance+=amount
            self.loan_limit-=1
            Account.transaction_history[self.accNo] =  print(f"Took a loan amount: ${amount}\nAfter taken Loan Main Balance: ${self.balance}")
           
            
        else:
            print("Unable to take loan at this moment")
    def transfer(self,rcvAcc,amount):
        if rcvAcc in Account.accounts:
            receiver= Account.accounts[rcvAcc]
            if amount<=self.balance:
                self.balance-=amount
                receiver.balance+=amount
                Account.transaction_history[self.accNo]
                print(f"Transeferred ${amount}to {receiver.name}")
                print(f"Account Number : {receiver.accNo}")
            else:
                print(" Insuffisient Balance for the transfer")
        else:
            print("Account does not exist")
    @abstractmethod
    def show_info(self):
        pass


class SavingsAccount(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address, "savings")

    def show_info(self):
        print(f"Account Type: {self.accType}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.accNo}")
        print(f"Current Balance: ${self.balance}")

class CurrentAccount(Account):
    def __init__(self, name, email, address ) -> None:
        super().__init__(name, email, address,"current")

    def show_info(self):
        print(f"Account Type: {self.accType}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.accNo}")
        print(f"Current Balance: ${self.balance}")


class Admin:
    @staticmethod
    def create_account(name,email,address,accType):
        if accType=="savings":
            account= SavingsAccount(name,email,address)
        elif accType=="current":
            account= CurrentAccount(name,email,address)
        else:
            print(" Invalid Account")

    @staticmethod
    def delete_account(accNo):
        if accNo in Account.accounts:
            del Account.accounts[accNo]
            del Account.transaction_history[accNo]
            print("Account Delete successfully")
        else:
            print(" Account doesnt exist")

    @staticmethod
    def list_all_acc():
        for accNo,account in Account.accounts.items():
            print(f"Account NUmber: {accNo}")
            print(f"Name: {account.name}")
    @staticmethod
    def total_bank_amnt():
        total_amnt=  sum(account.balance for account in Account.accounts.values())
        print(f"Total Loan amount: ${total_amnt}")
    @staticmethod
    def total_loan_amnt():
        total_loan=  sum(account.loan_taken for account in Account.accounts.values())
        print(f"Total Loan amount: ${total_loan}")

while(True):
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    user_ch=int(input("Select user type: "))
    if user_ch==1:
        print("1.Create Account")
        print("2. Login")
        print("3. Exit")
        user_option=int(input("Select user option: "))
        if user_option==1:
            name=input("Name: ")
            email=input("Email: ")
            address=input("Address: ")
            print("Account Types: ")
            print("1. Saving ")
            print("2. Current ")
            acc_typ_ch=input("select your type: ")
            if acc_typ_ch==1:
               accType="savings"
               Admin.create_account(name,email,address)
            elif acc_typ_ch==2:
                accType="current"
                Admin.create_account(name,email,address)
            else:
                print("Invalid naiin account type")
                continue
            
    elif user_ch==2:
        admin_pass="admin"
        password=input("Enter admin password: ")
        if password == admin_pass:
                name=input("Name: ")
                email=input("Email: ")
                address=input("Address: ")
                print("\n1. Create Account")
                print("\n2. Delete Account")
                print("\n3. List All Accounts")
                print("\n4. Total Bank Balance")
                print("\n5. Total Loan Amount")
                print("\n6. Exit")
                admin_option = int(input("Select admin option: "))

                if admin_option == 1:
                    Admin.create_account(name,email,address)
                elif admin_option==2:
                    Admin.delete_account()
                elif admin_option==3:
                    Admin.list_all_acc()
                elif admin_option==4:
                    Admin.total_bank_amnt()
                elif admin_option==5:
                    Admin.total_loan_amnt()
                elif admin_option==6:
                    print("Successfully exit")
    elif user_option==3:
        print("\nExit from user interface")
    
    else:
        print("\nInvalid option")
     
            