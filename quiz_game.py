DEFAULT_DATA = {
    "quizzes": [
        {
            "question": "컴퓨터의 '두뇌' 역할을 하며 모든 연산과 제어를 담당하는 부품은 무엇인가요?",
            "choices": ["RAM", "CPU", "HDD", "GPU"],
            "answer": 2
        },
        {
            "question": "데이터를 일시적으로 저장하며, 전원이 꺼지면 내용이 사라지는 휘발성 메모리는?",
            "choices": ["SSD", "ROM", "RAM", "CPU"],
            "answer": 3
        },
        {
            "question": "그래픽 작업과 영상 출력을 전문적으로 처리하는 장치는?",
            "choices": ["GPU", "메인보드", "파워 서플라이", "사운드 카드"],
            "answer": 1
        },
        {
            "question": "반도체를 이용하여 데이터를 저장하며, HDD보다 속도가 훨씬 빠른 저장장치는?",
            "choices": ["CD-ROM", "SSD", "RAM", "USB 메모리"],
            "answer": 2
        },
        {
            "question": "모든 하드웨어 부품이 장착되어 서로 데이터를 주고받을 수 있게 연결해주는 판은?",
            "choices": ["케이스", "쿨러", "메인보드", "랜카드"],
            "answer": 3
        }
    ]
}

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def print_quiz(self):
        print(f'{self.question}\n')

        for i, choice in enumerate(self.choices):
            print(f'{i + 1}. {choice}')

    def confirm_answer(self):
        if get_num(False) == self.answer: return True
        return False

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
