class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def depsoit(self, amount):
        """입금"""
        self.balance += amount
        print(f"{amount:,}원 입금")
        self.show_balance()
    def withdraw(self, amount):
        """출금"""
        if amount>self.balance:
            print("잔액부족")
        else:
            self.balance -= amount
            print(f"{amount:,}원 출금")
            self.show_balance()
    def show_balance(self):
        print(f"잔액:{self.balance:,}원")

account = BankAccount("홍길동",20000)
account.depsoit(5000)
account.withdraw(3300)