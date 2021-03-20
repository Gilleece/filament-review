import os
from flask import (
    Flask, flash, render_template, redirect,
     request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, loginForm
from extensions import csrf
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

csrf.init_app(app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/list_materials")
def list_materials():
    materials = mongo.db.materials.find()
    return render_template("materials.html", materials=materials)


@app.route("/register", methods=["GET", "POST"])
def register():
    name = None
    email = None
    password = None
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data.lower()
        email = form.email.data
        password = generate_password_hash(form.password.data)
        existing_user = mongo.db.users.find_one(
            {"username": name})

        if existing_user:
            flash("Username already taken :(")
            return redirect(url_for("register"))

        register = {
            "username": name,
            "email": email,
            "password": password,
            "admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = name
        flash("Thank you for signing up!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template(
        "register.html",
        form=form,
        name=name,
        email=email,
        password=password
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    name = None
    password = None
    form = loginForm()
    if form.validate_on_submit():
        name = form.name.data.lower()
        password = form.password.data
        # check if username exists in db
        existing_user = mongo.db.users.find_one({"username": name})

        if existing_user:
            # check password
            if check_password_hash(existing_user["password"], password):
                session["user"] = name
                flash("Sucessfully logged in!")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template(
        "login.html",
        form=form,
        name=name,
        password=password
    )


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/pla")
def pla():
    reviews = mongo.db.reviews.find()
    return render_template("materials/pla.html", reviews=reviews)


@app.route("/abs")
def abs():
    reviews = mongo.db.reviews.find()
    return render_template("materials/abs.html", reviews=reviews)


@app.route("/asa")
def asa():
    reviews = mongo.db.reviews.find()
    return render_template("materials/asa.html", reviews=reviews)


@app.route("/carbon")
def carbon():
    reviews = mongo.db.reviews.find()
    return render_template("materials/carbon.html", reviews=reviews)


@app.route("/hips")
def hips():
    reviews = mongo.db.reviews.find()
    return render_template("materials/hips.html", reviews=reviews)


@app.route("/metal")
def metal():
    reviews = mongo.db.reviews.find()
    return render_template("materials/metal.html", reviews=reviews)


@app.route("/nylon")
def nylon():
    reviews = mongo.db.reviews.find()
    return render_template("materials/nylon.html", reviews=reviews)


@app.route("/petg")
def petg():
    reviews = mongo.db.reviews.find()
    return render_template("materials/petg.html", reviews=reviews)


@app.route("/polycarbonate")
def polycarbonate():
    reviews = mongo.db.reviews.find()
    return render_template("materials/polycarbonate.html", reviews=reviews)

@app.route("/pva")
def pva():
    reviews = mongo.db.reviews.find()
    return render_template("materials/pva.html", reviews=reviews)


@app.route("/tpu")
def tpu():
    reviews = mongo.db.reviews.find()
    return render_template("materials/tpu.html", reviews=reviews)


@app.route("/wood")
def wood():
    reviews = mongo.db.reviews.find()
    return render_template("materials/wood.html", reviews=reviews)
    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Debug must be false on submission!