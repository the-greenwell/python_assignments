from curses.ascii import isdigit
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'soIgottaR1deWit0ne'

@app.route('/', methods=['GET'])
def counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    if 'increment' not in session:
        session['increment'] = 1
    return render_template("index.html")

@app.route('/', methods=['POST'])
def post_increment():
    if request.form['increment'].isdigit():
        session['increment'] = int(request.form['increment'])
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)