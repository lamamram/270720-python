# %% --------------------- créer un fichier ------------------------
## ".": dossier courant
## "..": dossier parent
## "~" : dossier utilisateur
## mode "w" : création si le fichier existe ET écrasement du contenu s'il existe
## attention souvent sous windows/Excell on peut avoir des fichiers encodés en iso-8859-1
f = open("./mon_fic.txt", mode="w", encoding="utf-8")
# creér (OUVRIR en mode création) le fichier "mon_fichier.txt" en encodage utf-8
f.write("1ère ligne\n")
f.write("2ème ligne\n")
# écriture de deux lignes avec les sauts de lignes

# important! il faut fermer ce qu'on a ouvert
f.close()


# %% ----------------- lire le contenu d'un fichier ---------------------
## ouvrir le fichier en lecture et même encodage
f = open("./mon_fic.txt", mode="r", encoding="utf-8")
# lire une ligne (avec \n)
print(f.read(11))

# lire tout
print(f.read())

## REM. notion de curseur: la deuxième lecture reprend 
## depuis la fin de la première ligne
f.close()


# %% ------------- écriture à la fin du fichier (append) -------------------
# écrire une 3ème ligne dans le fichier 
f = open("./mon_fic.txt", mode="a", encoding="utf-8")
# vérifier que le contenu existant n'a pas été supprimé
f.write("3ème ligne\n")

f.close()

# %% --------------------- readlines / writlelines --------------
f = open("./mon_fic.txt", mode="r", encoding="utf-8")
print(f.readlines())
f.close()

f = open("./mon_fic.txt", mode="w", encoding="utf-8")
f.writelines([
    "1ère ligne\n",
    "2ème ligne\n",
    "3ème ligne\n"
])
f.close()

# %% ------------------- modes avancés ------------------------------
# remplacer la ligne n
# r+: on a le curseur au début en lecture
#   : on peut replacer le curseur
f = open("./mon_fic.txt", mode="r+", encoding="utf-8")

# ce read est pour positionner le curseur à la fin
# print(f.read())
# f.write("4ème ligne\n")
# je remets le curseur au début
# f.seek(0)
# print(f.read())

### ATTENTION - seek se positionne sur un numéro d'OCTET, pas de numéro de CARACTERE
# avec utf-8 les caractère ASCII (de base) comme (a, 1, !, ?, ...) sont encodé sur 1 seul octet
# MAIS les caractères non ASCII comme (é, è, diacritique, idéogrammes ...) sont encodé avec 2 ou plus d'octet
f.seek(2)
f.read()
f.close()

# %% -- faciliter les ouvertures/fermetures: gestionnaires de contexte: with --

with open("./mon_fic.txt", mode="r", encoding="utf-8") as f:
    print(f.read())

f.read()

## with <ouverture>() as <var>:
  # fichier ouvert
  # ....



# ici fichier fermé



# %% ----------- un fichier est un itérable de lignes ----------------------

with open("./mon_fic.txt", mode="r", encoding="utf-8") as f:
    # for line in f:
    #     print(line)
    print(list(f))


# %% --------- suppression de la ligne n avec for ----------

n = 2


## je prends toutes les lignes du fichier sauf la ligne n

## et j'écrase le fichier avec les lignes restantes



# %% ---------------------- gérer des entêtes --------------------
lines = []

with open("./fichier.txt", mode="w", encoding="utf-8") as f:
    f.writelines([
        "name;age;size\n",
        "bob;33;1.75\n"
    ])

## utiliser la fonction next() pour faire une itération indivuelle des lignes de fihier
## pour récupérer la première ligne du fichier



# %% -----------------  création d'un csv -----------------------------
## importer le module standard csv de la bibliothèque standard

## données à écrire dans le csv: une liste de dictionnaires
users = [
  {"firstname":"Joe", "lastname": "Doe", "age": 22, "height": 1.75, "comment": "blablab ... ; blabliblo"},
  {"firstname": "Jane", "lastname": "Austen", "age": 34, "height": 1.79, "comment": "blabla"},
]

# 1. fabriquer le header

# 2. fabriquer les données: liste de listes à partir des valeurs des dictionnaires


# 3. ouvrir le fichier users.csv en création en utf-8 
# et utiliser un writer du module csv 
# pour écrire des ilgnes de csv avec le séparateur ";"



## REM avec windows la fin ligne est \r\n ...
# %% ------------------ idem mais avec le bon outil ------------------------------



# %% --------------- lire les lignes de csv ---------------
import csv

# idem mais en lecture
# protéger l'ouverture du fichier s'il le fichier existe
# tip: on peut itérer de façon manuelle un itérable avec la fonction next()
#    : pour récolter le header en première ligne



# %% ----------------------- écriture en JSON ----------------------
import json

# idem avec json 
# sachant que les objets et les dictionnaires python sont très proches
# méthodes pour écrire: json.dump et json.dumps
# écrire le json de façon comprimée ou dépliée (sep, indent)

users = [
  {"firstname":"Joe", "lastname": "Doe", "age": 22, "height": 1.75, "comment": "blablab ... ; blabliblo"},
  {"firstname": "Jane", "lastname": "Austen", "age": 34, "height": 1.79, "comment": "blabla"},
]



# %% --------------- lire un json ---------------------------
import json
# idem en lecture avec json.load ou json.loads




