import os
from flask import (
    Flask, flash, render_template, redirect,
     request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, loginForm, ReviewForm, EditForm, SearchForm
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
###
# Show list of materials on index/materials page
###
def list_materials():
    materials = mongo.db.materials.find()
    return render_template("materials.html", materials=materials)


@app.route("/register", methods=["GET", "POST"])
###
# User registration functionality
###
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data.lower()
        email = form.email.data
        password = generate_password_hash(form.password.data)
        existing_user = mongo.db.users.find_one(
            {"username": name})

        # Check if username is taken
        if existing_user:
            flash("Username already taken :(")
            return redirect(url_for("register"))

        # Add account to mongoDB
        register = {
            "username": name,
            "email": email,
            "password": password,
            "admin": False
        }
        mongo.db.users.insert_one(register)

        # Put the new user into session cookie
        session["user"] = name
        flash("Thank you for signing up!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template(
        "register.html",
        form=form
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    ###
    # Log In functionality
    ###
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
        form=form
    )


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    ###
    # Add review functionality
    ###
    form = ReviewForm()
    if form.validate_on_submit():
        # Assign all parts of the form to variables
        material_name = form.material_name.data
        brand = form.brand.data
        filament_name = form.filament_name.data
        rating = int(form.rating.data)
        cost = int(form.cost.data)
        temp = form.temp.data
        finish = form.finish.data
        colour = form.colour.data
        review = form.review.data
        image = form.image.data
        # Add review to mongoDB
        review = {
            "material_name": material_name,
            "brand": brand,
            "filament_name": filament_name,
            "author": session["user"],
            "rating": rating,
            "temperature": temp,
            "finish": finish,
            "colour": colour,
            "review_text": review,
            "image_url": image,
            "cost": cost,
            "likes": 0
        }
        mongo.db.reviews.insert_one(review)
        flash("Thanks for your review!")
        return redirect(url_for("add_review"))

    return render_template(
        "add_review.html",
        form=form
    )


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    ###
    # Edit review functionality
    ###
    review_to_edit = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    # Pass the existing review through to populate the form
    form = EditForm(**review_to_edit)
    if request.method == 'POST':
        if form.validate_on_submit():
            # Assign all parts of the form to variables
            material_name = form.material_name.data
            brand = form.brand.data
            filament_name = form.filament_name.data
            rating = int(form.rating.data)
            cost = int(form.cost.data)
            temp = form.temperature.data
            finish = form.finish.data
            colour = form.colour.data
            review = form.review_text.data
            image = form.image_url.data

            # Add updated review to mongoDB
            updated_review = {
                "material_name": material_name,
                "brand": brand,
                "filament_name": filament_name,
                "author": session["user"],
                "rating": rating,
                "temperature": temp,
                "finish": finish,
                "colour": colour,
                "review_text": review,
                "image_url": image,
                "cost": cost,
                "likes": 0
            }
            mongo.db.reviews.update(
                {"_id": ObjectId(review_id)}, updated_review)
            flash("Review successfully updated.")
            return redirect(url_for(
                    "profile", username=session["user"]))

    return render_template(
        "edit_review.html",
        form=form,
        review_to_edit=review_to_edit
    )


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    ###
    # Delete reivew
    ###
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Sucessfully Deleted")
    return redirect(url_for(
                    "profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    ###
    # Grab the session user's username from db
    ###
    reviews = mongo.db.reviews.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    ###
    # Remove user from session cookies
    ###
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/admin_tools")
def admin_tools():
    return render_template("admin_tools.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    ###
    # Search functionality
    ###
    reviews = list(mongo.db.reviews.find({"$text": {"$search": ""}}))
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))

    return render_template(
        "search.html",
        form=form,
        reviews=reviews
        )


#################################################################
# Below are the app routes for each individual filament section #
#################################################################
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
######################################
# End of filament section app routes #
######################################


##################
# Error Handling #
##################
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
