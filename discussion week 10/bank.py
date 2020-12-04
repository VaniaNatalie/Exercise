class Account:
    def __init__(self, balance=1000):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False

class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.account = Account()

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getAccount(self):
        return self.account

    def setAccount(self, account):
        self.account = account


class Bank:
    numberOfCustomers = 0

    def __init__(self, bankName, customers):
        self.bankName = bankName
        self.customers = customers

    def __str__(self):
        return f'{self.customers}'

    def addCustomers(self, firstname, lastname):
        return self.customers.append(Customer(firstname, lastname))

    def getnumberOfCustomers(self):
        return self.numberOfCustomers

    def getCustomer(self, index):
        return self.customers[index]

def menu():
    return int(input("What are you going to do?\n1. Login as staff\n2. Login as customer\n3. Add customer account\n4. Quit\n"))

def custMenu():
    return int(input("What are you going to do?\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Back to main menu\n"))

def staffMenu():
    return int(input("What are you going to do?\n1. Check number of customers\n2. Get customers based on index\n"
              "3. Back to main menu\n"))