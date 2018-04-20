from flask import Flask, render_template, request, redirect, session, url_for, escape
import json
from pprint import pprint

app = Flask(__name__)

database = json.load(open('database.json'))
pprint(database);

# go to localhost:5000
@app.route("/")
def index():
    # if the user is logged in
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    # if they are not logged in, redirect to login page
    return redirect(url_for('login'))

# go to localhost:5000/login
@app.route("/login", methods=['GET', 'POST'])
def login():
    # handle user login form submission
    if request.method == 'POST':
        # check if provided information matches a user
        for user in database['users']:
            if user['username'] == request.form['username'] and user['password'] == request.form['password']:
                # set the session variable
                session['username'] = request.form['username']
                # redirect to home page
                return redirect(url_for('index'))
        # if no user was found, login failed
        return "Login failed"

    # if user navigates to this page through the browser
    elif request.method =='GET':
        return render_template('login.html')


# go to localhost:5000/register
@app.route("/register", methods=['GET', 'POST'])
def register():
    # handle registration form submission
    if request.method == 'POST':
        # make sure passwords and confirm match
        if request.form['password'] != request.form['confirm']:
            return "Passwords do not match"
        # check to make sure no user has this username already
        for user in database['users']:
            if user['username'] == request.form['username']:
                return "Username already taken"
        # create and save the new user
        newUser = {
            'username': request.form['username'],
            'password': request.form['password']
        }
        database['users'].append(newUser)
        # save to file database.json
        with open('database.json', 'w') as outfile:
            json.dump(database, outfile)

        # set the session variable
        session['username'] = request.form['username']
        # redirect to home page
        return redirect(url_for('index'))

    # if user navigates to this page through the browser
    elif request.method == 'GET':
        return render_template('register.html')

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()
