from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = [
    {"question":"Capital of India?","options":["Mumbai","Delhi","Chennai","Kolkata"],"answer":"Delhi"},
    {"question":"2 + 2 = ?","options":["3","4","5","6"],"answer":"4"},
    {"question":"Largest planet?","options":["Earth","Mars","Jupiter","Venus"],"answer":"Jupiter"},
    {"question":"HTML stands for?","options":["Hyper Text Markup Language","High Text Machine Language","Home Tool Markup Language","None"],"answer":"Hyper Text Markup Language"},
    {"question":"Python is?","options":["Snake","Programming Language","Game","Browser"],"answer":"Programming Language"},
    {"question":"CSS used for?","options":["Styling","Database","Server","Security"],"answer":"Styling"},
    {"question":"Sun is a?","options":["Planet","Star","Moon","Asteroid"],"answer":"Star"},
    {"question":"Water formula?","options":["H2O","CO2","O2","NaCl"],"answer":"H2O"},
    {"question":"CPU full form?","options":["Central Processing Unit","Computer Power Unit","Central Program Unit","None"],"answer":"Central Processing Unit"},
    {"question":"JS stands for?","options":["Java Style","JavaScript","Just Script","None"],"answer":"JavaScript"}
]

@app.route("/")
def quiz():
    random.shuffle(questions)
    return render_template("quiz.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    for i,q in enumerate(questions):
        ans = request.form.get(f"q{i}")
        if ans == q["answer"]:
            score += 1
    return render_template("result.html", score=score, total=len(questions))

# ------------- RENDER READY -----------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)