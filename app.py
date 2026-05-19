from flask import Flask, render_template, request
from blockchain import Blockchain

app = Flask(__name__)

mycoin = Blockchain()


@app.route("/")
def home():
    return render_template(
        "index.html",
        blockchain=mycoin.chain,
        wallets=mycoin.wallets,
        error=None,
        valid=mycoin.is_valid()
    )


@app.route("/send", methods=["POST"])
def send_transaction():
    sender = request.form["sender"]
    receiver = request.form["receiver"]
    amount = int(request.form["amount"])

    error = mycoin.send_transaction(sender, receiver, amount)

    return render_template(
        "index.html",
        blockchain=mycoin.chain,
        wallets=mycoin.wallets,
        error=error,
        valid=mycoin.is_valid()
    )


@app.route("/create_wallet", methods=["POST"])
def create_wallet():
    username = request.form["username"]
    balance = int(request.form["balance"])

    error = mycoin.create_wallet(username, balance)

    return render_template(
        "index.html",
        blockchain=mycoin.chain,
        wallets=mycoin.wallets,
        error=error,
        valid=mycoin.is_valid()
    )


if __name__ == "__main__":
    app.run(debug=True)

