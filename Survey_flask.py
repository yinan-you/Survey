#Survey_csv
# Yinan You 3/12/2024
# Using flask

from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# Define your questions
questions = [
    "School",
    "Univeristy",
    "Age",
    "WAM",
    "ATAR",
    "Course",
    "Major"]

# Route for the survey form
@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Capture responses from the form
        responses = [request.form.get(q) for q in questions]
        
        # Save to CSV
        with open("survey_responses.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            # Check if the file is empty, then write headers
            if csvfile.tell() == 0:
                writer.writerow(questions)
            writer.writerow(responses)
        
        return "Thank you for participating!"
    
    # Display the form
    return render_template("survey.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)

