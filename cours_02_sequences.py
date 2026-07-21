#################### séquence: str, list, tuple ############################
# %% ---------- chaines de caractères: str: concaténation ---------------

prenom = "john"
nom = "doe"

# afficher nom complet: "john doe"
nom_complet = prenom + " " + nom
print(nom_complet)

# %% ---------- chaines de caractères: pas de conversion implicite en python ---------------

nb = 2

# print(nb + " inséparables") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(nb) + " inséparables") # conversion explicite
# %% ---------- fonctions internes d'une variable selon son type : ici str ----

######### forme type <variable>.<fonction>()

prenom = "john"
nom = "doe"

# afficher le nom complet : John DOE
nom_complet = prenom.capitalize() + " " + nom.upper()
print(nom_complet)

# %% ------------ indéxer une séquence ------------------------------------
nom_complet = "Joe DOE"

# prendre la longueur d'une str
length = len(nom_complet)

######## <variable>[n]: caractère de la variable à la position n 
# afficher le 1er caractère de la str, le 1er car. du 2ème mot, le dernier car.
print(f"1er car. de la str: {nom_complet[0]}")
print(f"1er car. du 2ème mot: {nom_complet[4]}")
print(f"dernier car. de la str à partir de 0: {nom_complet[length-1]}")
print(f"dernier car. de la str à partir de la fin: {nom_complet[-1]}")

# %% ------------- SLICING d'une séquence ----------------------------------- 

civilite_nom_complet = "Mr. Joe DOE"

######## slicing : <variable>[<index de début compris>:<index de fin non compris>]
######## slicing avec pas: <var>[deb:fin:pas]
# afficher la civilité, le prénom, le nom à partir de civilite_nom_complet
civilite = civilite_nom_complet[0:3]
prenom = civilite_nom_complet[4:7]
nom = civilite_nom_complet[8:11]

# si début => 0 ou rien, fin => rien longueur -1 ou compter depuis la fin ...
civilite = civilite_nom_complet[:3]
nom = civilite_nom_complet[8:]

# afficher une chaine contenant chaque 1er car. de chaque mot //
lettres_with_4step = civilite_nom_complet[::4]

# retourner civilite_nom_complet
redrum = civilite_nom_complet[::-1]


# %% -------------- retourner l'indice d'une str ---------------------------

civilite_nom_complet = "Mr. Joe DOE"

index_J = civilite_nom_complet.index("J")
index_D = civilite_nom_complet.index("D")

# afficher la civilité, le prénom, le nom à partir des indices de J et D
civilite = civilite_nom_complet[:index_J-1]
prenom = civilite_nom_complet[index_J:index_D-1]
nom = civilite_nom_complet[index_D:]

# même chose mais en remettant les valeurs slicées en minuscules
      #<--------  str ------------->: donc on peut utiliser lower() sur le résultat du slicing
nom = civilite_nom_complet[index_D:].lower()
      #<--------  str ---------- >: donc on peut utiliser [] sur le résultat en minuscules
nom = civilite_nom_complet.lower()[index_D:]

# %% -------------- list: indexation, concaténation, slicing -------------

mots = ["appeler", "un", "chat"]

# afficher chat à partir de mots
print(mots[2])

# modifier mots en concaténant ["il", "faut"] , mots et ["un", "chat"]
mots = ["il", "faut"] + mots + ["un", "chat"]

# remettre mots dans sa valeur initiale à partir de sa valeur courante
print(mots[2:5])

# %% -------------- transformation de liste <=> chaîne de caractères ----------

civilite_nom_complet = "Mr. Joe DOE"

# créer la liste mots, des mots de civilite_nom_complet => split
mots = civilite_nom_complet.split()
print(f"liste de mots: {mots}")
# recréer civilite_nom_complet à partir de mots
# une valeur litérale de type str a des fonctions internes de str
civilite_nom_complet = " ".join(mots)
print(f"chaine: {civilite_nom_complet}")
# %% ---------------- fonctions internes exclusives aux listes -----------------
mots = ["appeler", "un"]

# ajouter "chat" à droite avec [] ou autrement
# mots[2] = "chat" # [] : IndexError
# mots = mots + ["chat"]
# mots += ["chat"]

# append ne retourne RIEN ( -> None) MAIS agit DIRECTEMENT sur mots
mots.append("chat")

print(mots)

# concaténer ["chat", "un", "chat", "gris"] à droite avec une fonction non +
mots.extend(["chat", "un", "chat", "gris"])
print(mots)


# ajouter "il" à gauche
mots.insert(0, "Il")
print(mots)

# ajouter "faut" à gauche d'"appeler"
mots.insert(mots.index("appeler"), "faut")
print(mots)

# supprimer le dernier élement de mots ET retourne sa valeur
last_inserted_first_out = mots.pop()
print(mots)

# supprimer le premier élément //
# mots.pop(0)

# supprimer la 1ère occurence de chat 
mots.remove("chat")
print(mots)

# %% --------------- listes et tuples / str : mutabilité et immutabilité ------------
mots = ["nommer", "un", "chien"]

## remplacer "chien" en "chat" dans mots avec []
mots[2] = "chat"
## TRANSFORMATION MUABLE ==> CHANGEMENT PARTIEL DIRECT (ex. append ne retourne pas mais change)


## même chose avec un tuple
mots = tuple(mots)
## remplacer "nommer" en "appeler" dans mots
# mots[0] = "appeler" # ERROR

## transformer mots en une str phrase et mettre le 1er car. en majuscule
phrase = " ".join(mots)
# phrase[0] = "N" # ERROR

## TRANSFORMATION IMMUABLE ==> REAFFECTATION COMPLETE (capitalize retourne mais ne change pas phrase)
phrase = phrase.capitalize()
# %% --------------- opérateur in : test d'appartenance -----------------------

phrase = "appeler un chat"

# savoir si "chat" est dans phrase
"chat" in phrase
# savoir si "chien" n'est pas dans phrase
"chien" not in phrase
# idem en transformant phrase en mots
mots = phrase.split()
"chat" in mots
