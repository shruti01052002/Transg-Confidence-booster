from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signup.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password1 = db.Column(db.String(200), nullable=False)
    password2 = db.Column(db.String(200), nullable=False)
    date_signup = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'User ' + str(self.id) + " " + self.username


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/csignup', methods=['GET', 'POST'])
def csignup():
    if request.method == 'GET':
        return render_template('csignup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_email = request.form['email']
        user_name = request.form['username']
        user_password1 = request.form['password1']
        user_password2 = request.form['password2']
        if user_password1 == user_password2:
            new_user = Users(email=user_email, username=user_name, password1=user_password1, password2=user_password2)
            db.session.add(new_user)
            db.session.commit()
            print(user_password1)
            print(user_password2)
            return redirect('/profile')
        else:
            return redirect('/signup')
    else:
        return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
