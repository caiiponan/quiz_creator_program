# Initialize main window (root) using Tkinter's Tk() class
# Use class QuizCreatorGUI to encapsulate the GUI logic
# Set title for main window
# Define create_widgets method to create and arrange GUI elements
# Call create_widgets method to set up GUI elements
# Initialize file name for saving quiz questions
# Create LabelFrame for question input
# Create Label and Entry widget for question
# Create LabelFrame for answer options
# Create Label and Entry widget for each answer (a, b, c, d) using a loop
# Create LabelFrame for correct answer input
# Create Label and Entry widget for correct answer
# Create Frame to hold buttons
# Create 'Add Question' and 'Exit' buttons with associated commands
# Create a ScrolledText widget to display status messages
# Arrange all the created widgets using the pack and grid layout managers
# Define clear_entries to clear all input fields
# Delete text in the question entry using the delete() method
# Loop through each answer entry and clear its text
# Clear the correct answer entry
# Define validate_input to validate user input before adding a question
# Get the correct answer from the entry, convert it to lowewrcase, and remove leading/trailing spaces using the get(), lower(), and strip() methods
# Check if the correct answer is one of the options (a, b, c, d), show error message using messagebox.showerror() and return false if not
# If entry is empty, show error message and return false
# Loop through all answer entries and check if they are empty, show error message and return false if any are empty
# if all checks pass, return true
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
