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
## ASTUCE: opérateur d'incrémentation

print("créer y avec 5 et z avec la soustraction de x entre y")


## différentes façons d'afficher la valeur 7 !
## valeur litérale, variable, EXPRESSION


# %% ------------- fonctions globales entrée / sortie ----------------------
## input(invite): saisir un âge et un prénom à partir du clavier 
##        : et RETOURNER la valeur saisie
## voir la documentation def input(...) -> ...


## type(obj): voir le type de l'âge

#
# int(): conversion en entier
## REM: il y a une fonction de conversion pour chaque type de donnée 


## créer une variable user qui contient à la fois le prénom et l'âge


# %% ---------- jongler avec les expressions ---------------
## sasiur un entier au clavier et afficher la valeur ajoutée de 2
## on peut décomposer en plusieurs étapes


## ou en une seule ligne : mais c'est moins lisible et controlable


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


# %% ---------- MINI-EXO: opérateurs arithmétiques -------------------------
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)

# 2. convertir la sortie précédente en entier

# 3. décomposer ce nombre en nb en heure, minutes, secondes
# 4. affichier le résulat <nb_hour>h <nb_min>m <nb_sec>


# %% ------------------- même affichage mas en formatant mieux ---------------

## version 1 avec un template
# 02d: je veux 2 digits pour afficher l'entier, 
# et s'il n'ya qu'un chiffre, je rajoute un zéro à gauche
# padding avec des zéros

# tmp = "il est {}h {}m {}s"
# print(tmp.format(nb_hour, nb_min, nb_sec))

## version 2 avec f-string


# %%
