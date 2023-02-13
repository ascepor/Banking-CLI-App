class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, code, name):
        if code in self.accounts:
            print(f"Account with code {code} already exists.")
        else:
            self.accounts[code] = {"name": name, "balance": 0}
            print(f"Account {code} has been created for {name}.")

    def deposit(self, code, amount):
        if code in self.accounts:
            self.accounts[code]["balance"] += amount
            print(f"Amount of {amount} has been deposited to {code}.")
        else:
            print(f"Account with code {code} does not exist.")

    def withdraw(self, code, amount):
        if code in self.accounts:
            if self.accounts[code]["balance"] >= amount:
                self.accounts[code]["balance"] -= amount
                print(f"Amount of {amount} has been withdrawn from {code}.")
            else:
                print(f"Insufficient balance in account {code}.")
        else:
            print(f"Account with code {code} does not exist.")

    def show_balance(self, code):
        if code in self.accounts:
            print(f"{self.accounts[code]['name']} {self.accounts[code]['balance']}")
        else:
            print(f"Account with code {code} does not exist.")


if __name__ == "__main__":
    bank = Bank()

    while True:
        action = input("Enter action (CREATE, DEPOSIT, WITHDRAW, BALANCE, EXIT): ")

        if action == "EXIT":
            break
        elif action == "CREATE":
            code = input("Enter account code: ")
            name = input("Enter account name: ")
            bank.create_account(code, name)
        elif action == "DEPOSIT":
            code = input("Enter account code: ")
            amount = int(input("Enter deposit amount: "))
            bank.deposit(code, amount)
        elif action == "WITHDRAW":
            code = input("Enter account code: ")
            amount = int(input("Enter withdrawal amount: "))
            bank.withdraw(code, amount)
        elif action == "BALANCE":
            code = input("Enter account code: ")
            bank.show_balance(code)
        else:
            print("Invalid action.")
