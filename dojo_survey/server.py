from flask import Flask, render_template, redirect, request, url_for, session


app = Flask(__name__)
app.secret_key = 'soIgottaR1deWit0ne'

@app.route('/', methods=['GET'])
def root():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def post_form():
    session['form'] = request.form
    session['food_pref'] = request.form.getlist('food_pref')
    return redirect('/result')

@app.route('/result')
def render_form():
    if 'form' not in session:
        return redirect('/')
    return render_template('user.html')

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)