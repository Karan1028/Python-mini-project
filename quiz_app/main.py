from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    score = 0
    submitted = False

    if request.method == "POST":
        submitted = True
        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")
            if selected == q["answer"]:
                score += 1

    return render_template("index.html", questions=questions, score=score if submitted else None, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)
