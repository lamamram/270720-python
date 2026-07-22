# %% ------------ import d'un module avec espace de nom ----------------
## un fichier d'extension .py avec du code python est un MODULE
## si ce module ne contient que des définitions de variables, fonctions, classes
##    ce module est une bibliothèque/librairie
## le module qui est exécuté directement par l'interpréteur python ou jupyter
##    est appelé module principal

# 1. créer un module bank qui contient la fonction du retrait

# 2. importer le module est exécuter la fonction dans le module principal
import bank

account = {"balance": 2000, "overdraft": 200}
amount = 100
# bank est une variable de type module qu'on appelle espace de nom du module
account = bank.withdraw(account, amount)
print(account)
print(bank.PI)


# %% -- à partir d'un module, importer une fonction => sans espace de nom ----
## idem sans espace de nom
# from bank import withdraw, PI
from bank import *

account = {"balance": 2000, "overdraft": 200}
amount = 100
account = withdraw(account, amount)
print(account)
print(PI)



# %% -- gérer les conflits de noms => alias
# idem en changeant le nom de la fonction à l'import
from bank import withdraw as retrait

# conflit de nom
withdraw = "qqch d'autre"
account = {"balance": 2000, "overdraft": 200}
amount = 100
account = retrait(account, amount)
print(account)



# %% --- exemples d'utilisation de modules de la bibliothèque standard ------
## exemple de datetime
## importer l'objet datetime à partir du module datetime

# créer une variable dt représente la date d'aujourd'hui avec la signature de base 

# idem avec une fonction interne

# idem  Parser un dt à partir de la str "2026-04-01 15:30" et le format "%Y-%m-%d %H:%M" 

# à partir de la variable dt, Formater "%d/%m/%Y"

# à partir de la variable dt, afficher le nb de secondes à partir le 1er janvier 1970

# afficher la durée entre la fin de la journée et maintenant, en heures, min, s

# date + duree (timedelta) = date



# %% ------------- import d'un module d'un package ------------------------
## créer un dossier app qui contient un modile utils.py qui contient la fonction parse_template()
## ici le "." on appelle çà le "chemin python": Python Path (comme "/" ou "\")
## un package est un dossier qui contient un ou des modules ou des sous packahes 
## et qui contient un fichier nommé __init__.py qui peut être vide
import app.utils

# raccourcir le chemin d'importation avec un alias


# à partir du module utils dans le package app, importer la fonction




# %% ------------ programme principal ------------------
import bank

print(f"Nom du module importé: {bank.__name__}")
print(f"Nom du module importé: {__name__}")
# le nom du module courant sera toujours __main__
# le nom d'un module importé sera toujouts le nom du fichier - l'extension

# 1. afficher le nom du programme principal: nom du module courant
# 2. afficher le nom d'un module importé
# 3. comment certifier qu'un code d'un module donné ne s'exécutera que si le module est principal
# cf => dans tools.py

# ici c'est une convention qui fait référence au int main(void){} en C
if __name__ == "__main__":
  bank.withdraw({"balance": 1000, "overdraft": 200}, 500)



