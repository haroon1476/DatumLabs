import logging

# Info , error , warning , critical , debug

# ------------ BankAccount Class ------------
class BankAccount:
    def __init__(self, owner, balance=0):
        logging.info(f"Creating account for {owner}")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):

            # Using error type of logging
            logging.error("Deposit failed: Amount must be num   eric.")
            return
        
        if amount <= 0:
            # Using warning type of logging
            logging.warning("Deposit amount should be positive.")
            return
        
        self.balance += amount

        # using info type of logging
        logging.info(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            logging.error("Withdrawal failed: Amount must be numeric.")
            return
        
        if amount > self.balance:
            logging.critical(f"Insufficient funds! Attempted to withdraw ${amount}, balance is ${self.balance}")
            return
        
        self.balance -= amount
        logging.info(f"{self.owner} withdrew ${amount}. Remaining balance: ${self.balance}")

    def check_balance(self):
        logging.debug(f"Checking balance for {self.owner}")
        return self.balance


account = BankAccount("Alice", 1000)
account.deposit(500)
account.deposit("invalid")        
account.withdraw(200)
account.withdraw(5000)
print(f"Final Balance: ${account.check_balance()}")