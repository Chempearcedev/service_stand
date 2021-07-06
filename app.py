import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_jobs")
def get_jobs():
    jobs = list(mongo.db.jobs.find())
    return render_template("jobs.html", jobs=jobs)


@app.route("/search_bar", methods=["GET", "POST"])
def search_bar():
    querying = request.form.get("querying")
    jobs = list(mongo.db.jobs.find({"$text": {"$search": querying}}))
    return render_template("jobs.html", jobs=jobs)


@app.route("/userprofile/<username>", methods=["GET", "POST"])
def userprofile(username):
    if session["user"]:
        jobs = mongo.db.jobs.find({"created_by": username})
        username = mongo.db.user.find_one({
            "username": session["user"]})["username"]
        return render_template(
            "userprofile.html", username=username, jobs=jobs)
    return render_template("userprofile.html", username=username, jobs=jobs)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # does user exists
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("registration"))

        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.insert_one(registration)

        session["user"] = request.form.get("username").lower()
        flash("Your Registration Was Successful!")
        return redirect(url_for("userprofile", username=session["user"]))

    return render_template("registration.html")


# LOGIN FUNCTION


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking if the username already exists
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
         
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello there, {}".format
                        (request.form.get("username")))
                    return redirect(url_for
                        ("userprofile", username=session["user"]))
            else:

                flash("That's an incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("That's an incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/loggingout")
def loggingout():
    flash("You are logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/credentials.html", methods=["GET", "POST"])
def credentials():
    if request.method == "POST":
        credentials = {
            "image_url": request.form.get("image_url"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "profession": request.form.get("profession"),
            "available_now": request.form.get("available_now"),
            "available_date": request.form.get("available_date"),
            "telephone": request.form.get("telephone"),
            "skills": request.form.get("skills"),
            "locations": request.form.get("locations"),
            "created_by": session["user"]
        }
        mongo.db.jobs.insert_one(credentials)
        flash("Your Credentials Have Been Successfully Added")
        return redirect(url_for("get_jobs"))

    job = mongo.db.jobs.find().sort("first", 1)
    professions = mongo.db.professions.find().sort("profession_type", 1)
    return render_template(
    "credentials.html", job=job, professions=professions)


@app.route("/edit_jobs/<job_id>", methods=["GET", "POST"])
def edit_jobs(job_id):
    if request.method == "POST":
        submitting = {
            "image_url": request.form.get("image_url"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "profession": request.form.get("profession"),
            "available_now": request.form.get("available_now"),
            "available_date": request.form.get("available_date"),
            "telephone": request.form.get("telephone"),
            "skills": request.form.get("skills"),
            "locations": request.form.get("locations"),
            "created_by": session["user"]
        }
        mongo.db.jobs.update({"_id": ObjectId(job_id)}, submitting)
        flash("Your Credentials Have Been Successfully Updated")

    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    professions = mongo.db.professions.find().sort("profession_type", 1)
    return render_template("edit_jobs.html", job=job, professions=professions)


@app.route("/delete_job/<job_id>")
def delete_job(job_id):
    confirmation = input("Are you sure you want to delete your profile? Y/N")
    if confirmation.lower() == "y":
            mongo.db.jobs.remove({"_id": ObjectId(job_id)})
    flash("Profile Successfully Deleted")
    return redirect(url_for("get_jobs"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)