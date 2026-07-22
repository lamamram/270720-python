# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": 500,
    "section": 30,
    "debit": 2
}

# %%
## 1/ chercher une structure évidente pour une bloucle for
##  1a/ itération sur le dico mais que faire des slots non remplacés ?
## 2/ si on selectionne le while
##  2a/ faire un remplacement sans boucle
##  2b/ observer qui a changé ==> indice d'une condition while
##  2c/ encapsuler le cas particulier par le while

while "((" in _template:
    index_start = _template.index("((") + 2
    index_end = _template.index("))")
    key = _template[index_start:index_end]

    value = injections.get(key, "N/A")
    _template = _template.replace("((" + key + "))", str(value))

print(_template)


# %%
# for k, v in injections.items():
#     _template = _template.replace("((" + k + "))", str(v))
# print(_template)


# %% --------------------- portage en fonction ----------------------

"""
porter le code du while ou du for en fonction
0/ copier coller le code et l'entourer avec le bloc def ????():
1/ vous nommez la fonction de façon pertinente
2/ gérer la valeur de retour
3/ trouver les paramètres pertinents (positionnels/obligatoires), nommés avec defaut, *, **
4/ faire le refactoring: remplacer les variables globales de bout de code d'origine par les paramètres
"""

def parse_template(
        tpl: str, 
        data: dict, 
        delimiters: tuple=("{{", "}}"), 
        default: str="N/A",
        **opts
    ) -> str:
    """
    fonction de parsing d'un template avec des slots à remplacer par des valeurs d'un dictionnaire
    options secondaires: debug=True pour afficher les clés trouvées
    """
    start_delim, end_delim = delimiters
    while start_delim in tpl:
        index_start = tpl.index(start_delim) + len(start_delim)
        index_end = tpl.index(end_delim)
        key = tpl[index_start:index_end]
        if "debug" in opts and opts["debug"] == True:
            print(f"DEBUG key: {key}")

        value = data.get(key, default)
        tpl = tpl.replace(start_delim + key + end_delim, str(value))

    return tpl

parsed_template = parse_template(_template, injections, delimiters=("((", "))"), default="N/A")
print(parsed_template)

print(parse_template("Hello {{name}}!", {"name": "Alice"}, debug=True))




# %%
