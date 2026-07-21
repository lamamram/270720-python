# %%
"""
1/ saisir n valeurs entiers relatifs au le clavier séparées par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
que ces valeurs sont des entiers relatifs (1er cas entier naturel => une str qui ne contient que des caractères numérique, ensuite 2ème cas négatif)
Hint: pour vérifier une valeur : regarder les valeurs internes de la valeur en question
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 décimales.  (pas de formatage ==> vrai arrondi)
"""

# %% --------------------- solution n°1 ------------------------
saisie = input('saisir n valeurs entiers relatifs au le clavier séparées par ","')
valeurs = saisie.split(",")

# ex = "-56"
# print(ex.isnumeric())
integers = []
for valeur in valeurs:
    ## strip: dégage les espaces à gauche et à droite
    valeur  = valeur.strip()
    # ---- cas positif --- OU ----- cas négatif: commence avec "-" ET le reste est numérique
#    if valeur.isnumeric() or (valeur[0] == "-" and valeur[1:].isnumeric()):
                             # startswith est faux si la str est vide
                             # si valeur == "-" alors la slice en dehors de l'intervalle de la valeur ne plante pas mais est faux: valeur[1:]
    if valeur.isnumeric() or (valeur.startswith("-") and valeur[1:].isnumeric()):
        integers.append(int(valeur))

## moyenne arithmétique: somme (des éléments) / le nb d'éléments
if len(integers):
    average = sum(integers) / len(integers)
    print(f"moyenne de {integers}: { round(average, 2) }")

# %% ------------------------- solution n°2 avec break et else -----------------
## on sort dès la première erreur rencontrée, on ne veut pas voir toutes les erreurs
saisie = input('saisir n valeurs entiers relatifs au le clavier séparées par ","')
valeurs = saisie.split(",")

integers = []
for valeur in valeurs:
    valeur  = valeur.strip()
    if valeur.isnumeric() or (valeur.startswith("-") and valeur[1:].isnumeric()):
        integers.append(int(valeur))
    else:
        print(f"{valeur} non convertible en int !")
        break
else:
    if len(integers):
        average = sum(integers) / len(integers)
        print(f"moyenne de {integers}: { round(average, 2) }")


# %% ----------- solution n°3: on veut voir toutes les erreurs ------------



# %%
