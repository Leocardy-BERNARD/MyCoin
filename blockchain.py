from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.wallets = {}

        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block")
        self.chain.append(genesis)

        self.wallets = {
            "Alice": 100,
            "Bob": 50,
            "Charlie": 75
        }

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        dernier_bloc = self.get_last_block()

        nouveau_bloc = Block(
            len(self.chain),
            data,
            dernier_bloc.hash
        )

        self.chain.append(nouveau_bloc)

    def send_transaction(self, sender, receiver, amount):
        if sender not in self.wallets:
            return "Expéditeur inconnu"

        if receiver not in self.wallets:
            return "Destinataire inconnu"

        if sender == receiver:
            return "Impossible de s’envoyer de l’argent à soi-même"

        if amount <= 0:
            return "Montant invalide"

        if self.wallets[sender] < amount:
            return "Solde insuffisant"

        self.wallets[sender] -= amount
        self.wallets[receiver] += amount

        transaction = f"{sender} -> {receiver} : {amount} MyCoin"

        self.add_block(transaction)

        return None

    def create_wallet(self, username, balance):
        if username in self.wallets:
            return "Ce wallet existe déjà"

        if balance < 0:
            return "Solde invalide"

        self.wallets[username] = balance

        return None
    
    def is_valid(self):
        for i in range(1, len(self.chain)):
            bloc_actuel = self.chain[i]
            bloc_precedent = self.chain[i - 1]

            # Vérifie que le hash actuel est correct
            if bloc_actuel.hash != bloc_actuel.calculer_hash():
                return False

            # Vérifie le lien entre les blocs
            if bloc_actuel.prev_hash != bloc_precedent.hash:
                return False
        return True