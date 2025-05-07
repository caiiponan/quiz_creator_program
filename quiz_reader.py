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
        # Strip trailing spaces just to get the letter
        # Remove any period after the answer letter if present
    # Add question to the list
# Handle error if error is FileNotFoundError
# Function to start the quiz
    # Randomize the questions
    # Display the questions and options
    # Validate the correct answer
    # Get correct option text
        # Debug output
    # Add score if answer is correct
    # No score if answer is incorrect
    # Display final score
# Main function to run the quiz