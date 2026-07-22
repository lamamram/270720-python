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