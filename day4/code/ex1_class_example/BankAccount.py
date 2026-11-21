# 클래스 예제: 은행 계좌 (BankAccount)
# - __init__ 으로 객체 생성 시 속성 초기화
# - self 로 객체 자신의 속성에 접근
# - 메서드로 입금 / 출금 / 잔액 조회 기능 구현


class BankAccount:
    def __init__(self, owner, balance=0):
        self.bank = '파이썬 은행'      # 모든 계좌에 공통으로 들어가는 값
        self.owner = owner             # 예금주
        self.balance = balance         # 잔액
        self.history = []              # 거래 내역


    def deposit(self, amount):
        if amount <= 0:
            print('입금액은 0원보다 커야 합니다.')
            return

        self.balance += amount
        self.history.append(f'입금 +{amount}원')
        print(f'{self.owner}님 {amount}원 입금 완료')


    def withdraw(self, amount):
        if amount > self.balance:
            print(f'잔액 부족! (현재 잔액: {self.balance}원)')
            return

        self.balance -= amount
        self.history.append(f'출금 -{amount}원')
        print(f'{self.owner}님 {amount}원 출금 완료')


    def show_balance(self):
        print(f'[{self.bank}] {self.owner}님의 잔액: {self.balance}원')


    def show_history(self):
        print(f'--- {self.owner}님 거래 내역 ---')
        for h in self.history:
            print(h)


if __name__ == '__main__':
    # 객체 생성: 같은 클래스로 서로 다른 계좌 2개 만들기
    acc1 = BankAccount('홍길동', 10000)
    acc2 = BankAccount('김철수')

    acc1.deposit(5000)
    acc1.withdraw(3000)
    acc1.withdraw(50000)     # 잔액 부족 상황
    acc1.show_balance()
    acc1.show_history()

    print()

    acc2.deposit(20000)
    acc2.show_balance()
