import os
import json

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

        list(map(lambda x: print(f'{x[[0]]}. {x[1]}'), enumerate(self.choices, 1)))

    def confirm_answer(self):
        return quiz_game.get_num(False) == self.answer

class QuizGame:
    def save_file(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def initialization(self):

        if not os.path.exists(FILE_NAME):
            print("⚠️ 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")
            self.save_file(DEFAULT_DATA)

        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            print("⚠️ 데이터 파일이 손상되었거나 읽을 수 없습니다. 기본 데이터로 복구합니다.")
            self.save_file(DEFAULT_DATA)
            self.data = DEFAULT_DATA

        self.quiz_list = [Quiz(quiz["question"], quiz["choices"], quiz["answer"]) for _, quiz in enumerate(data["quizzes"])]

        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quiz_list)}개, 최고점수 {int(data["best_score"] / len(self.quiz_list) * 100)}점)")
        print("========================================")

    def solve_quiz(self):
        for i in range(len(self.quiz_list)):
            self.quiz_list[i].print_quiz()
            if self.quiz_list[i].confirm_answer(): 
                print("정답입니다!")
                self.score = self.score + 1
            else: print("오답입니다!")

        if self.score > self.best_score:
            self.data["best_score"] = self.score
        
        print(f'총 {self.score}점 획득하셨습니다.')

    def add_quiz(self):
        print("📌 새로운 퀴즈를 추가합니다.\n")

        self.question = input("문제를 입력하세요: ")

        self.choices = [input(f"선택지 {i}") for i in range(1, 5)]

        self.answer = self.get_num(False)

        self.quiz_list.append(Quiz(self.question, self.choices, self.answer))

        self.data["quizzes"] = list(map(vars, self.quiz_list))

        self.save_file(self.data)

        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        print("----------------------------------------")
        list(map(lambda x: print(f"[{x[0]}] {x[1].question}"), enumerate(self.quiz_list, 1)))
        print("----------------------------------------")

    def show_quiz_score(self):
        quiz_count = len(self.quiz_list)
        print(f"🏆 최고 점수: {quiz_count * self.data["best_score"] * 100}점 ({quiz_count}문제 중 {self.data["best_score"]}문제 정답)")

    def process_data(self, choice):
        global score, highest_score

        match choice:
            case 1: self.solve_quiz()
            case 2: self.add_quiz()
            case 3: self.show_quiz_list()
            case 4: self.show_quiz_score() 

    def print_menu(self):
        print("========================================")
        print("🎯 나만의 퀴즈 게임 🎯")
        print("========================================")

        if len(self.quiz_list) < 1: self.initialization()

        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")   
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료") 
        print("========================================")

    def get_num(self, isMenu):
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
            self.save_file()
            return 0

        return choice

quiz_game = QuizGame()

while True:
    quiz_game.print_menu()
    choice = quiz_game.get_num(True) 

    if choice == -1: continue
    elif choice == 0 or choice == 5: break   
    else: quiz_game.process_data(choice)
