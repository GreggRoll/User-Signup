from flask import Flask, request, redirect, render_template, flash, url_for
import cgi
import os

app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['DEBUG'] = True

@app.route('/')
def move_em_to_the_right_spot():
    return redirect ('/signup')

@app.route('/signup')
def index():
    return render_template('input.html')

@app.route('/signup', methods=['POST'])
def validate_form():

    username = request.form['username']
    username_error = ''

    password = request.form['password']
    password_error = ''

    verify_password = request.form['verify_password']
    verify_error = ''

    email = request.form['email']
    email_error = ''

    # if not username and not password and not verify_password:
    #     flash('put in some info!')
    #     return redirect(url_for('index'))
    
    # if username == password:
    #     flash('get serious please. normal people dont have a password that equals their username.')
    #     return redirect(url_for('index'))

    if username == '':
        username_error = "Enter a username!"
        username = ''
    elif ' ' in username or len(username) < 3 or len(username) > 20:
        username_error = "Username is not valid!"
        username = ''
     
    if password == '':
        password_error = "Enter a password!"
        password == ''
    elif ' ' in password or len(password) < 3 or len(password) > 20:
        password_error = "Password is not valid!"
        password = ''

    if verify_password == '':
        verify_error = "re-enter your password"
        verify_password = ''
    if not verify_error and password != verify_password:
        verify_error = "Passwords don't match"
        verify_password = ''

    if email and '@' and '.' not in email:
            email_error = "That's not a valid email"
            email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('input.html',
            username_error=username_error,
            password_error = password_error,
            verify_error = verify_error,
            email_error = email_error
        )


@app.route("/welcome", methods=['POST', 'GET'])
def valid_hello():
    user_name = request.args.get('username')
    return render_template('hello.html', name=user_name)
    
app.run()