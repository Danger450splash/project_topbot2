# Create a black market where you can buy specific food and item

import os, abstract

# Main Class
class BlackMarket(abstract.AbstractClass):

    # Constructor
    def __init__(self) -> None:
        self.loopPattern()
        self.__cash: int = 1000
        self.__savings: int = 1000
        print(f"My cash: {self.__cash}")
        self.market_menu()

    # Instance Method 1 (under Abstract)
    def market_menu(self) -> None:
        self.__user = input("Do you want to buy [foods], [items], or [atm]?: ")

        if self.__user == "foods":
            print("The user has select foods")
            print("Select a Food [burger], [fries], [nuggets]:")
            self.__foods()
        elif self.__user == "items":
            print("The user has select items")
            print("Select an Item [tshirt], [short], [watch], [umbrella]:")
            self.__items()
        elif self.__user == "atm":
            self.AuthenticateATM()
        else:
            print("Please try again")
            self.market_menu()

    # Instance Method 2 (under Abstract)
    def AuthenticateATM(self) -> None:
        print(f"Welcome to Automatic Cash Machine")
        self.__myusername = "Alpha Omega"
        self.__mypassword = "123456"

        self.__username = input("Username/Email: ")
        self.__password = input("Password: ")

        if self.__username == self.__myusername and self.__password == self.__mypassword:
            print(f'You have successfully login as {self.__username}')
            print(f'[1] - Check Savings Account' + "\n" + "[2] - Withdraw Savings Account" + "\n" + "[3] - Logout" + "\n")
            self.ATM()
        else:
            print("Please enter correctly your credentials.")
            self.AuthenticateATM()

    # Instance Method 3 (under Abstract)
    def ATM(self) -> None:
        self.__useratm = int(input("Select a method: "))
        
        if self.__useratm == 1:
            print(f'{self.__savings}')
            self.ATM()
        elif self.__useratm == 2:
            self.__userwithdraw = int(input("Enter the amount you want to withdraw: "))
            if self.__userwithdraw < self.__savings or self.__userwithdraw == self.__savings:
                self.__savings: int = self.__savings - self.__userwithdraw
                self.__cash: int = self.__cash + self.__userwithdraw
                print(f'Remaining Cash in Savings Account: {self.__savings}')
                print(f'Your hands-on Cash is now {self.__cash}')
                self.ATM()
            else:
                print("You don't have enought balance in your account.")
                self.ATM()

        elif self.__useratm == 3:
            print(f"You have logout as {self.__username}")
            self.market_menu()
        else:
            print("Enter one digit between 1-3 options in the ATM.")
            print(f'[1] - Check Savings Account' + "/n" + "[2] - Withdraw Savings Account" + "[3] - Logout")
            self.ATM()

    # Instance Method 4
    def __marketToATMOptions(self):
        self.__userchoice = int(input(f"Do you want to go back in the [1] market or withdraw in your [2] ATM?: "))

        if self.__userchoice == 1:
            self.market_menu()
        elif self.__userchoice == 2:
            self.AuthenticateATM()
        else:
            print("Please enter correctly the choices before proceeding beyond.")
            self.__marketToATMOptions()

    # Instance Method 5
    def __foods(self) -> None:
        self.__burger: int = 500
        self.__fries: int = 300
        self.__nuggets: int = 400

        self.__usersfood = input(" ")

        if self.__usersfood == "burger":
            if self.__cash >= self.__burger:
                os.system('cls')
                self.__cash: int = self.__cash - self.__burger
                print(f'You have purchased a burger.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the burger.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        elif self.__usersfood == "fries":
            if self.__cash >= self.__fries:
                os.system('cls')
                self.__cash: int = self.__cash - self.__fries
                print(f'You have purchased a fries.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the fries.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        elif self.__usersfood == "nuggets":
            if self.__cash >= self.__nuggets:
                os.system('cls')
                self.__cash: int = self.__cash - self.__nuggets
                print(f'You have purchased a nuggets.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the nuggets.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        else:
            os.system('cls')
            print("Program: Please correctly select a food in the menu...")
            print("[burger], [fries], [nuggets]?:")
            self.__foods()

    # Instance Method 6
    def __items(self) -> None:
        self.__tshirt: int = 100
        self.__short: int = 50
        self.__watch: int = 150
        self.__umbrella: int = 150

        self.__usersitem = input(" ")

        if self.__usersitem == "tshirt":
            if self.__cash >= self.__tshirt:
                os.system('cls')
                self.__cash: int = self.__cash - self.__tshirt
                print(f'You have purchased a T-Shirt.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the T-Shirt.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        elif self.__usersitem == "short":
            if self.__cash >= self.__short:
                os.system('cls')
                self.__cash: int = self.__cash - self.__short
                print(f'You have purchased a Short.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the Short.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        elif self.__usersitem == "watch":
            if self.__cash >= self.__watch:
                os.system('cls')
                self.__cash: int = self.__cash - self.__watch
                print(f'You have purchased a Watch.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the Watch.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        elif self.__usersitem == "umbrella":
            if self.__cash >= self.__umbrella:
                os.system('cls')
                self.__cash: int = self.__cash - self.__umbrella
                print(f'You have purchased a Umbrella.')
                print(f"Your cash remaining: {self.__cash}")
                self.market_menu()
            else:
                os.system('cls')
                print("You don't have enough cash to purchase the Umbrella.")
                print(f"Your cash remaining: {self.__cash}")
                self.__marketToATMOptions()

        else:
            os.system('cls')
            print("Program: Please correctly select an item in the menu...")
            print("[tshirt], [short], [watch], [umbrella]?:")
            self.__items()

    # Instance Method 7
    def loopPattern(self) -> None:
        self.stars = 5

        for self.rows in range(1, self.stars+1):
            self.num = 1
            for self.columns in range(self.stars+1, 0, -1):
                if self.columns > self.rows:
                    print(" ", end='')
                else:
                    print("*", end='')
                    self.num =+ 1
            print()