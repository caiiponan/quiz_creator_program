import random
import os

# Create function to load questions from file
def load_questions(file_name = 'quiz.txt'):
    # Error handling
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        # Initialize variables as empty lists and dictionaries
        question_list = []
        question_data = {}
        
        for line in lines:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
        
        # Save previous questions if a new one starts
        if line.startswith('Question:'):
            if question_data:
                question_list.append(question_data)
                question_data = {}
            question_data['question'] = line.split(':', 1)[1].strip()
            # Initialize options
        elif line.startswith('a.') or line.startswith('a'):
            question_data['option_a'] = line[2:].strip() if line.startswith('a.') else line[1:].strip()
        elif line.startswith('b.') or line.startswith('b'):
            question_data['option_b'] = line[2:].strip() if line.startswith('b.') else line[1:].strip()
        elif line.startswith('c.') or line.startswith('c'):
            question_data['option_c'] = line[2:].strip() if line.startswith('c.') else line[1:].strip()
        elif line.startswith('d.') or line.startswith('d'):
            question_data['option_d'] = line[2:].strip() if line.startswith('d.') else line[1:].strip()
        elif line.startswith('Correct Answer:'):
            # Strip trailing spaces just to get the letter
            correct_answer = line.split(':', 1)[1].strip().lower()
            # Remove any period after the answer letter if present
            question_data['correct_answer'] = correct_answer[0]
        # Add question to the list
        if question_data:
            question_list.append(question_data)

        return question_list
# Handle error if error is FileNotFoundError
    except FileNotFoundError:
        print("Quiz file not found")
        return []

# Function to start the quiz
def start_quiz(question_list):
    print("\n\033[94m--- Welcome to the Quiz Game! ---\033[0m")
    # Randomize the questions
    random.shuffle(question_list)
    total_score = 0

    # Display the questions and options
    for question_number, question in enumerate(question_list, 1):
        print(f"\nQuestion {question_number}: {question['question']}")
        print(f"a) {question['option_a']}")
        print(f"b) {question['option_b']}")
        print(f"c) {question['option_c']}")
        print(f"d) {question['option_d']}")

        user_answer = input("Your answer (a/b/c/d): ").lower()
        while user_answer not in {'a', 'b', 'c', 'd'}:
            user_answer = input("Please enter a valid option (a/b/c/d): ").lower()
    # Validate the correct answer
        correct_key = question.get('correct_answer')
        if correct_key not in {'a', 'b', 'c', 'd'}:
            print("\033[91mError: Invalid or missing correct answer key in the question data.\033[0m")
            print(f"Debug: Question data: {question}")  # Debug output
            continue
    # Get correct option text
        correct_text = question.get(f"option_{correct_key}")
        if not correct_text:
            print("\033[91mError: Missing option for the correct answer key.\033[0m")
            print(f"Debug: Question data: {question}")  # Debug output
            continue
    # Add score if answer is correct
        if user_answer == correct_key:
            print("\033[92mCorrect!\033[0m")
            total_score += 1
    # No score if answer is incorrect
        else:
            print(f"\033[91mWrong! Correct answer was: {correct_key}) {correct_text}\033[0m")
    # Display final score
    print(f"\n\033[96mYour final score is {total_score}/{len(question_list)}.\033[0m")
    print("\033[93mThanks for playing!\033[0m")

# Main function to run the quiz
if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    questions_from_file = load_questions('quiz.txt')
    if questions_from_file:
        start_quiz(questions_from_file)