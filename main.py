from flask import Flask , request , render_template
import string 
import random
app = Flask(__name__,template_folder="templates")
possiblethings = [string.ascii_lowercase]
password = ""


@app.route("/",methods=["POST","GET"])
def getpass():
    global possiblethings
    global password
    password = ""
    possiblethings = [string.ascii_lowercase]
    if request.method == "POST":
        uppercase = request.form.get("uppercase")
        special = request.form.get("special")
        numbers = request.form.get("numbers")
        length = int(request.form.get("length"))
        if uppercase:
            possiblethings +=string.ascii_uppercase
        if special:
            possiblethings +=string.punctuation
        if numbers:
            possiblethings+=string.digits
        for i in range(length):
            password = password + random.choice(possiblethings)
        return render_template("index.html",password=password)
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)