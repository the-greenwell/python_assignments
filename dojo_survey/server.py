from flask import Flask, render_template, redirect, request, url_for, session


app = Flask(__name__)
app.secret_key = 'soIgottaR1deWit0ne'

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        session['form'] = request.form
        session['food_pref'] = request.form.getlist('food_pref')
        print(request.form)
        return redirect('/result')
    return render_template("index.html")

@app.route('/result')
def handle_form():
    if 'form' not in session:
        return redirect('/')
    return render_template('user.html', form_data=session['form'], food_data=session['food_pref'])

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)