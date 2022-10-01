from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html", x=3)

@app.route('/play/<int:x>')
def multiplyBoxes(x):
    return render_template("index.html", x=x)

@app.route('/play/<int:x>/<color>')
def changeColor(x, color):
    return render_template("index.html", x=x, color=color)




if __name__=="__main__":
    app.run(debug=True)