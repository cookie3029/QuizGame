import os
import json

quiz_list = []
score = 0
highest_score = 0
data = {}

FILE_NAME = "state.json"

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
    ],
    "best_score":0
}

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def print_quiz(self):
        print(f'{self.question}\n')

        for i in range(len(self.choices)):
            print(f'{i + 1}. {self.choices[i]}')

    def confirm_answer(self):
        if get_num(False) == self.answer: return True
        return False

class QuizGame:

    def save_file(data):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def initialization(self):
        global data

        if not os.path.exists(FILE_NAME):
            print("⚠️ 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")
            self.save_file(DEFAULT_DATA)

        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            print("⚠️ 데이터 파일이 손상되었거나 읽을 수 없습니다. 기본 데이터로 복구합니다.")
            data = DEFAULT_DATA
            self.save_file(data)

        for _, quiz in enumerate(data["quizzes"]):
            quiz_list.append(Quiz(quiz["question"], quiz["choices"], quiz["answer"]))        

        highest_score = data["best_score"]

        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quiz_list)}개, 최고점수 {int(highest_score / len(quiz_list) * 100)}점)")
        print("========================================")

    def add_quiz(self):
        global data

        choices = []

        print("📌 새로운 퀴즈를 추가합니다.\n")

        question = input("문제를 입력하세요: ")

        for i in range(1, 5):
            choices.append(input(f"선택지 {i}"))

        answer = get_num(False)

        quiz_list.append(Quiz(question, choices, answer))

        data["quizzes"] = list(map(vars, quiz_list))

        self.save_file(data)

        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        print("----------------------------------------")
        list(map(lambda x: print(f"[{x[0]}] {x[1].question}"), enumerate(quiz_list, 1)))
        print("----------------------------------------")

    def show_quiz_score(self):
        quiz_count = len(quiz_list)
        print(f"🏆 최고 점수: {quiz_count * data["best_score"] * 100}점 ({quiz_count}문제 중 {data["best_score"]}문제 정답)")

    def process_data(self, choice):
        global score, highest_score

        match choice:
            case 1: 
                for i in range(len(quiz_list)):
                    quiz_list[i].print_quiz()
                    if quiz_list[i].confirm_answer(): 
                        print("정답입니다!")
                        score = score + 1
                    else: print("오답입니다!")

                if highest_score < score:
                    highest_score = score

                data["best_score"] = highest_score
                
                print(f'총 {score}점 획득하셨습니다.')
            case 2: self.add_quiz()
            case 3: self.show_quiz_list()
            case 4: self.show_quiz_score() 

def print_menu():
    print("========================================")
    print("🎯 나만의 퀴즈 게임 🎯")
    print("========================================")

    if len(quiz_list) < 1: initialization()

    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")   
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료") 
    print("========================================")

def get_num(isMenu):
    if isMenu: player_num = input("선택: ").strip()
    else: player_num = input("정답 입력: ").strip()

    try:
        choice = int(player_num)

        if (isMenu and (choice > 5 or choice < 1)) or (not isMenu and (choice > 4 or choice < 1)):
            raise ValueError
    except ValueError:
        if isMenu:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
        else:
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
        return -1
    except (KeyboardInterrupt, EOFError):
        print("⚠️ 프로그램을 비정상적으로 종료되었습니다.")
        print("⚠️ 데이터를 저장하고 프로그램을 종료합니다.")
        return 0

    return choice



while True:

    print_menu()

    choice = get_num(True) 

    if choice == -1: continue
    elif choice == 0 or choice == 5: break   
    else: process_data(choice)
