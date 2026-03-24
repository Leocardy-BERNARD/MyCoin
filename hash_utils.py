# hash_utils.py
import hashlib


def calculer_hash(index, timestamp, data, prev_hash):
    #Calcule le hash SHA-256 d'un bloc.
    contenu = f"{index}{timestamp}{data}{prev_hash}"
    return hashlib.sha256(contenu.encode()).hexdigest()


# Test rapide
if __name__ == "__main__":
    h = calculer_hash(0, "2024-01-01", "Genesis", "0000")
    print(f" Hash généré : {h}")


