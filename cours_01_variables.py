# %% ----------- affectation --------------------------
# "x <- 10 : on met 10 dans x")
# "1. on créé la variable x")
# "2. on place la valeur litérale 10 de type entier")
# "3. dans x")
## REM: = opérateur d'affection

x = 10

## REM en python on ne DECLARE par le type de la variable
## donc on peut changer la valeur de x avec une valeur d'un autre type de donées

x = "bonjour"

# supprimer une variable

del x


print(x) # NameError


# %% --------------- types built-in et politique de nommage -----------

age = 33 # entier              (type int)
taille = 1.75 # nombre flottant     (type float)
prenom = 'joe' # chaine de caractère (type str)
full_name = "john doe"# snake_case
PI = 3.14 # convention => CONSTANTE
lst = [1,"truc"] # liste               (type list): ensemble d'éléments ordonnables de types quelconque
tpl = (1,"truc") # tuple               (type tuple): // non modifiables 
dico = {"nom": "doe", 1: lst } # dictionnaire        (type dict): ensemble de paires clé: valeur
test = False # booléen             (type bool)
rien = None # rien                (type NoneType)

# %% --------------- manipulation des variables ------------------------------

x = 10

## incrémenter x: ajouter 1 à x et réaffecter x avec cet ajout
# évaluation de l'expression x + 1
# ensuite réaffection x = ...
x = x + 1
## ASTUCE: opérateur d'incrémentation
x += 1 # -= *= /=, ....
print("créer y avec 5 et z avec la soustraction de x entre y")

y = 5
z = y - x

## différentes façons d'afficher la valeur 7 !
## valeur litérale, variable, EXPRESSION
print(   7,         z,        y - x)

# %% ------------- fonctions globales entrée / sortie ----------------------
## input(invite): saisir un âge et un prénom à partir du clavier 
##        : et RETOURNER la valeur saisie
## voir la documentation def input(...) -> ...
age = input("saisir un âge: ")

## type(obj): voir le type de l'âge
print(type(age))
#
# int(): conversion en entier
## REM: il y a une fonction de conversion pour chaque type de donnée 
age = int(age)

## créer une variable user qui contient à la fois le prénom et l'âge
prenom = input("saisir un prénom: ")
user = {"prenom": prenom, "age": age}
print(user)

# %% ---------- jongler avec les expressions ---------------
## sasiur un entier au clavier et afficher la valeur ajoutée de 2
## on peut décomposer en plusieurs étapes

# nb = int(input("saisir un bombre: "))
# nb = float(nb)
# nb += 2
# print(nb)

## ou en une seule ligne : mais c'est moins lisible et controlable
print(float(input("saisir un entier: ")) + 2)

# %% ------------ unpacking ----------------------

x, y = 10, 5 # on peut affecter plusieurs variables en même temps
x, y = (10, 5) # on peut aussi affecter à partir d'un tuple => unpacking
tup  = (10, 5) # on affecte un tuple à une variable
x, y = tup # unpacking à partir d'une variable de type tuple 

## warning sur le unpacking
# v, w = 10, v - 1 # NameError: le v de droite n'est pas encore défini, on ne peut pas faire du unpacking avec des variables qui n'existent pas encore

v = 10

# v += 1
# w = v - 1 
v, w = v + 1, v - 1 # 2 affectations en même temps, et 2 affectations différents, n'ont pas le même résultat
print(v, w)

# %% --------------- identifiant unique d'une variable ----------------------
## REM. python est un langage haut niveau => on ne manipule pas directement la mémoire
## l'interpréteur gère l'allocation des variables avec un indentifiant unique (id)
x = 10
print(id(x))

# passage en référence: x et y sont 2 étiquettes qui pointent vers le même objet en mémoire
y = x

print(id(x), id(y), x is y)
z = 10
print(x is z)

y += 1
print(x is y, id(y))

# %% ---------- MINI-EXO: opérateurs arithmétiques -------------------------
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)
# 2. convertir la sortie précédente en entier
# moche car pas de contrôle de type
nb_sec = int(input("saisir un entier compris entre 0 et 86400: "))

# 3. décomposer ce nombre en nb en heure, minutes, secondes
nb_hr = nb_sec // 3600
nb_min = (nb_sec % 3600) // 60
# nb_sec = nb_sec % 60
nb_sec %= 60
# 4. afficher le résulat <nb_hour>h <nb_min>m <nb_sec>
print(nb_hr, "h", nb_min, "m", nb_sec, "s")

# %% ------------------- même affichage mas en formatant mieux ---------------

## version 1 avec un template
# 02d: je veux 2 digits pour afficher l'entier, 
# et s'il n'ya qu'un chiffre, je rajoute un zéro à gauche
# padding avec des zéros

# tmp = "il est {}h {}m {}s"
# print(tmp.format(nb_hour, nb_min, nb_sec))

## version 2 avec f-string
print(f"il est {nb_hr:02d}h, {nb_min:02d}m, {nb_sec:02d}s")

# %%
## attention avec la mémoire de la console ipython de jupyter !!

x = 10

# %%
x += 1
print(x)
# %%
