import os
from flask import Flask, request, session, render_template, redirect
from app.models.orm import db
from app.models.models import Users

app = Flask(__name__, static_url_path="/static")
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost/db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.urandom(24)

db.init_app(app)
db.create_all(app=app)

@app.route('/')
def index():
    if session.get('user'):
        return redirect('/home')
    return render_template('title.html')

@app.route("/login", methods=["GET", "POST"])
def login():

    if session.get('user'):
        return redirect('/home')

    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                session["user"] = user.email_address
                return redirect('home')
            else:
                return "Login Failed"
        else:
            return "Login Failed"

@app.route("/register", methods=["GET", "POST"])
def signup():

    if session.get('user'):
        return redirect('/home')

    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")
        number = request.form.get("number")
        user = Users.query.filter_by(email_address=email).first()
        if user:
            return "Email already registered"
        elif Users.query.filter_by(username=username).first():
            return "Username already taken"
        elif Users.query.filter_by(number=number).first():
            return "Phone number already registered"
        else:
            user = Users(email_address=email, username=username, name=name, password=password, number=number)
            db.session.add(user)
            db.session.commit()
            return redirect('login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route("/home")
def home():
    if not session.get("user"):
        return redirect('login')
    else:
        return render_template("index.html")

@app.route("/events")
def events():
    if not session.get("user"):
        return redirect('login')
    else:
        return render_template("events.html")

@app.route("/gallery")
def gallery():
    if not session.get("user"):
        return redirect('login')
    else:
        return render_template("gallery.html")

@app.route("/payment")
def payment():
    if not session.get("user"):
        return redirect('login')
    else:
        return render_template("payment.html")


@app.route("/Student Information")
def list():
    if session.get("user"):
        # get all registered users from the database
        allusers = Users.query.all()
        #string = ''
        #for user in allusers:
        #    string += user.name + '\t' + user.email_address + '\n'
        return render_template("list.html", data=allusers)
    else:
        return redirect('login')
