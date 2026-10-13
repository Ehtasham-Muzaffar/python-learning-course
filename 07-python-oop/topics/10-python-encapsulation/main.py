"""Python encapsulation: independent learner project. See README.md for purpose and use."""

class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    @property
    def balance(self) -> float:
        return self._balance

account = BankAccount(10)
account.deposit(5)
print(account.balance)
