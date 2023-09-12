# importing flask
from flask import Flask, render_template, request, flash

# for the sql database
from flask_sqlalchemy import SQLAlchemy
# error handling for the database
from sqlalchemy.exc import IntegrityError

# for password incription
from werkzeug.security import generate_password_hash, check_password_hash

# import local file
from data import countries
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDetails.db'
db = SQLAlchemy(app)
app.secret_key = 'hewbW68q:5-5Ji2'

class DataBase(db.Model):
    # row id
    id = db.Column(db.Integer, primary_key=True)
    # name 1
    userName = db.Column(db.String(200), nullable=False, unique=True)
    # email 2
    email = db.Column(db.String(254), nullable=False, unique=True)
    # phone 3
    phoneNumber = db.Column(db.String(15), nullable=False)
    # address 4
    address = db.Column(db.String(500), nullable=False)
    #permanent Address 5
    permanentAddress = db.Column(db.String(500))
    # gender 6 
    gender = db.Column(db.String(10))
    # password 7
    password = db.Column(db.String(32), nullable=False)
    # extra activities 8
    eca = db.Column(db.JSON, nullable=True)
    # education details 9
    educationDetails = db.Column(db.String(2000))
    # father's name 10
    fatherName = db.Column(db.String(225), nullable=False)
    # monther's name 11
    motherName = db.Column(db.String(225), nullable=False)
    # fullName 12
    fullName = db.Column(db.String(225), nullable=False)
    # country 13
    country = db.Column(db.String(225))

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message=None
    if request.method == 'POST':
        # try:
            
        # except IntegrityError:
        #     db.session.rollback()
        #     error_message = "Try again with a different User Name, this one already exists"
        # try:
            
        # except IntegrityError:
        #     db.session.rollback()
        #     error_message = "Try again with a different Email, this one already exists"
        try:
            user = DataBase(    
                # name 1
                userName = request.form['userName'],
                # email 2
                email = request.form['email'],
                # phone 3
                phoneNumber = request.form['phoneNumber'],
                # address 4
                # address = request.form['address'],
                address = request.form.get('address', ''),
                # 5
                permanentAddress = request.form['permanentAddress'],
                # 6
                gender = request.form['gender'],
                # 7
                password = generate_password_hash(request.form['password'], method='sha256'),
                # 8
                eca = request.form['eca'],
                # 9
                educationDetails = request.form['educationDetails'],
                # 10
                fatherName = request.form['fatherName'],
                # 11
                motherName = request.form['motherName'],
                # 12
                fullName = request.form['fullName'],
                # 13
                country = request.form['country'],
            )
            print(user)
            db.session.add(user)
            db.session.commit()
            print('added to the database')
        except IntegrityError as e:
            db.session.rollback()
            error_info = str(e.orig)
            if 'userName' in error_info:
                flash("Try again with a different user name, this one already exists")
            elif 'email' in error_info:
                flash("Try again with a different email, this one already exists")


    return render_template('index.html', countries=countries, error_message=error_message)
    return render_template('index.html')

# def random():
#     request.

# @app.route('/read-from')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)