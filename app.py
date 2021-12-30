from flask import *
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vinay@0411"
)
cur = mydb.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("form.html")


@app.route("/user")
def user():
    


if __name__ == "__main__":
    app.run(debug=True)
