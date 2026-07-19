# %% ---------------- code impératif avec sqlite3 -------------
"""
SQLITE3: BDD relationnelle avec un dialecte SQL simple
BDD en un seul fichier ou chargé en RAM
pas de host / port / user / password / droits
le module sqlite3 python est dans la lib standard

sqlite3 utilise la DbAPI python pour tous les clients de BDD en python
- méthode connect() => connexion (création ou connexion sur la bdd)
- méthode cursor()  => prompt sur la connexion
- méthode execute() => exécuter une requête SQL sur le cursor
- méthode fetch()   => faire sortir les enregistrements attendus
- méthode close()   => fermer la cnx
---------------- gérer les transactions -----------------
- méthode begin()   => commence une transaction
- methode commit()  => confitmer une tr
- méthode rollback()=> annuler une tr
"""

import sqlite3

# avec sqlite3, la base de donnée est un simple fichier dans le disque (pas de serveur)
#  //         , il n'y a pas d'utilisateur ni mot de passe ni gestion de droits
#  //         , si le fichier de base de données n'existe, la méthode connect() créé la base de donnée 
conn = sqlite3.connect("dns.db")
# prompt à partir de la connexion
cur  = conn.cursor()
# "hello world" pour vérifier la connexion
req = "SELECT SQLITE_VERSION()"
cur.execute(req)
# la requête rétourne une seule ligne qui ne contient qu'une colonne (la version)
row  = cur.fetchone()
print(row)
conn.close()

# %% ----------------- une connexion s'ouvre et se ferme ------------------
import sqlite3

# exécuter un script SQL pour créer les tables de la bdd

  ## notion hydratation des données 
  # je veux faire retourner des dictionnaires et pas des tuples

  ##

  # test



# %% ----------------------- insérer 100k lignes à partir d'un csv -----------------
## 1. ouvrir le fichier dns_100000.csv et extraire les deux 1ère colonnes dans une liste
## [[dns, pays], [dns, pays], ...]

## 2. créer la requête préparée 'INSERT INTO domain_name (?, ?) VALUES (?, ?)'
## hint utiliser cur.executemany()

## 3. vérifier qu'on a 100k enregistrement dans la table domain_name



# %% ----------------- client sqlite3 en poo et gestionnaire de contexte



# %% -------------------- initiation à sqlAlchemy (véritable ORM) ---------------

# pip install SQLAlchemy

# connexion et session pour pooling
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# définition des modèles
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# champs SQL
from sqlalchemy import String, Enum, Integer, Float, DateTime, Text, ForeignKey, func

from pathlib import Path
import csv

# %% -------------------------------- GLOBALS - se connecter à une pool de connexionq ------------------------------------

DB_PATH = Path(__file__).parent / "dns.db"
# chaîne de cnx :URI
DB_URI = f"sqlite:///{DB_PATH}"


engine = create_engine(
  DB_URI,
  # par défaut: on peut réutiliser le même thread pour une nouvelle cnx => pooling possible
  connect_args={"check_same_thread": False},
  # voir les requêtes SQL pour debug
  # echo=True
)

# factory de sessions
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# --------------------------- MODELES --------------------------------------------

class Base(DeclarativeBase):
  """classe de base pour tous les modèles (tables)"""
  pass

class DomainName(Base):
  __tablename__ = "domain_name"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  iso2: Mapped[str] = mapped_column(String(2), nullable=False)
  name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)

class Pays(Base):
  __tablename__ = "pays"
  iso2: Mapped[str] = mapped_column(String(2), primary_key=True)
  name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

# %% ------------------------------- init_db --------------------------------------------------


def init_db():
  import re
  import csv

  Base.metadata.create_all(bind=engine)

  with SessionLocal() as session:
    # Import pays depuis le script SQL
    sql_path = Path(__file__).parent / "domain_names_sqlite3.sql"
    with open(sql_path, "r", encoding="utf-8") as f:
      sql_content = f.read()

    # bidouille pas intéressante
    match = re.search(r"INSERT INTO `pays` VALUES (.+);", sql_content)
    if match:
      pays_values = re.findall(r"\('([^']+)','([^']+)'\)", match.group(1))
      for iso2, name in pays_values:
        # Pays(iso2=iso2, name=name)  => objet enregistrement de table
        # cet objet a une réalité en python et aussi dans la base
        # il faut synchroniser régulièrement les objet py et sql flush() commit()
        session.merge(Pays(iso2=iso2, name=name))

    # insérer les données avec SQLAlchemy
    data = []
    csv_path = Path(__file__).parent / "data" / "dns_100000.csv"
    with open(csv_path, mode="r", encoding="utf-8") as f:
      reader = csv.reader(f, delimiter=";")
      next(reader)
      for row in reader:
        data.append(DomainName(name=row[0], iso2=row[1]))   
    session.add_all(data)

    session.commit()

init_db()
# %% ------------------------- usage ----------------------------------------
from sqlalchemy import select, func

with SessionLocal() as session:
  # SELECT * FROM domain_name
  dns_count = session.execute(select(func.count()).select_from(DomainName)).scalar()
  print(f"Nombre de domaines: {dns_count}")

# %%
