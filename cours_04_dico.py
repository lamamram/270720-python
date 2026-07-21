# %% ------------------- créer un dictionnaire: dict ----------------------

#       {         paire      , paire    }
#       { clé       : valeur , clé  : valeur}
user =  {"firstname": "roger", "age": 56}

## REM: les clés sont uniques et peuvent être n'importe quel type immutable
# créer un dict ayant 
# des clés de type tuple à 2 éléments qui représentent la latitude et la longitude
# et des valeurs qui sont les noms des villes liés à ces coordonnées 
points = {
    (48.856614, 2.3522219): "Paris",
    (43.604652, 1.444209): "Toulouse",
}

# %% -------------- accéder à la valeur d'une clé -------------
user =  {"firstname": "roger", "age": 56}

# afficher la valeur liée à la clé 'firstname'
user["firstname"]
# afficher le nom d'une ville liée à un point

points[(48.856614, 2.3522219)]

# %% --------- remplacer une valeur, créer une clé, ... --------
user =  {"firstname": "roger", "age": 56, "taille": 1.75}
# remplacer le prénom
user["firstname"] = "rogerio"
# ajouter un email
user["email"] = "me@example.com"
# supprimer age du dict
del user["age"]

# suprimer une clé du dict et récupérer sa valeur dans une variable
user.pop("email")
# afficher la taille de user si la clé existe dans user 

# if "taille" in user:
#     print(user["taille"])
# else:
#     print("N/A")

# ou afficher une valeur par défaut N/A
print(user.get("taille", "N/A"))
print(user.get("poids", "N/A"))

# %% ---------------- itérer sur un dictionnaire -----------------
user = {"firstname": "roger", "age": 56}

# tester si un dictionnaire est un itérable
for key in user:
    print(key)

# afficher la liste des clés
print(list(user))

print("-"*10 + "avec les valeurs" + "-"*10)
# afficher la liste des valeurs d'un dictionnaire
print(list(user.values()))

# itérer sur les valeurs d'un dictionnaire
for value in user.values():
    print(value)

print("-"*10 + "avec les items: clés & valeurs" + "-"*10)

# afficher la conversion d'un dictionnaire en une liste de tuples à 2 éléments
print(list(user.items()))

# itérer sur les clés & les valeurs d'un dictionnaire
for key, value in user.items():
    print(key, value)



# %% -- zip: recréer un dict à partir d'une liste de clés et une liste de valeurs --
user = {"firstname": "roger", "age": 56, "taille": 1.75}

# créer la liste des clés
keys = list(user)
# créer la liste des valeurs
values = list(user.values())


# "zipper" les 2 listes
z = zip(keys, values)
print(z)
# convertir cet "objet" en liste
print(list(z))

# warning: zip est un itérateur, une fois converti en liste, il ne peut plus être itéré
# recréer le zip et le convertir en dictionnaire
z = zip(keys, values)
print(dict(z))

 

# %% -------------- gestion des sets -----------------

fruits = {"pomme", "poire", "banane"}

# tester si les sets sont indexables
# fruits[0] # Error: 'set' object is not subscriptable

# tester si un élément est dans un set
print(f"coing dans {fruits}: { "coing" in fruits }")

# ajouter un élément à un set
fruits.add("coing")
print(f"maintenant coing dans {fruits}: { "coing" in fruits }")

# supprimer un élément d'un set + erreur si l'élément n'existe pas
fruits.remove("coing")
print(f"maintenant coing dans {fruits}: { "coing" in fruits }")

# supprimer un élément d'un set + ne fait rien
fruits.discard("ananas")
print(f"maintenant coing dans {fruits}: { "coing" in fruits }")

# tester si les sets sont itérables
for f in fruits:
    print(f)

# conversions entre set <-> list
fruits_list = list(fruits)

fruits_list.append("pomme")
print(f"liste de fruits: {fruits_list}")

fruits = set(fruits_list)
print(f"set de fruits: {fruits}")
### les sets dédoublonne naturellement les liste / tuples

# %%
