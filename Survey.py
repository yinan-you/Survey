# Yinan You 2/12/2024
# First Survey

import csv

# Define your questions
questions = [
    "School",
    "Univeristy",
    "Age",
    "WAM",
    "ATAR",
    "Course",
    "Major"]

# Initially write the data columns to be recorded
def record_questions(questions, filename):
    with open(filename, "w") as file:
        for question in questions:
            file.write(f"{question} ")
        file.write("\n")
    return

def add_responses(questions, filename):
    with open(filename, "a") as file:
        for question in questions:
            response = input(f"What is your {question}? ")
            file.write(f"{response} ")
        file.write("\n")
    return
            
# Make another survey that saves responses into a csv, instead of a txt file



# Define your questions
questions = [
    "School",
    "Univeristy",
    "Age",
    "WAM",
    "ATAR",
    "Course",
    "Major"]

# Initially write the data columns to be recorded
def record_questions_csv(questions, data):
    with open(data, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(questions)
    return

def add_responses_csv(questions, data):
    with open(data, "a") as csvfile:
        writer = csv.writer(csvfile)
        responses = [input(f"{question}: ") for question in questions]
        writer.writerow(responses)        
    return

print("hello world")