class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("Dollars = $1000")
        print("Cents = 20")

    def withdrawl1(self,dollars):
        new_amount = 1000 - dollars

        if new_amount < 0:
            print("You can withdraw maximum value you have in your account")
        else:
            print("Thank you for withdrawing hope we will see you again...")
            print("You have successfully withdrawn amount of "+ str(dollars) + "$" + ". Your remaining balance is "+ str(new_amount) + "$")


    def withdrawl2(self,cents):
        new_amount = 20 - cents
        if new_amount < 0:
            print("You can withdraw maximum value you have in your account")
        else:
            print("Thank you for withdrawing hope we will see you again...")
            print("You have successfully withdrawn amount of "+ str(cents) + "¢" + ". Your remaining balance is "+ str(new_amount) + "¢")

def main():

    print("Welcome to US Stock Exchange !!")

    Account = int(input("Please enter your account number: "))
    Card_number = input("Insert your key number:- ")
    pin_number  = int(input("Enter your pin number:- "))

    new_user =  Atm(Account,Card_number,pin_number)

    print("ATM Started.......")

    print("Choose your activity")

    print("1.Balance Enquiry")
    print("2.Withdraw money")
    
    activity = int(input("Enter activity number (enter 1 or 2):- "))

    if (activity == 1):

        print("Here is your bank balance.")

        new_user.check_balance()

    elif (activity == 2):

        print("Initializing Withdrawal.........")

        print("Withdrawal process started")

        print("1. Withdraw Dollars ($)")
        print("2. Withdraw Cents(¢)")

        choose = int(input("Choose either 1 or 2"))

        if (choose == 1):
           dollars = int(input("Enter the amount($):- "))
           new_user.withdrawl1(dollars)
        if (choose == 2):
           cents = int(input("Enter the amount(¢):- "))
           new_user.withdrawl2(cents)
    else:
        print("Error 404 Bad Input !!")

if __name__ == "__main__":
    main()