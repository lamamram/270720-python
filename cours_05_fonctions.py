# %% ---------- définition et appel d'une fonction -----------------------
## une fonction est un objet créé/définie avec: 
## le mot clé def suivi de <nom_de_la_fonction>(): 
##     et après un bloc d'instructions  
# f = function(){print("coucou")} en JS
# définition d'une fonction ma_fonction() qui contient l'affichage de "coucou"
def ma_fonction():
    print("coucou")

## pour exécuter le bloc de la définition, on doit appeler la fonction 
## <nom_de_la_fonction>()
## (): opérateur d'appel
## une fonction est un type de donnée dite "callable"

# afficher l'appel de la fonction ma_fonction
print("appel de ma_fonction() => ", ma_fonction())



# %% ----------- retour d'une fonction ------------------------------
## même définition mais en remplaçant le print("coucou") par le mot clé return et 'coucou'
def ma_fonction():
  return "coucou"

# afficher l'appel de la fonction
print("appel de ma_fonction() => ", ma_fonction())
# alternativement, on peut affecter l'appel de la fonction dans une variable
ret = ma_fonction()


# %% -- définition d'une fonction avec des paramètres et appel des paramètres ---
# définir une fonction qui ajoute 2 entiers en paramètres et qui retourne la somme 
# a, b dans la définition de la focntions sont des paramètres formels
def addition(a, b):
    return a + b

## injection des variables préexistante à la fonction (globales) en tant que paramètres d'appel: 
## passage en référence

# -------------------------------------------  a   b    a    b      a     b       a  b
# appliquer cette fonction avec des paramètres (3, 4), (3.5, 4.5), ("xx", "yy"), (2, "yy")  
print("addition(3, 4) => ", addition(3, 4))
print("addition(3.5, 4.5) => ", addition(3.5, 4.5))
print("addition('xx', 'yy') => ", addition("xx", "yy"))
# print("addition(2, 'yy') => ", addition(2, "yy")) # TypeError: unsupported operand type(s) for +: 'int' and '

x, y = 3, 4
print("addition(x, y) => ", addition(x, y)) # injection de variables global
a, b = 3.5, 4.5
print("addition(a, b) => ", addition(a, b)) # injection de variables global même nom que les paramètres formels: pourquoi pas ?

# %% ------------ annotations, documentation et contrôle -------------------
## créer une fonction division de 2 floats qui retourne un float
## 1. en notifiant les types d'entrée et de sortie de la fonction
## REM: les annotations ne sont pas des contrôles, ce ne sont que des indications
## 2. documenter la fonction en ajoutant une """doctstring""" au début du bloc
## 3. faire un contrôle sur le dénominateur
def division(a: float, b: float) -> float | str:
    """ retourne le résultat de la division de a par b
    a: float, le numérateur
    b: float, le dénominateur
    return: float, le résultat de la division
    """
    if b == 0:
        return "division par zéro impossible"
    return a / b

num = 3
denom = float(input("entrez le dénominateur: "))
print("division(num, denom) => ", division(num, denom))


# %% ------------------ portée globale et locale ------------
def func(param: int):
      print("param", param, id(param))
      x = 1
      print("x: local", x, id(x))
      x += param
      return x

x = 5
print("x: global avant appel", x, id(x))
x = func(x)
print("x: global après réaffectation", x, id(x)) # x global prend l'id du x local



# %% --------------- passage en référence de type immutables ------------------
def immutable(x: int):
      print("x: paramètre", x, id(x))
      x += 1
      print("x: local", x, id(x))
      return x

x = 5
print("x: global avant appel", x, id(x))
x = immutable(x)
print("x: global après réaffectation", x, id(x)) # x global prend l'id du x local



# %% --------------- passage en référence de type mutables ------------------
def mutable(l: list, elem: int):
      print("l: param", l, id(l))
      l.append(elem)
      print("l: param après chgt", l, id(l))

l = [1, 2, 3]
print("l global avant exec mutable()", l, id(l))
mutable(l, 4)
print("l global après exec mutable()",l, id(l)) # l global a changé car l est mutable => le l local



# %% --------------- types de paramètres ----------------------------------
## créer une fonction calcul_tva qui prend 2 paramètres le prix ht et le taux
## et retourne la valeur de tva sur ce prix et ce taux
## 1. annotations et documentation
## 2. le prix est arbitraire => paramètre positionnel / obligatoire
## MAIS on considère que la valeur par défaut du taux est 20 => paramètre nommé / optionnel

# ---param: positionnel / obligatoire,  nommé / optionnel



## appeler la fonction sans paramètres
## print(f"""appel positionnel: rien -> prix_ht, rien -> taux 
##        => {calcul_tva()} """) # TypeError
print(f"""appel positionnel: 199 -> prix_ht, 5.5 -> taux 
       => {"???"} """)
print(f"""appel avec un paramètre optionnel: 199 -> prix ht et rien -> taux
       => {"???"} """)
print(f"""appel nommé: les valeurs sont fléchées vers les paramètres 
       => pas besoin d'ordre => {"???"} """)



# %% ---------------- paramètres "variadiques" *args ---------------------
## *args: permet de définir un nombre variable de paramètres positionnels
## le bloc peut alors utiliser un tuple args

## exemple: print
## on veut afficher tous les mots soudés par "-" à partir de 2 prints
## et les 2 paramètres nommées "sep" et "end"

print("bonjour", "tout", "le", "monde")
print("comment", "allez", "vous")


## créer une fonction addition qui peut ajouter un nombre quelconque de params



# %% -------------- *args dans l'appel -------------
def ma_fonction(a, b, c):
    return a, b, c

l = [1, 2, 3]
## injecter les éléments de la liste l en tant que paramètres d'appel de ma_fonction



# %% paramètres "variadiques" **kwargs
## **kwargs: permet de définir un nombre variable de paramètres nommés
## le bloc peut alors utiliser un dict kwargs

## créer une fonction create_user avec
# 1. le prénom et le nom obligatoires
# 2. et un nombre quelconque de paramètres nommés/optionnels
# 3. pour créer et retourner un dictionnaire user 
#    avec les paramètres obligatoires et les autres s'ils existent (age, taille...)

# ---------------- positionnels, clé/valeur dans le dict options



# %% ------------ **kwargs dans l'appel -------------
def ma_fonction(a, b, c):
    return a, b, c

dico = {"a": 1, "b": 2, "c": 3}
## inejcter les valeurs du dict dico en tant que paramètres nommés d'appel de ma_fonction
print(ma_fonction(**dico))



# %% ----------------- programmation fonctionnelle et lambda: exemple map ---------------------
def to_upper(s: str):
    return s.upper()

fruits = ["pomme", "poire", "framboise"]

## j'injecte en premier paramètre l'objet fonction to_upper 
## NON PAS la valeur de retour to_upper(...)

## on a pas besoin de to_upper car on peut utiliser l'objet méthode de la classe str

## on peut aussi utiliser une fonction lambda,  lambda <variables,>: <expression>

## REM programmation fonctionnelle et + performante que les boucles for pour transformer une liste



# %% ----------------- programmation fonctionnelle et lambda: exemple filter ---------------------
fruits = ["pomme", "poire", "framboise"]
# fruits qui commencent par "p"

## filtrer la liste selon la valeur True d'une fonction en paramètre



# %% ----------------- programmation fonctionnelle et lambda: exemple sorted -------------
import random

# liste en intension
rows = [ f"row_{i}" for i in range(20)]
print(rows)
random.shuffle(rows)
print(rows)

## trier en python: sorted()
## le paramètre key permet de trier selon la valeur de retour d'une fonction
