from BankAccount import BankAccount


allUserInfo = {}

while True:
    print(
        '''
Bank Class Simulation
1. 사용자 등록
2. 입급
3. 출금
4. 잔액 조회
5. 기록
6. 종료
'''
    )

    try:
        menu = int(input('메뉴 입력(숫자로): '))


        # 1. 사용자 등록
        if menu == 1:
            userName = input('사용자 이름 입력: ')
            allUserInfo[userName] = BankAccount(userName)


        # 2. 입금
        elif menu == 2:
            try:
                findUser = input('입금할 사용자 입력: ')
                if findUser in allUserInfo.keys():
                    amount = int(input('입금할 금액 입력: '))
                    allUserInfo[findUser].deposit(amount)

                else:
                    print('잘못된 사용자 이름!')

            except ValueError:
                print('잘못된 사용자 이름!')


        # 3. 출금
        elif menu == 3:
            try:
                findUser = input('입금할 사용자 입력: ')
                if findUser in allUserInfo.keys():
                    amount = int(input('출금할 금액 입력: '))
                    allUserInfo[findUser].withdraw(amount)

                else:
                    print('잘못된 사용자 이름!')
            except ValueError:
                print('잘못된 사용자 이름!')


        # 4. 사용자 잔액 조회
        elif menu == 4:
            try:
                findUser = input('입금할 사용자 입력: ')
                if findUser in allUserInfo.keys():
                    allUserInfo[findUser].show_balance()
                    
                else:
                    print('잘못된 사용자 이름!')
            except ValueError:
                print('잘못된 사용자 이름!')

        # 5. 사용자 입출금 이력
        elif menu == 5:
            try:
                findUser = input('입금할 사용자 입력: ')
                if findUser in allUserInfo.keys():
                    allUserInfo[findUser].show_history()
                    
                else:
                    print('잘못된 사용자 이름!')
            except ValueError:
                print('잘못된 사용자 이름!')
        

        # 6. 종료
        elif menu == 6:
            break
        
        
        # 나머지 값
        else:
            print('잘못된 값 입력')
    except ValueError:
        print('잘못된 값 입력')