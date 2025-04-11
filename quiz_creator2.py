# Initialize main window (root) using Tkinter's Tk() class
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

# Use class QuizCreatorGUI to encapsulate the GUI logic
class QuizCreatorGUI:
    def __init__(self, root):
        
# Set title for main window
        self.root = root
        self.root.title("Quiz Creator")

# Call create_widgets method to set up GUI elements
        self.create_widgets()
# Initialize file name for saving quiz questions
        self.filename = "quiz_questions.txt"

# Define create_widgets method to create and arrange GUI elements
    def create_widgets(self):

# Create LabelFrame for question input
        question_frame = ttk.LabelFrame(self.root, text = "Question")
        question_frame.pack(padx = 10, pady = 10, fill = tk.X)

# Create Label and Entry widget for question
        self.question_label = ttk.Label(question_frame, text = "Enter the question:")
        self.question_label.pack(padx = 5, pady = 5)
        self.question_entry = ttk.Entry(question_frame, width = 50)
        self.question_entry.pack(padx = 5, pady = 5)

# Create LabelFrame for answer options
        answer_frame = ttk.LabelFrame(self.root, text = "Answers")
        answer_frame.pack(padx = 10, pady = 5, fill = tk.X)
        self.answer_labels = []
        self.answer_entries = []

# Create Label and Entry widget for each answer (a, b, c, d) using a loop
        for i, option in enumerate(['a', 'b', 'c', 'd']):
            label = ttk.Label(answer_frame, text = f"Enter option {option}")
            label.grid(row = i, column = 0, padx = 5, pady = 2, sticky = tk.W)
            self.answer_labels.append(label)

            entry = tk.Entry(answer_frame, width = 50)
            entry.grid(row = i, column = 1, padx = 5, pady = 2, sticky = tk.W)
            self.answer_entries.append(entry)

# Create LabelFrame for correct answer input
        correct_answer_frame = ttk.LabelFrame(self.root, text = "Correct Answer")
        correct_answer_frame.pack(padx = 10, pady = 5, fill = tk.X)

# Create Label and Entry widget for correct answer
        self.correct_answer_label = ttk.Label(correct_answer_frame, text = "Enter correct answer (a, b, c, d):")
        self.correct_answer_label.pack(padx = 5, pady = 5)
        self.correct_answer_entry = ttk.Entry(correct_answer_frame, width = 10)
        self.correct_answer_entry.pack(padx = 5, pady = 5)
        
# Create Frame to hold buttons
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(padx = 10, pady = 10, fill = tk.X)

# Create 'Add Question' and 'Exit' buttons with associated commands
        self.add_button = ttk.Button(buttons_frame, text = "Add Question", command = self.add_question)
        self.add_button.pack(side = tk.LEFT, padx = 5)

        self.exit_button = ttk.Button(buttons_frame, text = "Exit", command = self.exit_program)
        self.exit_button.pack(side = tk.RIGHT, padx = 5)

# Create a ScrolledText widget to display status messages
        self.status_text = scrolledtext.ScrolledText(self.root, height = 5, state = tk.DISABLED)
        self.status_text.pack(padx = 10, pady = 5, fill = tk.BOTH, expand = True)
        # Arrange all the created widgets using the pack and grid layout managers
# Define clear_entries to clear all input fields
    def clear_entries(self):
# Delete text in the question entry using the delete() method
        self.question_entry.delete(0, tk.END)

# Loop through each answer entry and clear its text
        for entry in self.answer_entries:
# Clear the correct answer entry
            entry.delete(0, tk.END)
# Clear the correct answer entry using the delete() method
        self.correct_answer_entry.delete(0, tk.END)

# Define validate_input to validate user input before adding a question
    def validate_input(self):
# Get the correct answer from the entry, convert it to lowewrcase, and remove leading/trailing spaces using the get(), lower(), and strip() methods
        correct_answer = self.correct_answer_entry.get().lower().strip()
# Check if the correct answer is one of the options (a, b, c, d), show error message using messagebox.showerror() and return false if not
        if correct_answer not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Input Error", "Invalid correct answer. Please enter a, b, c, or d.")
            return False
# If entry is empty, show error message and return false
        if not self.question_entry.get():
            messagebox.showerror("Input Error", "Question cannot be empty.")
# Loop through all answer entries and check if they are empty, show error message and return false if any are empty
        for entry in self.answer_entries:
            if not entry.get().strip():
                messagebox.showerror("Input Error", "Answers cannot be empty.")
                return False
# if all checks pass, return true
        return True
# Define add_question method to handle adding a question to the quiz
# Call validate_input to check if input is valid, if not, return
# Get the question and answers, and correct answer from the entry fields using the get() method
# Open file in append mode ('a') using the open() function
# Write the question and answers to the file using write() method
# Write each answer optioon (a, b, c, d) to the file
# Write the correct answer to the file
# Write a separator line (empty line) to the file
# Call update status to display success message
# Call clear_entries to clear all input fields
# Handle potential writing errors using try-except block and display and error message using messagebox.showerror() if necessary
# Define update_status method to display messages in the ScrolledText widget
# Enable status text widget for editing using the config(state=tk.NORMAL) method
# Insert the message at the end of the current text using insert(tk.END, message)
# Scroll to the end of the text using see(tk.END) method
# Disable the text widget for editing using config(state=tk.DISABLED) method
# Define exit_program method to close the application
# Display confirmation dialogue using messagebox.askokcancel()
# If user confirms, destroy the main window using root.destroy() method
# If user cancels, do nothing and return to the program
# Create the main Tkinter window (root) using tk.Tk()
# Create an instance of the QuizCreatorGUI class, passing the root window as an argument
# Start tkinter event loop to handle user interactions using root.mainloop() that responds to button clicks and user input