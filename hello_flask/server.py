from flask import Flask

app = Flask(__name__)


@app.route('/')
def first_route():
    return '<h1>This is home</h1>'

@app.route('/say_hi')
def hi_route():
    return '<h1>Hello User!</h1>'

if __name__ == '__main__':
    app.run(debug=True)