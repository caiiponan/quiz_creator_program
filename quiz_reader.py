import random

# Create function to load questions from file
def load_questions(file_name = "quiz_questions.txt"):
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
    # Get correct option text
        # Debug output
    # Add score if answer is correct
    # No score if answer is incorrect
    # Display final score
# Main function to run the quiz