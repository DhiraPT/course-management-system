from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html')


'''@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))'''


if __name__ == "__main__":
    app.run(debug=True)

