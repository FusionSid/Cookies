from flask import Flask, render_template, request, make_response, redirect
import time
from utils import *

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route('/account', methods= ["GET", "POST"])
def account():
    if request.method == "POST":
        resp = make_response(redirect("/"))
        resp.set_cookie('username', '', expires=0)
        resp.set_cookie('password', '', expires=0)

        
        return resp

    username = request.cookies.get('username')
    password = request.cookies.get('password')

    if username is None or password is None or username is None and password is None:
        return redirect('/login')
    else:
        return render_template("account.html", username=username)


@app.route("/login/", methods = ['POST', "GET"])
def login():
    user_name = request.cookies.get('username')
    pass_word = request.cookies.get('password')
    if user_name is not None and pass_word is not None:
        return redirect("/account")

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = get_account(username)
        if len(user) == 0:
            return render_template("login.html", text="Incorrect password/username")
        
        correct = False
        print(user)
        acutal_password = user[0][3]
        print(acutal_password)
        print(encrypt(password))
        if encrypt(password) == acutal_password:
            correct = True

        if correct:
            resp = redirect("/account")
            resp.set_cookie('username', username)
            resp.set_cookie('password', password)

            return resp
        else:
            return render_template("login.html", text="Incorrect password/username")    
    else:
        return render_template("login.html")


@app.route("/signup/",methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        text, check = "", True
        username = (request.form['username']).replace(" ", "")
        password = (request.form['password']).replace(" ", "")

        if len(username) == 0 or len(password) == 0:
            check = False
            text = "Input can't be none"

        if not check:
            return render_template("signup.html", text=text)
        
        if len(username) < 3 or len(password) < 8:
            check = False
            text = "Username must be more than or equal to 3 and password must be more than or equal to 8"

        if not check:
            return render_template("signup.html", text=text)

        if check:
            password = encrypt(password)
            if len(get_account(username)) != 0:
                return render_template("signup.html", text="Username already exists")
            
            acc = create_account(username, password)
            if acc == True:
                render_template("signup.html", text="Account Created!")
                time.sleep(2)
            else:
                return ("ERROR")

            resp = redirect("/account")
            resp.set_cookie('username', username)
            resp.set_cookie('password', password)
        
            return resp

        create_account(username, password)
    else:
        return render_template("signup.html")


app.run(host="0.0.0.0", port=80, debug=True)
