class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Deposit: +${amount}')
            print(f'Deposit of ${amount} successful.')
        else:
            print('Deposit amount must be greater than zero.')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdrawal: -${amount}')
            print(f'Withdrawal of ${amount} successful.')
        elif amount > self.balance:
            print('Insufficient funds.')
        else:
            print('Withdrawal amount must be greater than zero.')

    def get_statement(self):
        print(f"Account Statement for Account {self.account_number}:")
        print(f"Current Balance: ${self.balance}")
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma conta bancária
    account1 = BankAccount('12345')

    # Realizando algumas operações
    account1.deposit(1000)
    account1.withdraw(500)
    account1.deposit(200)
    account1.get_statement()
