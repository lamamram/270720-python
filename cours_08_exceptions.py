# %% ----------- gestion d'erreur avec une exception -------------------
## recréer la fonction division du cours des fonctions sans contôle

def division(a: float, b: float) -> float:
       """cette fonction retourne le résultat de la division de a par b"""
       return a / b

## REM: en peut entourer un bout de code entre 
## l'entête try: 
##      alors le bloc du try s'exécute jusqu'à qu'une erreur survienne
##      s'il n'ya pas d'erreur le bloc try s'exécute jusq'au bout
## ET l'entête except
##       s'il y a erreur, le bloc try s'interromp et exécute le bloc except
try:
    a, b = 5, 0
    ret = division(a, b)
except:
    print("pb")



# %% ---------- capturer les erreurs individuellement ------------------
def division(a: float, b: float) -> float:
    """cette fonction retourne le résultat de la division de a par b"""
    return a / b

# idem mais avec plusieurs pbs: 
#    ZeroDivisionError est traitée singulièrement
#    TypeError et KeyError sont traitées collectivement

## REM except: capture tout mais sans information sur le type de pb
## except <classe>: capture une erreur de sa classe 
## except (<classe1>, <classe2>) : capture la 1ère erreur liée au tuple de classes d'exception 
## except <classe> as e: //
##                       et injecte un objet exception e dans le bloc

try:
    # a, b = 5, 10
    a, b = 5, 0
    d = {"k": 1}
    d["j"]
    # a, b = 5, "truc"
    ret = division(a, b)
## traitements individuels d'erreurs particulières
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

## traitement collectif de certaines erreurs particulières
except (ZeroDivisionError, TypeError) as e:
     print(e)
# except Exception as e: # capture tout
#     print(e)

## ce bloc ne sera exécuté que s'il n'ya aucune exception déclenchée de le try
else:
    print(f"résultat final: {ret * 25/100}")
finally:
    print("on aura toujours ce message même en cas de plantage")


## TIP: quand on veut protéger un code donnée
# 1/ on commence en mettant Exception qui capture tout
# 2/ à l'usage, on voit les erreurs fréquentes et on individualise les traitements de erreurs
# 3/ si l'on voit des types d'erreurs qui seront gérées de la même façon, alors on peut les capturer en même temps



# %% ------------------ else, finally ------------------------------------




# %% --- lever une exception nous même quand on a un pb "métier" ---------

## 1. créer une liste de  notes de 0 -> 20 avec deux valeurs aberrantes -4 et 22
## 2. créer la fonction average qui calcule la moyenne
##    et calculer la moyenne de la liste de notes
## 3. utiliser le mot clé raise <classe>() qui génère une erreur si la note est aberrante
##    tip: trouver une erreur native de python de type XxxxxError
## 4. protéger le calcul de la moyenne des notes

notes = [12, 15, 18, 20, 10, -4, 22]

def average(notes: list) -> float:
    """cette fonction retourne la moyenne des notes"""
    errors = []
    for note in notes:
        # if note < 0 or note > 20:
        if not (0 <= note <= 20):
            errors.append(note)
    if errors:
        raise ValueError(f"notes aberrantes: {errors}")
    return sum(notes) / len(notes)

try:
    ret = average(notes)
except ValueError as e:
    print(e)



# %%
