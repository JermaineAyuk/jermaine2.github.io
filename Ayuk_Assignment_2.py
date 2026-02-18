# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Jermaine Ayuk
# Assignment Number: Lab #2
# Due Date: 02/18/2026
# Purpose: This program reads student names and six scores from an input file.
#          It calculates each student's final average and prints the results
#          in descending order by average grade.
# Resources Used: -Youtube Creator: Programming with Mosh, Bro Code, basic Python knowledge and class notes.

# -------------------------------------------------------------
# Ask the user for the input file name
# -------------------------------------------------------------

file_name = input("Enter the input file name: ")

students = []  # list to store (name, average)

# -------------------------------------------------------------
# Read the file and calculate averages for each student
# -------------------------------------------------------------
with open(file_name, "r") as file:
    for line in file:
        parts = line.split()  # split line into fields

        # First field is the student's name
        name = parts[0]

        # Remaining fields are the six scores
        scores = parts[1:]

        # Convert score strings to integers
        numeric_scores = [int(score) for score in scores]

        # Calculate the average of the six scores
        average = sum(numeric_scores) / len(numeric_scores)

        # Store the result as a tuple (name, average)
        students.append((name, average))

# -------------------------------------------------------------
# Sort students by average in descending order
# -------------------------------------------------------------
students.sort(key=lambda x: x[1], reverse=True)

# -------------------------------------------------------------
# Print results
# -------------------------------------------------------------
print("\nFinal Averages (Descending Order):")
for name, avg in students:
    print(f"{name} {avg:.2f}")
