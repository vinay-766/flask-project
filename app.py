from flask import *
import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="admin_detail")
cur = myconn.cursor()

app = Flask(__name__)
app.secret_key = "vinay"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    msg = ""
    return render_template("form.html", msg=msg)


@app.route("/user", methods=["POST"])
def userpage():
    session["username"] = request.form['Username']
    session["password"] = request.form['Password']

    cur.execute("select * from admin_login where Username = %s and Password = %s", (session["username"], session["password"]))
    rows = cur.fetchall()
    if len(rows) == 1:
        return render_template("profile.html", name=session["username"])
    else:
        msg = "you are not resister as admin user, please resister first."
        return render_template("form.html", msg=msg)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop("username", None)
        return render_template("logout.html")
    else:
        return render_template("logout.html")


@app.route("/resister")
def resister():
    return render_template("resister.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    username = request.form["Username"]
    password = request.form["Password"]
    cur.execute("insert into admin_login(Username, Password) values(%s,%s)", (username, password))
    return render_template("message.html")


if __name__ == "__main__":
    app.run(debug=True)
