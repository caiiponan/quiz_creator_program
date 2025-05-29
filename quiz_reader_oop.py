import random

class QuizReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.question_list = self.load_questions()
    
    def load_questions(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("The file is empty.")
                    return []
        except FileNotFoundError:
            print(f"Error: The file '{self.file_name}' was not found.")
            return []
        
        question_list = []
        question_data = {}

        for line in lines:
            line.strip()
            if not line:
                continue

            if line.startswith('Question:'):
                if question_data:
                    question_list.append(question_data)
                    question_data = {}
                question_data['question'] = line.split(':', 1)[1].strip()
            elif line.startswith('a.') or line.startswith('a'):
                question_data['option_a'] = line[2:].strip()
            elif line.startswith('b.') or line.startswith('b'):
                question_data['option_b'] = line[2:].strip()
            elif line.startswith('c.') or line.startswith('c'):
                question_data['option_c'] = line[2:].strip()
            elif line.startswith('d.') or line.startswith('d'):
                question_data['option_d'] = line[2:].strip()
            elif line.startswith('Correct Answer:'):
                correct_answer = line.split(':', 1)[1].strip().lower()
                question_data['correct_answer'] = correct_answer[0]

        if question_data:
            question_list.append(question_data)

        return question_list
    
    def start_quiz(question_list):
        if not question_list:
            print("No valid questions were loaded. Exiting the quiz.")
            return
        
        print("\n\033[94m--- Welcome to the Quiz Game! ---\033[0m")
        random.shuffle(question_list)
        total_score = 0

        for question_number, question in enumerate(question_list, 1):
            print(f"\nQuestion {question_number}: {question['question']}")
            print(f"a) {question['option_a']}")
            print(f"b) {question['option_b']}")
            print(f"c) {question['option_c']}")
            print(f"d) {question['option_d']}")

        user_answer = input("Your answer (a/b/c/d): ").lower()
        while user_answer not in {'a', 'b', 'c', 'd'}:
            user_answer = input("Please enter a valid option (a/b/c/d): ").lower()

        correct_key = question.get('correct_answer')
        correct_text = question.get(f"option_{correct_key}", "Unknown")

        if user_answer == correct_key:
            print("\033[92mCorrect!\033[0m")
            total_score += 1
        else:
            print(f"\033[91mWrong! Correct answer was: {correct_key}) {correct_text}\033[0m")

        print(f"\n\033[96mYour final score is {total_score}/{len(question_list)}.\033[0m")
        print("\033[93mThanks for playing!\033[0m")