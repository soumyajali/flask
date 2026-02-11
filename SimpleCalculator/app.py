from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        result = num1 + num2

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
