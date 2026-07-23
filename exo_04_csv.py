# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.ZipFile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. déplacer le fichier csv en dans data/dns.csv
4.. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de 100k lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne (dns_100k.csv, dns_200k.csv)
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
j'ouvre en lecture le gros fichier:
  j'accumule 100k ligne (sans header)
  j'en fais un fichier
  je le fais 2x
  (utiliser intelligemment break et continue)

"""

# %% -------------------- téléchargement avec le paquet requests à partir de pip ---------
# pip install requests (dans l'environnement virtuel)
import requests
import os

# HTTP: communication client/serveur
# HTTP: le client envoie une requête HTTP au serveur
# requête HTTP: (URL, verbe HTTP, entêtes de requêtes, corps (optionnel))
                     # lire, créer, modifier, supprimer, ...
         # verbe HTTP: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
         # corps de la requête: données de formulaire, ou pièces jontes, objets json/xml en cas d'api REST

# réponse HTTP: (code de statut, entêtes de réponse, corps de la réponse)
         # code de statut: 200, 404, 500, ...
         # corps de la réponse: page HTML, fichier binaire, objet json/xml en cas d'api REST
#              adresses IP  --------------------path----------------querystring-------------
# -protocole://nom de domaine/chemin/physique/ou/virtuel/fichier.xxx?param1=val1&param2=val2#ancre
URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
DNS_NAME="dns.csv"

archive_name = URL.split("/")[-1]
# stocker la réponse HTTP liée à la requête HTTP associée à l'url
# on utilise le verbe HTTP "GET" qui est utilisé pour faire de la lecture

if not os.path.exists(f"./{archive_name}"):
   try:
      response = requests.get(URL)

      ### contrôles

      # 1. le code de statut de la réponse

      # les codes 2xx sont OK
      # les codes 3xx sont OK ~mais il y a eu redirection
      # les codes 4xx sont KO pb d'url (404 not found)
      # les codes 5xx sont KO pb sur le serveur distant
      if 200 <= response.status_code < 300:
         # regarder la valeur de l'entête Content-Type pour savoir la nature de ce qu'on a téléchargé
         if "application/zip" in response.headers["content-type"]:
            # wb => création d'un fichier binaire (.zip)
            with open(f"./{archive_name}", mode="wb") as f:
                  ## .content pour un flux d'octet / .text pour une page HTML / .json() pour du JSON
                  f.write(response.content)
      else:
         raise ValueError(f"mauvais code : {response.status_code}")
   except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
      print(e)
        



# %%  ---------------------- decompression -----------------------------
from zipfile import ZipFile

if not os.path.exists(f"./data/{DNS_NAME}"):
   with ZipFile(f"./{archive_name}", mode="r") as zf:
      to_extract = zf.namelist()[0]
      zf.extract(to_extract)

   os.mkdir("./data")
   os.rename(f"./{to_extract}", f"./data/{DNS_NAME}")

# %% ----------------  manipulation du fichier ---------------------






# %% --------------------------- idem avec pandas --------------------------------
# pip install pandas (dans l'environnement virtuel)

import pandas as pd
import numpy as np

dns_df = pd.read_csv(URL, delimiter=";", encoding="utf-8")
dns_df

# %% ----------- écrire le csv en zip à partir du DataFrame ------------
dns_df.to_csv(
    "dns.zip",
    sep=";", 
    encoding="utf-8",
    compression={
        "archive_name": "dns.csv",
        "method": "zip"
    },
    index=False
)
# %% ---------------------- exemple (group by): le nombre de dns par pays -----------

dns_subset_df = pd.read_csv(
    "dns.zip",
    sep=";",
    encoding="utf-8",
    nrows=10**6,
    usecols=["Nom de domaine", "Pays BE"]
)
dns_subset_df
# %%
gb = dns_subset_df.groupby("Pays BE")
count_df = gb["Nom de domaine"].count().sort_values(ascending=False)
count_df
# %%
