from database import Database
from user import User
from flask import Flask,render_template,request, session
from fitness import Fitness
import send_mail

app=Flask(__name__)
app.secret_key="ash007"


@app.route('/')
def login_template():
    return render_template('login.html')

@app.route('/reset_password')
def reset_password():
    return render_template('reset.html')

@app.route('/validate', methods=['POST'])
def validate_user():
    email = request.form['email']
    print(email)
    if User.check_email(email):
        print("verified")
        code=send_mail.update_pass(email)
        session['code']=code
        return render_template('verification.html')
    else:
        return render_template('reset.html',message="a")

@app.route('/verify', methods=['POST'])
def verify():
    number = request.form['verification_number']
    if number==session['code']:
        return render_template('reset_password.html')
    else:
        return render_template('reset.html',message="a")   

@app.route('/update_password', methods=['POST'])  
def update_password():
    new_password1=request.form['password1']
    new_password2=request.form['password2']
    if new_password1==new_password2:
        User.update_password(new_password1)
        return render_template('login.html')
    else:
        return render_template('reset_password.html',message="a")   

@app.route('/register')
def register_template():
    return render_template('sign_up.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
        return render_template("home-page.html", name=session['name'])
    else:
        return render_template("login.html",message="a")
    

@app.route('/register/new_user', methods=['POST'])
def register_user():
    name = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender']
    email = request.form['email']
    password1 = request.form['password1']
    password2= request.form['password2']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    if password1==password2:
        password=password1
        if send_mail.check(email) is True:
            if User.register(name,age,gender,height,weight,email,password) is True:
                return(render_template("home-page.html", name=session['name']))
            else:
                return render_template('sign_up.html', message="a")
        else:
            return render_template('sign_up.html', message="a")
    else:
        return render_template('sign_up.html', message="a")

@app.route('/login/homepage', methods=['GET'])
def home_page():
    return(render_template("home-page.html", name=session['name']))

@app.route('/login/diet', methods=['GET'])
def diet():
    return(render_template("diet.html", name=session['name']))

@app.route('/login/exercise', methods=['GET'])
def fitness():
    return(render_template("exercise.html", name=session['name']))

@app.route('/login/profile', methods=['GET'])
def profile():   
    return(render_template("profile.html", name=session['name'],bmi=session['bmi'],calories=round(session['calories'],2),
    email=session['email'],age=session['age'],suggestion=Fitness.suggest_bmi(session['bmi']),breakfast=session['breakfast'],
    lunch=session['lunch'],snacks=session['snacks'],dinner=session['dinner'],suggestion1=Fitness.suggest_calories_breakfast(
    session['breakfast'],session['bmi']),suggestion2=Fitness.suggest_calories_lunch(session['lunch'],
    session['bmi']),suggestion3=Fitness.suggest_calories_dinner(session['dinner'],session['bmi'])))

@app.route('/login/help', methods=['GET'])
def help():   
    return(render_template("help.html", name=session['name']))

@app.route('/login/diet/update', methods=['POST'])
def update_calories_intake():
    calories = float(request.form['calories'])
    quantity = int(request.form['quantity'])
    User.add_calories(calories*quantity)
    return(render_template("diet.html", name=session['name'],message="a"))

@app.route('/login/exercise/update', methods=['POST'])
def update_calories_burnt():
    activity = request.form['activity']
    duration = float(request.form['duration'])
    User.subtract_calories(activity,duration)
    return(render_template("exercise.html", name=session['name'],message="a")) 

@app.route('/update/user-details', methods=['GET'])
def update_user_details():   
    return(render_template("update_user.html", name=session['name']))

@app.route('/update/user_details/input', methods=['POST'])
def update_height_weight():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    User.update_user_details(height,weight)
    return(render_template("help.html", name=session['name'],message="a")) 

@app.route('/logout', methods=['GET'])
def logout():
    User.logout()
    return render_template('login.html')