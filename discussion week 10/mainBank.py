from bank import Bank, menu, custMenu, staffMenu

if __name__ == "__main__":
    staffDict = {"BCA1":"12345", "BCA2":"abcde"}
    customerDict = {}
    customerCounter = 0
    ans = menu()
    BCA = Bank("BCA", [])
    while ans != 4:
        if ans == 1:
            username = input("Input staff's username: ")
            password = input("Input staff's password: ")
            if username in staffDict and password == staffDict[username]:
                ansStaff = staffMenu()
                while 0 < ansStaff < 3:
                    if ansStaff == 1:
                        print(BCA.getnumberOfCustomers())
                        ansStaff = staffMenu()
                    elif ansStaff == 2:
                        index = int(input("Input index of cust: "))
                        print(BCA.getCustomer(index).getFirstName().getLastName)
                        ansStaff = staffMenu()
                ans = menu()
            else:
                print("You're not the staff")
                ans = menu()
        elif ans == 2:
            firstName = input("Input first name: ")
            lastName = input("Input last name: ")
            index = int(input("Input your customer number: "))
            if firstName in customerDict and lastName == customerDict[firstName][0] and index == customerDict[firstName][1]:
                ansCust = custMenu()
                while 0 < ansCust < 4:
                    if ansCust == 1:
                        deposit = int(input("How much do you want to deposit? "))
                        BCA.getCustomer(index).getAccount().deposit(deposit)
                        print("The current amount is", BCA.getCustomer(index).getAccount().getBalance())
                        ansCust = custMenu()
                    elif ansCust == 2:
                        withdraw = int(input("How much do you want to withdraw? "))
                        BCA.getCustomer(index).getAccount().withdraw(withdraw)
                        print("The current amount is", BCA.getCustomer(index).getAccount().getBalance())
                        ansCust = custMenu()
                    elif ansCust == 3:
                        print("The current amount is", BCA.getCustomer(index).getAccount().getBalance())
                        ansCust = custMenu()
                ans = menu()
            else:
                print("You don't have an account or your index number is wrong.")
                ans = menu()
        elif ans == 3:
            firstName = str(input("Input first name: "))
            lastName = str(input("Input last name: "))
            customerDict[firstName] = [lastName, customerCounter]
            BCA.addCustomers(firstName, lastName)
            deposit = input("Do you want to add more from the default deposit 1000? (Y/N)? ")
            if deposit == 'Y':
                deposit = int(input("How much more? "))
                BCA.getCustomer(-1).getAccount().deposit(deposit)
                print("The current amount is", BCA.getCustomer(-1).getAccount().getBalance())
                print("Your account number is", customerCounter)
                customerCounter += 1
            elif deposit == 'N':
                print("The current amount is", BCA.getCustomer(-1).getAccount().getBalance())
                print("Your account number is", customerCounter)
                customerCounter += 1
            ans = menu()
    print("ThankYou!")
