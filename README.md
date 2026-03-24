# 🪙 MyCoin — Blockchain fictive en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/Projet-Personnel-green)
![Status](https://img.shields.io/badge/Status-En%20développement-orange)

> Projet pédagogique : implémentation d'une blockchain simplifiée en Python pur.

---

## 📌 Description

MyCoin est une cryptomonnaie fictive développée from scratch en Python.  
L'objectif est de comprendre les mécanismes fondamentaux d'une blockchain :
hachage SHA-256, chaînage de blocs et vérification d'intégrité.

---

## 📁 Structure du projet
```
mycoin/
├── hash_utils.py   → Fonction de hachage SHA-256
├── block.py        → Classe Block (structure d'un bloc)
└── main.py         → Point d'entrée — création et validation de la chaîne
```

---

## ⚙️ Installation

**Prérequis :** Python 3.x installé sur ta machine.
```bash
# Cloner le dépôt
git clone https://github.com/Leocardy-BERNARD/MyCoin.git

# Se déplacer dans le dossier
cd MyCoin

# Lancer le projet
python main.py
```

---

## 🚀 Utilisation
```bash
python main.py
```

**Résultat attendu :**
```
==================================================
   Bienvenue sur MyCoin - Ma Blockchain Python
==================================================

--- Bloc #0 ---
timestamp : 2024-01-01 00:00:00
data      : Genesis Block
prev_hash : 0000
hash      : 3a7bd3e2...

✅ Blockchain valide — tous les blocs sont liés correctement.
```

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| Python 3.x  | Langage principal |
| hashlib     | Hachage SHA-256 |
| datetime    | Horodatage des blocs |

---

## 📈 Roadmap

- [x] Hachage SHA-256 (`hash_utils.py`)
- [x] Classe Block (`block.py`)
- [x] Vérification d'intégrité (`main.py`)
- [ ] Classe Blockchain complète
- [ ] Transactions et portefeuilles
- [ ] Proof of Work (minage)
- [ ] Interface web (HTML/CSS/PHP)

---

## 👨‍💻 Auteur

**Leocardy BERNARD**  
Étudiant BTS SIO — Projet personnel  
[![GitHub](https://img.shields.io/badge/GitHub-Leocardy--BERNARD-black?logo=github)](https://github.com/Leocardy-BERNARD)

---

## 📄 Licence

Projet open source — libre d'utilisation à des fins éducatives.
```

---

Une fois le fichier sauvegardé, envoie-le sur GitHub avec ces 3 commandes :
```
git add README.md
git commit -m "Ajout du README professionnel"
git push 