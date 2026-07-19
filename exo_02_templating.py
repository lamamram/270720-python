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



# %% --------------------- portage en fonction ----------------------

"""
porter le code du while ou du for en fonction
0/ copier coller le code et l'entourer avec le bloc def ????():
1/ vous nommez la fonction de façon pertinente
2/ gérer la valeur de retour
3/ trouver les paramètres pertinents (positionnels/obligatoires), nommés avec defaut, *, **
4/ faire le refactoring: remplacer les variables globales de bout de code d'origine par les paramètres
"""




