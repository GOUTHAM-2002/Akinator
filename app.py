import akinator
from flask import Flask,render_template,request

app=Flask(__name__)
aki = akinator.Akinator()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start",methods=["POST","GET"])
def start():
    if request.form.get("character_name") and aki.progression <=80:
            user_input=request.form.get("character_name")
            q = aki.answer(user_input)
            return render_template("question.html", q=q)
    elif aki.progression == None:
        q = aki.start_game()
        return render_template("question.html",q=q)
    else:
        aki.win()
        x=aki.first_guess['name']
        return render_template("win.html",name=x,des=aki.first_guess['description'])











