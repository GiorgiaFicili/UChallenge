from __future__ import print_function # In python 2.7

import flask_bcrypt
from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user

from __init__ import app, db
from form import StudentLoginForm, SchoolLoginForm, SchoolRegistrationForm, StudentRegistrationForm
from database import Students, Schools


@app.route('/')  # def layout():return render_template("layout.html") #
@app.route('/homepage')
def basic_homepage():  # put application's code here
    return render_template("basic_homepage.html")


@app.route('/reset_db')
def reset_db():
    db.drop_all()
    db.create_all()
    return render_template("basic_homepage.html")


@app.route('/student_registration', methods=['GET', 'POST'])
def student_registration():
    form = StudentRegistrationForm()

    if form.validate_on_submit():
        hashed_password = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_student = Students(username=str(form.username.data), name=str(form.name.data), surname=str(form.surname.data), email=str(form.email.data), password=str(hashed_password), degrees=str(form.degree.data))

        if form.duplicate_username():
            flash("Username already existent", "danger")
        else:
            flash("Congrats, the account has been created for {}! \n Login to start".format(form.name.data), 'success')
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for("student_login"))

    return render_template("student_registration.html", form=form)


@app.route('/school_registration', methods=['GET', 'POST'])
def school_registration():
    form = SchoolRegistrationForm()

    if form.validate_on_submit():
        hashed_password = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        string_degrees = ""
        string_districts = ""
        string_majors = ""
        for s in form.degrees.data:
            string_degrees += s+"-"
        for s in form.district.data:
            string_districts += s+"-"
        for s in form.majors.data:
            string_majors += s + "-"

        new_school = Schools(name=str(form.name.data), email=str(form.email.data), username=str(form.username.data),
                             password=str(hashed_password), district=str(string_districts), degrees=str(string_degrees),
                             majors=str(string_majors), address=str(form.address.data))

        if form.duplicate_username():
            flash("Username already existent", "danger")
        else:
            flash("Congrats, the account has been created for {}! \n Login to start".format(form.name.data), 'success')
            db.session.add(new_school)
            db.session.commit()
            return redirect(url_for("school_login"))

    return render_template("school_registration.html", form=form)


@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    form = StudentLoginForm()

    if form.validate_on_submit():

        s = form.existent_username()

        if s is not None:
            flash("Congrats, you logged!")
            login_user(s)
            session['user_type'] = 'student'
            return redirect(url_for('student_homepage'))
        else:
            flash("Inexistent account or wrong password", "danger")

    return render_template("student_login.html", form=form)


@app.route('/school_login', methods=['GET', 'POST'])
def school_login():
    form = SchoolLoginForm()

    if form.validate_on_submit():

        s = form.existent_username()

        if s is not None:
            flash("Congrats, you logged!")
            login_user(s)
            session['user_type'] = 'school'
            return redirect(url_for('school_homepage'))
        else:
            flash("Inexistent account or wrong password", "danger")

    return render_template("school_login.html", form=form)


@app.route('/school_homepage')
def school_homepage():
    return render_template("school_homepage.html")


@app.route('/student_homepage')
def student_homepage():
    return render_template("student_homepage.html")


@app.route('/layout')
def layout():
    return render_template("layout.html")


@app.route('/layout_homepages')
def layout_homepages():
    return render_template("layout_homepages.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('basic_homepage'))

@app.route('/school_profile')
def school_profile():
    return render_template("school_profile.html")


