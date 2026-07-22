# %% ------------- gestion des str --------------

_str = "bonjour"
print(f"afficher la chaine et son id: {_str}, {id(_str)}")
print(f"afficher un caractère à l'index n: {_str[5]}")
print(f"afficher un caractère en dernière position: {_str[-1]}")
print(f"afficher l'index de la 1ère occurence d'une sous chaîne jour : {_str.index('jour')}")
print(f"afficher une sous chaine entre n compris et m non compris: {_str[2:5]}")
print(f"afficher une sous chaine entre n jusqu'à la fin: {_str[2:]}")
print(f"afficher une sous chaine depuis le début jusqu'à l'index n: {_str[:5]}")
print(f"savoir si une sous chaine est dans une chaine: {'on' in _str}")
print(f"savoir si une sous chaine n'est pas dans une chaine: {'on' not in _str}")
print("IMMUABILITE: modification d'une str")
_str.find() = _str.upper()
print(f"str modifiée et son id: {_str}, {id(_str)}")

phrase = "bonjour tout le monde"
print(f"transformer la phrase {phrase} en liste de mots: {phrase.split()}")
mots = phrase.split()
print(f"transformer une liste de str {mots} en str: {' '.join(mots)}")
print(f"fonction globale sur les str: len(phrase) = {len(phrase)}")

# %% ---------------- gestion des list -----------------
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"afficher la liste et son id: {l}, {id(l)}")
print(f"afficher un élément à l'index 2: {l[2]}")
print(f"afficher un élément en dernière position: {l[-1]}")
print(f"afficher l'index de la 1ère occurence d'un élement 8 : {l.index(8)}")
print(f"afficher une sous liste entre 2 compris et 5 non compris: {l[2:5]}")
print(f"afficher une sous liste entre 2 jusqu'à la fin: {l[2:]}")
print(f"afficher une sous liste depuis le début jusqu'à l'index 5: {l[:5]}")
print(f"savoir si 5 est dans la liste: {5 in l}")
print(f"savoir si 5 n'est pas dans la liste: {5 not in l}")
print("MUTABILITE: modification d'une liste")
l.append(11)
print(f"liste modifiée et son id: {l}, {id(l)}")
l.pop()
print(f"liste modifiée et son id: {l}, {id(l)}")
print(f"fonctions globales sur les listes: len(l) = {len(l)}, max(l) = {max(l)}, sum(l) = {sum(l)}")

# %% -------------- effet pervers de la muabilité -----------------
l = [1, 2, 3, 4, 5]
l2 = l

l2.append(6)
print(f"passage en référence d'un type muable")
print(f"l: {l}, l2: {l2}, l is l2: {l is l2}")

l2 = l.copy()
l2.append(7)
print(f"copie creuse d'un type muable")
print(f"l: {l}, l2: {l2}, l is l2: {l is l2}")

# %% --------------- gestion des tuples -----------------
t = (1, 2, 3, 4, 5)
print(f"afficher le tuple et son id: {t}, {id(t)}")
print(f"afficher un élément à l'index 2: {t[2]}")
print(f"afficher un élément en dernière position: {t[-1]}")
print(f"afficher l'index de la 1ère occurence d'un élement 4 : {t.index(4)}")
print(f"afficher une sous tuple entre 2 compris et 5 non compris: {t[2:5]}")
print(f"afficher une sous tuple entre 2 jusqu'à la fin: {t[2:]}")
print(f"afficher une sous tuple depuis le début jusqu'à l'index 5: {t[:5]}")
print(f"savoir si 5 est dans le tuple: {5 in t}")
print(f"savoir si 5 n'est pas dans le tuple: {5 not in t}")
print("IMMUABILITE: modification d'un tuple")
#       tuple à 1 élément
t = t + (6,)
print(f"tuple modifié et son id: {t}, {id(t)}")

# %% ------------------ gestion des dict -----------------
user = {"firstname": "roger", "age": 56, "taille": 1.75}
print(f"afficher le dict et son id: {user}, {id(user)}")
print(f"afficher la valeur d'une clé: {user['age']}")
print(f"savoir si une clé est dans le dict: {'age' in user}")
print(f"savoir si une clé n'est pas dans le dict: {'age' not in user}")
print("MUTABILITE: modification d'un dict")
user["age"] = 57
print(f"dict modifié et son id: {user}, {id(user)}")
print(f"fonctions globales sur les dict: len(user) = {len(user)}, max(user) = {max(user)}, min(user) = {min(user)}")
print(f"fonctions internes sur les dict: user.get('age') = {user.get('age')}, user.values() = {list(user.values())}, user.items() = {list(user.items())}")
# %% ------------------ conditions -----------------

if "email" in user:
    print(user["email"])
elif "age" in user:
    print(user["age"])
else:
    print("N/A")

# %% ------------------ itérations -----------------

for letter in _str:
    print(letter)

for number in l:
    print(number)

for k, v in user.items():
    print(k, v)

# fibonacci sequence
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b