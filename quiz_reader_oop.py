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