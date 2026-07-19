# %% ------------------- créer un dictionnaire: dict ----------------------

#       {         paire      , paire    }
#       { clé       : valeur , clé  : valeur}
user =  {"firstname": "roger", "age": 56}

## REM: les clés sont uniques et peuvent être n'importe quel type immutable
# créer un dict ayant 
# des clés de type tuple à 2 éléments qui représentent la latitude et la longitude
# et des valeurs qui sont les noms des villes liés à ces coordonnées 



# %% -------------- accéder à la valeur d'une clé -------------
user =  {"firstname": "roger", "age": 56}

# afficher la valeur liée à la clé 'firstname'

# afficher le nom d'une ville liée à un point



# %% --------- remplacer une valeur, créer une clé, ... --------
user =  {"firstname": "roger", "age": 56, "taille": 1.75}
# remplacer le prénom

# ajouter un email

# supprimer age du dict

# suprimer une clé du dict et récupérer sa valeur dans une variable

# afficher la taille de user si la clé existe dans user 

# ou afficher une valeur par défaut N/A



# %% ---------------- itérer sur un dictionnaire -----------------
user = {"firstname": "roger", "age": 56}

# tester si un dictionnaire est un itérable

# afficher la liste des clés

print("-"*10 + "avec les valeurs" + "-"*10)
# afficher la liste des valeurs d'un dictionnaire

# itérer sur les valeurs d'un dictionnaire

print("-"*10 + "avec les items: clés & valeurs" + "-"*10)

# afficher la conversion d'un dictionnaire en une liste de tuples à 2 éléments

# itérer sur les clés & les valeurs d'un dictionnaire



# %% -- zip: recréer un dict à partir d'une liste de clés et une liste de valeurs --
user = {"firstname": "roger", "age": 56, "taille": 1.75}

# créer la liste des clés

# créer la liste des valeurs

# "zipper" les 2 listes

# convertir cet "objet" en liste


# warning: zip est un itérateur, une fois converti en liste, il ne peut plus être itéré
# recréer le zip et le convertir en dictionnaire


 

# %% -------------- gestion des sets -----------------

fruits = {"pomme", "poire", "banane"}

# tester si les sets sont indexables

# tester si un élément est dans un set

# ajouter un élément à un set

# supprimer un élément d'un set + erreur si l'élément n'existe pas

# supprimer un élément d'un set + ne fait rien
# fruits.remove("ananas")

# tester si les sets sont itérables

# conversions entre set <-> list

### les sets dédoublonne naturellement les liste / tuples

# %%
