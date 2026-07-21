# %% ------------------ structure conditionnelle : le if ----------------------
balance = 1000
overdraft = 200

amount = input("Entrez un montant : ")
amount = int(amount)

if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
elif amount >= balance + overdraft:
    print(f"Transaction refusée: {amount} fonds insuffisants")
else:
    balance -= amount
    print(f"retrait accepté: solde: {amount}")

# si le montant est négatif => afficher "Transaction refusée: {montant} négatif"
# sinon mais si le montant trop important => "Transaction refusée: {montant} fonds insuffisants" 
# sinon => le retrait est effectué et "Transaction acceptée"

## idem avec la logique inverse !!
# if amount >= 0:
#     if amount <= balance + overdraft:
#         balance -= amount
#         print(f"retrait accepté: solde: {amount}")
#     else:
#         print(f"Transaction refusée: {amount} fonds insuffisants")
# else:
#     print(f"Transaction refusée: {amount} négatif")

# avec opérateur logique
# if amount >= 0 and amount <= balance + overdraft:
#     balance -= amount
#     print(f"retrait accepté: solde: {amount}")
# elif amount < 0:
#     print(f"Transaction refusée: {amount} négatif")
# else:
#     print(f"Transaction refusée: {amount} fonds insuffisants")


# %% ----------------- opérateur ternaire ---------------------------------
reponse = input("2+2 ?")
message = ""

# si la réponse est 4 => message vaut "bingo"
# sinon               => message vaut "perdu"


# version sur une seule phrase

print(message)



# %% ---------------- opérateurs comparaison et logique ------------------
## prendre un int. savoir si l'entier est négatif ou nul
x = int(input("saisir un entier: "))


## savoir çà ET si c'est impair (idem en remplaçant ET par OU)



# %% --------------- valeur fausses des built-ins et négation --------------
## prendre un str et la convertir en bool
# x = input("saisir une str: ")
# x = 0
x = []

# idem avec une str vide 
print(bool(x))

# savoir si une str n'est pas vide
if x:
    print(f"{x} a une valeur non vide")

# idem si elle est vide
if not x:
    print(f"{x} a une valeur vide")



# %% -------------------------- boucle for -----------------------------------
## REM: le for classique en informatique c'est: for(initialisaton; condition d'arrêt; changement)
## MAIS pour boucler en python avec le for, on DOIT itérer/consommer un ITERABLE
## ITERABLE == n'importe quelle variable qu'on peut mettre dans un for

mots = ["appeler", "un", "chat"]
# pour mot dans mots: 
#     afficher mot


print("-"*20)

nom_complet = "John DOE"
# pour lettre dans nom_complet:
#    afficher lettre 



# %% --------- générer une "série d'entiers" avec range() -------------------------
# pour i dans une range de 5 entiers depuis 0: afficher i

print("-"*20)

# pour i dans une range entre 2 et 5: afficher i

print("-"*20)

# pour i dans une range de 5 jusqu'à 0: afficher i

# %% ---------- transformation de liste en préservant la liste d'origine ------

fruits = ["pomme", "poire", "framboise"]

# afficher une liste des fruits en majuscule sans modifier fruits


# %% ----------- idem en modifiant directement de la liste d'origine --------
fruits = ["pomme", "poire", "framboise"]

# %% -------------- idem avec la fonction - enumerate() -------------------
fruits = ["pomme", "poire", "framboise"]

## enumerate transforme la liste en liste de tuple (index, valeur)
## itérer à la fois avec les indices et les valeurs dans la boucle



# %% --- interrompre l'exécution d'une boucle : break, continue, else ---
## prendre une range 5 pour afficher i et on s'arrête à 3
print("-"*10 + "break" + "-"*10)

## prendre une range 5 pour afficher i, sans afficher 3
print("-"*10 + "continue" + "-"*10)

## saisir j par le clavier. prendre une range 5 pour afficher i
## dans la boucle, casser la boucle si i==j
## en sortant de la boucle, tester si la boucle est sortie à cause du break ou non 
print("-"*10 + "else après for" + "-"*10)



# %% boucle while : tant qu'une condition est vraie: le bloc est exécutée
temp = int(input("saisir une temperature en °C: "))

# tant que la temp est sous 100°C: 
#     on roule donc on perd 10°C
#     afficher la temp
#     si la temp est sous 25°C:
#         on remet une pelettée de charbon dans la cheminée
#         donc on resaisit temp à partir du clavier
# afficher boom quand on sort de la boucle



# %% --------------- boucle infinie: condition toujours vraie --------------------------
## idem avec une boucle infinie
temp = int(input("saisir une temperature en °C: "))
