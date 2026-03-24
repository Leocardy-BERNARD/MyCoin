# main.py
from block import Block


def main():
    print("=" * 50)
    print(" Bienvenue sur MyCoin Ma Blockchain Python")
    print("=" * 50)
    print()

    # Création des blocs
    print("  Création de la blockchain")
    print()

    b0 = Block(0, "Genesis Block")
    b1 = Block(1, "Alice -> Bob : 10 MyCoin", b0.hash)
    b2 = Block(2, "Bob -> Charlie : 5 MyCoin", b1.hash)
    b3 = Block(3, "Charlie -> Alice : 2 MyCoin", b2.hash)

    blockchain = [b0, b1, b2, b3]

    # Affichage de la chaîne
    for bloc in blockchain:
        print(bloc)

    # Vérification de l'intégrité
    print("=" * 50)
    print(" Vérification de l'intégrité")
    print()

    valide = True
    for i in range(1, len(blockchain)):
        if blockchain[i].prev_hash != blockchain[i - 1].hash:
            print(f" Bloc #{i} corrompu !")
            valide = False

    if valide:
        print(" Blockchain valide.")
    print()
    print("=" * 50)


if __name__ == "__main__":
    main()
