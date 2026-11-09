# run with: gunicorn 2_flaskhello:app
# or
# run with: flask --app 2_flaskhello run --debug


from flask import Flask, request, render_template, make_response
from markupsafe import escape

from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time")
def time():
    return f"<p>{dt.now()}</p>"


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"


@app.route("/nonono")
def badhello():
    name = request.args.get("name", "Flask")
    return f"Hello, {name}!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/pretty/')
@app.route('/pretty/<int:number>')
def prettynumber(number=None):
    return render_template('pretty.html', num=number)



@app.route('/favourite/<food>')
def favourite(food):
    food = escape(food)
    stored_food = request.cookies.get('food')
    if stored_food is None:
        resp = make_response(f'Welcome, your favourite food is {food}!')
        resp.set_cookie('food', food)
        return resp
    elif stored_food == food:
        return f"Hello! Your favourite food still is {food}."
    else:
        return f"Hello! Now your favourite food is {food}. But wasn't it {stored_food} last time?"



@app.route('/forget_food')
def forget():
    resp = make_response(f'Food cookie cleared')         
    resp.set_cookie('food', '', expires=0)
    return resp

