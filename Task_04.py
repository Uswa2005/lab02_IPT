# Task 4: Student Marks, Total, and Average Calculation

# Take student information
name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")

# Take marks in three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average marks
total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

# Display student information and results
print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
