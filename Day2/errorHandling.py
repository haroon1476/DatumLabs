def applyDivision():

    try:
        # This part of code may generate some kind of exception
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        result = num1/num2
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError as e:
        print("Valid value not entered")
    else:
        print(f"Result of the operation is {result}")
    finally:
        print("Operation complete successfully")


    return

#applyDivision()


# <---------- CREATING A BANK CLASS TO DEMONSTRATE TRY AND CATCH STATEMENTS

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            #  self.balance += amount
            if not isinstance(amount, (int, float)):
                raise ValueError("Deposit amount must be positive.")
            #     raise TypeError("Amount must be a number (int or float).")
            # if amount <= 0:
            #     raise ValueError("Deposit amount must be positive.")
            # else:
            #     self.balance += amount
            #     print(f"Deposited ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Deposit value error: {e}")
        except Exception as e:
            print(f"Some unexpected error {e} occured")

    def withdraw(self, amount):
        try:
            if not isinstance(amount , (int, float)):
                raise TypeError("Amount must be a number (int , flaot).") 
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds in account.")
            else:
                self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Withdrawal Error: {e}")
        except Exception as e:
            print(f"Unexpected error during withdrawal: {e}")

    def show_balance(self):
        print(f"{self.owner}'s current balance: ${self.balance:}")



bankAccount = BankAccount("Haroon Ur Rasheed",50000.00)
bankAccount.deposit("a")
print(bankAccount.balance)
bankAccount.show_balance()