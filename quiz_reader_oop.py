import random

class QuizReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.question_list = self.load_questions()