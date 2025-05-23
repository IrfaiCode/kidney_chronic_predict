from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("indexx.html")


if __name__ == "__main__":
    app.run(debug=True)
