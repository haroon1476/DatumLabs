class BankAccount:

    # constructor
    def __init__(self, name, username, password, balance=0):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"{amount}Rs deposited successfully. New balance: {self.balance}Rs")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
       
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(" Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Rs {amount} withdrawed successfully. New balance: Rs{self.balance}")

    def check_balance(self):
      
        print(f" Current balance: {self.balance}Rs")

    # this func will be called for authentication purposes at the beginning of the program
    def authenticate(self, username, password):

        # Authentication is done only on the basis of username and password
        return self.username == username and self.password == password

    def innitiateAccount(name , username , password , initialBalance = 0):
        return BankAccount(name , username , password , initialBalance)

def main():

    print("Setting up your account!")
    name = input("Enter your name : ")
    userName = input("Enter your username : ")
    password = input("Enter password to set up : ")

    account = BankAccount.innitiateAccount(name , userName , password , 0) # Default balance on account creation set to 0

    # User authentication
    print("Please log in.")
    username = input("Username: ")
    password = input("Password: ")

    if not account.authenticate(username, password):
        print(" Incorrect username or password.")
        return

    print(" Authentication successful!")
    while True:

        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print(" Invalid amount. Please enter a number.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print(" Invalid amount. Please enter a number.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print(" Exited successfully.")
            break

        else:
            print(" Invalid choice. Please try again.")


# Main function call
main()