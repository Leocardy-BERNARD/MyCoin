from flask import Flask, render_template, request
from block import Block

app = Flask(__name__)

blockchain = []

wallets = {
    "Alice": 100,
    "Bob": 50,
    "Charlie": 75
}

genesis = Block(0, "Genesis Block")
blockchain.append(genesis)


@app.route("/")
def home():
    return render_template(
        "index.html",
        blockchain=blockchain,
        wallets=wallets,
        error=None
    )


@app.route("/send", methods=["POST"])
def send_transaction():
    sender = request.form["sender"]
    receiver = request.form["receiver"]
    amount = int(request.form["amount"])

    if sender == receiver:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Impossible de s’envoyer de l’argent à soi-même"
    )
    if amount <= 0:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Montant invalide"
    )

    if sender not in wallets:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Expéditeur inconnu"
        )

    if receiver not in wallets:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Destinataire inconnu"
        )

    if wallets[sender] < amount:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Solde insuffisant"
        )

    wallets[sender] -= amount
    wallets[receiver] += amount

    transaction = f"{sender} -> {receiver} : {amount} MyCoin"

    dernier_bloc = blockchain[-1]

    nouveau_bloc = Block(
        len(blockchain),
        transaction,
        dernier_bloc.hash
    )

    blockchain.append(nouveau_bloc)

    return render_template(
        "index.html",
        blockchain=blockchain,
        wallets=wallets,
        error=None
    )

@app.route("/create_wallet", methods=["POST"])
def create_wallet():
    username = request.form["username"]
    balance = int(request.form["balance"])

    if username in wallets:
        return render_template(
            "index.html",
            blockchain=blockchain,
            wallets=wallets,
            error="Ce wallet existe déjà"
        )

    wallets[username] = balance

    return render_template(
        "index.html",
        blockchain=blockchain,
        wallets=wallets,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True)

