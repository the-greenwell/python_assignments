from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'soIgottaR1deWit0ne'

@app.route('/', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        session['increment'] = request.form['increment']

    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    times = 1
    if 'increment' in session:
        times = int(session['increment'])
    print(times, session['visits'])
    return render_template("index.html", visits=session['visits'], count=session['visits']*times, incremental=times)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)