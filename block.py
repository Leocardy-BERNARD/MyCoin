# block.py
import hashlib
import datetime


class Block:
    """Un bloc de la blockchain MyCoin."""

    def __init__(self, index, data, prev_hash="0000"):
        self.index     = index
        self.timestamp = str(datetime.datetime.now())
        self.data      = data
        self.prev_hash = prev_hash
        self.hash      = self.calculer_hash()

    def calculer_hash(self):
        """Calcule le hash SHA-256 du bloc."""
        contenu = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(contenu.encode()).hexdigest()

    def __repr__(self):
        return (
            f"--- Bloc #{self.index} ---\n"
            f"timestamp : {self.timestamp}\n"
            f"data      : {self.data}\n"
            f"prev_hash : {self.prev_hash}\n"
            f"hash      : {self.hash}\n"
        )


# Test rapide
if __name__ == "__main__":
    b0 = Block(0, "Genesis Block")
    b1 = Block(1, "Alice -> Bob : 10 MyCoin", b0.hash)
    b2 = Block(2, "Bob -> Charlie : 5 MyCoin", b1.hash)

    for b in [b0, b1, b2]:
        print(b)
