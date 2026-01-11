from datetime import datetime, timedelta
# === 공통 계좌(부모) ===
class Account:
    def __init__ (self, owner, balance, interest_rate):
        self.owner = owner
        self.balance = balance
        self. interset_rate = interest_rate
        self.last_interest_date = datetime.now()
        self.history = []

    def record(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H %M")
        self.history.append(f"[{timestamp}] {message}")

    def add_monthly_inerest(self):
        now = datetime.now()
        if now - self.last_interest_date >= timedelta(days=30):
            interset = int(self.balance * self.interset_rate)
            self.balance += interset
            self.last_interest_date = now
            self.record(f"이자 {interset:,}원 지급")

    def show_balance(self):
        print(f"잔액: {self.balance:,}원")
    
    def save_history(self, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\n === {self.owner} 통장내역 === \n")
            for h in self.history:
                f.write(h+"\n")

# 자유 예금
class FreeAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        self.record(f"{amount:,}원 입금")

    def withdraw(self, amount):
        if amount > self.balance:
            self.record("출금 실패 ( 잔액부족 )")
        else:
            self.balance -= amount
            self.record(f"{amount:,}원 출금")


# 적금
class SavingAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        self.record(f"{amount:,}원 적금 입금")
    def withdraw(self, amount):
        self.record("출금 불가 ( 적금 계좌 )")


# 정기 예금
class FixedAccount(Account):
    def deposit(self, amount):
        self.record("입금 불가 ( 적금 계좌 )")
    def withdraw(self, amount):
        self.record("출금 불가 ( 적금 계좌 )")

#은행 관리 클래스
class Bank:
    def __init__ (self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)
        print(f"{account.owner} 계좌 개설 완료") 

    def monthly_process(self):
        for acc in self.accounts:
            acc.add_monthly_interset()
    
    def save_all_histories(self):
        for acc in self.accounts:
            acc.save_history("bank_history.txt")

# 실행
bank = Bank()

ac1 = FreeAccount("홍길동" , 500000, 00.2)
ac2 = SavingAccount("김철수", 20000, 0.03)
ac3 = FixedAccount("이영희", 50000, 0.04)

bank.create_account(ac1)
bank.create_account(ac2)
bank.create_account(ac3)

ac1.deposit(5000)
ac1.withdraw(3000)

ac2.deposit(20000)
ac2.withdraw(5000)

ac3.deposit(12000)

#한달 결과
for acc in bank.accounts:
    acc.last_interest_date -= timedelta(days=30)

bank.monthly_process()
bank.save_all_histories()