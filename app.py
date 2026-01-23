from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
from utils.auth import validate_user
from utils.chatbot import get_bot_response

app = Flask(__name__)
app.secret_key = "dummy_bank_secret"

USERS_CSV = "data/users.csv"
CHAT_CSV = "data/chat_history.csv"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username, password):
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["username"])

@app.route("/chat", methods=["POST"])
def chat():
    if "username" not in session:
        return jsonify({"reply": "Please login again."})

    user_message = request.json["message"]
    bot_reply = get_bot_response(user_message)

    # Save chat to CSV
    chat_df = pd.DataFrame([
        {"username": session["username"], "message": user_message, "sender": "user"},
        {"username": session["username"], "message": bot_reply, "sender": "bot"}
    ])
    chat_df.to_csv(CHAT_CSV, mode="a", header=False, index=False)

    return jsonify({"reply": bot_reply})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
