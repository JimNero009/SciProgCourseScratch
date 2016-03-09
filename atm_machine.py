#!/usr/bin/env python3 


class ATMMachine(object):
    """
    This class is an ATM simulator
    """
    def __init__(self):
        self.account_number = 0
        self.accounts = []

    def make_a_withdraw(self, account_number, amount):
        """Withdraw (amount) from (account_number)"""
        [acc for acc in self.accounts if acc.account_number == account_number]
        acc.withdraw(amount)

    def make_a_deposit(self, account_number, amount):
        """Deposit (amount) into (account_number)"""
        [acc for acc in self.accounts if acc.account_number == account_number]
        acc.deposit(amount)

    def print_account_balance(self, account_number):
        """Print the Account Balance from (account_number)"""
        [acc for acc in self.accounts if acc.account_number == account_number]
        print acc.balance

    
    def make_a_transfer(self, from_account_number, to_account_number, amount):
        """Transfer (amount) from (from_account_number) to (to_account_number)"""
        #[toacc for toacc in self.accounts if toacc.account_number == to_account_number]
        #[fromacc for fromacc in self.accounts if fromacc.account_number == from_account_number]
        #fromacc.transfer_money(amount, toacc)
        self.accounts[0].transfer_money(amount,self.accounts[1])
        #This needs to be fixed


    def create_new_account(self, clients_name, initial_balance):
        """Create a new account that belongs to (clients_name) and has the (initial_balance)"""
        new_account = Account(self.account_number, clients_name, initial_balance)
        self.accounts.append(new_account)
        print "New account created for %s with number %d" % (clients_name, self.account_number)
        self.account_number += 1


class Account(object):
    """This class represents a simple Account"""
    def __init__(self, account_number, clients_name, initial_balance = 0.0):
        self.account_number = account_number
        self.clients_name = clients_name
        self.balance = initial_balance

    def withdraw(self, amount):
        """Withdraw some money!"""
        self.balance -= amount

    def deposit(self, amount):
        """Let's receive some money!"""
        self.balance += amount
    
    def check_balance(self):
        """Let's see how rich we are!"""
        return self.balance

    def transfer_money(self, amount, another_account):
        """Transfer money from this account to the other one"""
        self.withdraw(amount)
        another_account.deposit(amount)

class CheckingAccount(Account):

    def __init__(self, account_number, clients_name, initial_balance = 0.0):
        self.account_number = account_number
        self.clients_name = clients_name
        self.balance = initial_balance
        self.transfers = 0
        self.balancecheck = 0

    def transfer_money(self, amount, another_account):
        """Transfer money from this account to the other one"""
        self.withdraw(amount)
        another_account.deposit(amount)
        if(self.transfers > 4):
            self.withdraw(5)
        else:
            self.transfers = self.transfers + 1
        

    def check_balance(self):
        """Let's see how rich we are!"""
        if(self.balancecheck > 5):
            self.withdraw(1)
        else:
            self.balancecheck = self.balancecheck + 1
        return self.balance

    

class SavingsAccount(Account):

    def __init__(self, account_number, clients_name, initial_balance = 0.0):
        self.account_number = account_number
        self.clients_name = clients_name
        self.balance = initial_balance
        self.withdrawlcheck = 0

    def withdraw(self, amount):
        """Withdraw some money!"""
        if(self.withdrawlcheck < 3):
            self.balance -= amount
            self.withdrawlcheck = self.withdrawlcheck + 1
        else:
            self.balance -= (amount + 2)

    def transfer_money(self, amount, another_account):
        """Transfer money from this account to the other one"""
        self.withdraw(amount)
        another_account.deposit(amount)

def main():
    atm = ATMMachine()

    """This is the menu"""
    menu_text = """
    1 - Create new Account
    2 - Make a deposit
    3 - Withdraw money
    4 - Check your balance
    5 - Transfer money
    0 - Exit
    """
    while True:
        print("Welcome to the ATM machine")
        print("Choose one of the following options:")
        print(menu_text)
        selected_option = int(input("Option: "))
        print()
        
        if selected_option == 1:
            print("Register new Account:")
#            account_number = int(raw_input("Number: "))
            clients_name = str(raw_input("Name: "))
            initial_balance = float(raw_input("Initial Balance: "))
            account_type = str(raw_input("Specify account type: "))
            atm.create_new_account(clients_name, initial_balance)

        elif selected_option == 2:
            print("Make a deposit:")
            deposit_amount = float(raw_input("Enter amount to deposit: "))
            atm.make_a_deposit(account_number, deposit_amount)

        elif selected_option == 3:
            print("Withdraw money:")
            withdraw_amount = float(raw_input("Enter amount to withdraw: "))
            atm.make_a_withdraw(account_number, withdraw_amount)

        elif selected_option == 4:
            print("Check your balance:")
            print("Your total assests amount to: ")
            atm.print_account_balance(account_number)

        elif selected_option == 5:
            print("Transfer money:")
            from_account = int(raw_input("Enter account to transfer FROM: "))
            to_account = int(raw_input("Enter account to transfer TO: "))
            transfer_amount = float(raw_input("Enter amount to transfer: "))
            atm.make_a_transfer(from_account, to_account, transfer_amount)

        elif selected_option == 0:
            print("Bye Bye!")
            exit(0)
        else:
            print("Invalid option!")
        
        print()


if __name__ == '__main__':
    main()
