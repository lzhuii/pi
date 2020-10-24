from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cmd", methods=['POST'])
def cmd():
    print("按下了按钮: "+request.values.get("cmd"))
    return "cmd"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
