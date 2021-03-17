import os
from flask import (
    Flask, flash, render_template, redirect,
     request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm
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
    return render_template(
        "register.html",
        form=form,
        name=name,
        email=email,
        password=password
    )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Debug must be false on submission!


#    if request.method == "POST":
#        existing_user = mongo.db.users.find_one(
#            {"username": request.form.get("username").lower()})
#
#        if existing_user:
#            flash("Username already taken :(")
#            return redirect(url_for("register"))
#
#        register = {
#            "username": request.form.get("username").lower(),
#            "email": request.form.get("email"),
#            "password": generate_password_hash(request.form.get("password")),
#            "admin": False
#        }
#        mongo.db.users.insert_one(register)
#
#        # put the new user into session cookie
#        session["user"] = request.form.get("username").lower()
#        flash("Thank you for signing up!")
#    return render_template("register.html")