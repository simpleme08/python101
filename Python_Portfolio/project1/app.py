from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    message = request.form.get("message")
    database.save_message(message)
    return "Saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)
