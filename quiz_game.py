def print_menu():
    print("========================================")
    print("🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")   
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료") 
    print("========================================")

def get_num(isMenu):
    if isMenu: player_num = input("선택: ").strip()
    else: player_num = input("정답 입력: ")

    try:
        choice = int(player_num)

        if (isMenu and (choice > 5 or choice < 1)) or (not isMenu (choice > 4 or choice < 1)):
            raise ValueError
    except ValueError:
        print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
        return -1
    except (KeyboardInterrupt, EOFError):
        print("⚠️ 프로그램을 비정상적으로 종료되었습니다.")
        print("⚠️ 데이터를 저장하고 프로그램을 종료합니다.")
        return 0

    return choice

def process_data(choice):
    match choice:
        case 1: print("퀴즈 풀기")
        case 2: print("퀴즈 추가")
        case 3: print("퀴즈 목록")
        case 4: print("점수 화인")   

while True:
    print_menu()

    choice = get_num(True) 

    if choice == -1: continue
    elif choice == 0 or choice == 5: break   
    else: process_data(choice)
