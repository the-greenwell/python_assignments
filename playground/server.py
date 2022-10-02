from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/play/<int:x>')
def blue_box(x):
    return render_template("index.html", times=x)	

@app.route('/play/<int:x>/<string:color>')
def color_box(x,color):
    return render_template("index.html", color=color, times=x)	

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/play/5')

if __name__ == '__main__':
    app.run(debug=True)