from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = [
    
    {"question":"Capital of France?","options":["Paris","Rome","Berlin","Madrid"],"answer":"Paris"},
    {"question":"Largest ocean on Earth?","options":["Atlantic","Indian","Arctic","Pacific"],"answer":"Pacific"},
    {"question":"Who wrote 'Romeo and Juliet'?","options":["Shakespeare","Tolstoy","Hemingway","Dickens"],"answer":"Shakespeare"},
    {"question":"Smallest prime number?","options":["0","1","2","3"],"answer":"2"},
    {"question":"Fastest land animal?","options":["Cheetah","Lion","Tiger","Horse"],"answer":"Cheetah"},
    {"question":"The Great Wall is located in?","options":["China","India","Egypt","Mexico"],"answer":"China"},
    {"question":"Which planet is called the Red Planet?","options":["Mars","Venus","Jupiter","Saturn"],"answer":"Mars"},
    {"question":"Which country is famous for the Eiffel Tower?","options":["France","Italy","Spain","Germany"],"answer":"France"},
    {"question":"Currency of Japan?","options":["Yen","Dollar","Euro","Rupee"],"answer":"Yen"},
    {"question":"How many continents are there on Earth?","options":["5","6","7","8"],"answer":"7"},
    {"question":"Largest mammal?","options":["Elephant","Blue Whale","Giraffe","Hippopotamus"],"answer":"Blue Whale"},
    {"question":"Who painted the Mona Lisa?","options":["Leonardo da Vinci","Picasso","Van Gogh","Michelangelo"],"answer":"Leonardo da Vinci"},
    {"question":"Hottest planet in the solar system?","options":["Mercury","Venus","Mars","Jupiter"],"answer":"Venus"},
    {"question":"Which element has the chemical symbol 'O'?","options":["Oxygen","Gold","Silver","Iron"],"answer":"Oxygen"},
    {"question":"World’s longest river?","options":["Nile","Amazon","Yangtze","Mississippi"],"answer":"Nile"},
    {"question":"Who invented the telephone?","options":["Alexander Graham Bell","Thomas Edison","Nikola Tesla","Guglielmo Marconi"],"answer":"Alexander Graham Bell"},
    {"question":"Tallest mountain in the world?","options":["K2","Everest","Kangchenjunga","Lhotse"],"answer":"Everest"},
    {"question":"Which gas do plants absorb from the atmosphere?","options":["Oxygen","Carbon Dioxide","Nitrogen","Helium"],"answer":"Carbon Dioxide"},
    {"question":"Largest desert in the world?","options":["Sahara","Gobi","Kalahari","Antarctic Desert"],"answer":"Antarctic Desert"},
    {"question":"How many planets are in the Solar System?","options":["7","8","9","10"],"answer":"8"}
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