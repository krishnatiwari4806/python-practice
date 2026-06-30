class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
========= ATM MENU =========

1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw
5. Exit

Enter your choice: """)

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.change_pin()

            elif user_input == "3":
                self.check_balance()

            elif user_input == "4":
                self.withdraw()

            elif user_input == "5":
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid Choice! Please try again.")

    def create_pin(self):
        self.pin = input("Create your PIN: ")
        self.balance = int(input("Enter Initial Balance: "))
        print("✅ PIN Created Successfully!")

    def change_pin(self):
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter New PIN: ")
            self.pin = new_pin
            print("✅ PIN Changed Successfully!")
        else:
            print("❌ Incorrect PIN!")

    def check_balance(self):
        user_pin = input("Enter Your PIN: ")

        if user_pin == self.pin:
            print(f"💰 Your Balance is: ₹{self.balance}")
        else:
            print("❌ Incorrect PIN!")

    def withdraw(self):
        user_pin = input("Enter Your PIN: ")

        if user_pin == self.pin:

            amount = int(input("Enter Amount to Withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ ₹{amount} Withdrawn Successfully!")
                print(f"💰 Remaining Balance: ₹{self.balance}")
            else:
                print("❌ Insufficient Balance!")

        else:
            print("❌ Incorrect PIN!")


# Object Creation
obj = Atm()