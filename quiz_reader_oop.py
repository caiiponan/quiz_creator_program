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
            