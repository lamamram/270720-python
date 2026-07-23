# %% un exemple en programmation impérative / procédurale 
## sans programmation orientée objet

# ce dictionnaire représente la structure générique d'un compte
account = {
  "balance": 0,
  "overdraft": 0,
}

# créer une fonction init_account qui va mettre à jour les champs d'un dict account en param
# à partir de paramètres balance et overdraft
def init_account(account: dict, balance: float, overdraft: float) -> dict:
  real_account = account.copy()
  real_account["balance"] = balance
  real_account["overdraft"] = overdraft
  return real_account

# créer une fonction withdraw pour effectuer un retrait d'un montant sur un compte en param.
def withdraw(account: dict, amount: float) -> dict:
  """
  fonction de retrait sur un dictionnaire...
  """
  if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
  elif amount > account["balance"] + account["overdraft"]:
    print(f"Transaction refusée: {amount} fonds insuffisants")
  else:
    account["balance"] -= amount
    return account


# %% -- utilisation simple ---------------
if __name__ == "__main__":
  real_account = {
    "balance": 1000,
    "overdraft": 200
  }

  amount = float(input("amount: "))
  withdraw(real_account, amount)
  print(real_account)

  

# %% ----------- utilisation avec initialisation -----------
## programme principal
if __name__ == "__main__":
  ## initialiser le dictionnaire account avec un solde de 1000 et un découvert de 200
  real_account = init_account(account, balance=1000, overdraft=200)
  # print(real_account)
  # print(account)

  ## saisir un montant, effectuer le retrait et afficher le solde après
  amount = input("Entrez un montant : ")
  amount = int(amount)

  withdraw(real_account, amount)
  print(real_account)
  print(account)

# %% --- même exemple en Programmation Orientée Objet (POO) avec attributs de classes et sans __init__ ---------

class Account:

  # attributs (ici de classe) => VARIABLES INTERNES
  balance: float = 0.
  overdraft: float = 0.
  
  # méthodes => FONCTIONS INTERNES
  def withdraw(account, amount: float):
    if amount < 0:
      print(f"Transaction refusée: {amount} négatif")
    elif amount > account.balance + account.overdraft:
      print(f"Transaction refusée: {amount} fonds insuffisants")
    else:
      account.balance -= amount
      print(f"Transaction acceptée: nouveau solde {account.balance}")

if __name__ == "__main__":
  # créer un objet de type Account <=> instancier un objet de classe Account
  acc = Account()
  acc.balance = 1000
  acc.overdraft = 200
  
  ## le premier de toute méthode est un objet de cette classe
  ## ici cet objet est acc !! donc on a pas besoin de le redemander quand on appelle la méthode
  acc.withdraw(500)
  print(acc.balance)

# %% --- même exemple en Programmation Orientée Objet (POO) avec __init__ ---------

class Account:
  """
  le premier paramètre de toute méthode est nommé par convention self
  """

  __balance: float = 0
  overdraft: float = 0

  def __init__(self, balance: float, overdraft: float=200) -> dict:
    """
    __init__: méthode "magique" qui a pour but d'initialiser les attributs d'objets
    """
    ## préfixer un attribut avec "__" rend l'attribut PRIVE
    # permet de protéger l'utilisation des attributs: 
    # seules les méthodes publiques peuvent les manipuler
    # les méthodes publiques sont un "sas" d'entrée / sortie avec l'extérieur
    self.__balance = balance
    self.overdraft = overdraft
  
  def withdraw(self, amount: float):
    if amount < 0:
      print(f"Transaction refusée: {amount} négatif")
    elif amount > self.__balance + self.overdraft:
      print(f"Transaction refusée: {amount} fonds insuffisants")
    else:
      self.__balance -= amount
      print(f"Transaction acceptée: nouveau solde {self.__balance}")

  def get_balance(self):
    return self.__balance
  
if __name__ == "__main__":
  acc = Account(balance=1000)
  acc.withdraw(500)
  print(acc.overdraft)
  print(acc.get_balance())
  # print(Account.overdraft)
  ## __balance: est considéré comme privé
  ## on ne peut pas le lire ou le modifier depuis l'EXTERIEUR de la classe
  # print(acc.__balance) # AttributeError

  # print(acc._Account__balance) => moyen détourné d'utiliser un attribuer privé depuis l'extérieur
  # print(acc.__balance)

# %% ------------------ encapsulation (public / private) frauduleuse en python ------------------

##### MORALE DE L'HISTOIRE ##################

# il n'ya pas en réalité d'attributs privés => pas d'encapsulation effective
# par contre, on peut l'utiliser pour STRUCTURER VOS CLASSES
# protected en python c'est _var => public mais n'est pas spécifié dans la documentation

# %% ------------- en python: TOUT EST OBJET ---------------------
# instancier un objet t d'une classe Truc vide

class Truc:
  pass

d = dict(k1=1, k2=2)
t = Truc()
print(d, t)

# afficher le type de t et de d
print(type(d), type(t))
# vérifier que t est d'instance de Truc  et d instance de dict avec isinstance()
print(isinstance(d, dict), isinstance(t, Truc))


# %% ------------------------ exemple client ---------------------------------
## ajouter la classe Account dans le module app.bank

## 1.créer une classe client qui contient firstname, name, et date_joint :objet datetime
## et 2 méthodes: 
##     get_full_name: retourne le prénom capitalisé et le nom en majuscule
##     get_date_joint: retourne la date dans le format voulu en paramètre

from app.bank import Client, Account

cl = Client("john", "doe", "2016-07-22")
# print(cl.date_joint.strftime("%d/%m/%Y"))
print(cl.get_full_name())
print(cl.get_date_joint("%d/%m/%Y"))

acc = Account(cl, 2000)
print(acc.get_client_full_name())


# %% -------------------------- héritage simple -----------------------------

#### CF app/bank.py
# reprendre l'exemple précédent sachant qu'un client EST une personne avec un prénom et un nom
## person est considérée comme classe parente de client
## client est //                      enfant de personne , hérite de personne

## la classe enfant peut réutiliser directement les méthodes parentes
## la classe enfant peut également créer ses propres méthodes
## super().<methode>() permet d'exécuter une méthode de la classe PARENT 
## dans la classe ENFANT et sur l'objet ENFANT

# classe personne
#    utilise prénom et nom

# classe client est une personne
#    utilise prénom, nom et date_joint      



# %% ------------------------- injection de dépendances -----------------------------

## relation de type AVOIR entre une classe "utilisateur" et une autre qui est une dépendance
## l'utilisateur mange sa dépendance à l'instanciation et utilise LA SIGNATURE PUBLIQUE de cette dépendance

## un compte possède un client et un client peut posséder plusieurs comptes
## on peut voir le nom complet du client depuis le compte


# %% ------------------------ méthodes magiques ------------------------
## autres méthodes dunders (magique __xxxx__) utilisation de __str__, __add__
from app.bank import Account, Client

cl = Client("john", "doe", "2016-07-22")
acc = Account(cl, 2000)
acc2 = Account(cl, 1000)

print(acc)

print(acc == acc2)



# %% ------------------------- héritage multiple + polymorphisme --------------------
# classe abstraite = impossible d'instancier
# abstractmethod est un décorateur qui rend une méthode abstraite
from abc import ABC, abstractmethod

# "Interface" en python
# une interface garanti un ensemble de méthodes 
# (des noms des paramètres d'i/o) liés à un SAVOIR FAIRE
class IAccount(ABC):
  @abstractmethod
  def __init__(self, balance: float) -> None: pass

  @abstractmethod
  def get_balance(self) -> float: pass


class BasicAccount(IAccount):
  def __init__(self, balance: float, overdraft: float):
    self.balance = balance
    self.overdraft = overdraft
  
  def withdraw(self, amount: float):
    if amount <= self.balance + self.overdraft: self.balance -= amount
  
  def get_balance(self):
    return self.balance

class SavingAccount(IAccount):
  def __init__(self, balance: float, rate: float):
    self.balance = balance
    self.rate = rate
  
  def interest(self):
    self.balance += self.balance*self.rate/100

class PremiumAccount(BasicAccount, SavingAccount):
  def __init__(self, balance: float, overdraft: float, rate: float):
    # indétermination: quel __init__ est utilisé ? en réalité il ya un algo MRO: ordre de résolution de méthodes
    # super().__init__(balance, overdraft)
    # plus simple
    BasicAccount.__init__(self, balance, overdraft)
    SavingAccount.__init__(self, balance, rate)

  def get_balance(self):
    # ici super ira chercher de BasicAccount
    return super().get_balance()

class Manager:
  ## POLYMORPHISE == demander un objet de type IAccount 
  # ==> j'utilise n'importe quel objet qui implémente toutes les signatures de IAccount
  def __init__(self, account: IAccount):
    self.__account = account
    print(self.__account.get_balance())

if __name__ == "__main__":
  p_acc = PremiumAccount(1000, 200, 2.5)
  print(p_acc.get_balance(), p_acc.overdraft, p_acc.rate)
  p_acc.withdraw(500)
  p_acc.interest()
  print(f"nouveau solde: {p_acc.get_balance()}")
   
  print(PremiumAccount.mro()) # ordre simple des résolution des méthodes



# %% -------------- itérateur / itérable ---------------
# un itérateur/itérable : une classe qui implémente les 3 méthodes 
# __init__, __iter__, __next__
class MyRange: pass
class MyRange:

  def __init__(self, limit=10):
    """ init pour la condition d'arrêt """
    self.limit = limit
  
  def __iter__(self) -> MyRange:
    """ un itérateur == itérable avec un compteur """
    self.cpt = 0
    return self
  
  def __next__(self):
    if self.cpt < self.limit:
      ret = self.cpt
      self.cpt += 1
      return ret
    else:
      raise StopIteration

# mr est un itérable
mr = MyRange()

# iter exécute mr.__iter__() pour faire d'it un itérateur
it = iter(mr)

print("-"*10 + "pas à pas avec next" + "-"*10)

for _ in range(10):
  print(next(it))

# recharge l'itérateur
it = iter(mr)
print(next(it)) # => l'itération de TROP sauf si le compteur est rechargé

print("-"*10 + "boucle for" + "-"*10)

# 1. recharge / créé le compteur
# enchaine les next
# et CAPTURE l'exception StopIteration
for i in it:
  print(i)


# %% ------------------------- gestionnaire de contexte --------------------
class Ctx:
  def __enter__(self):
    print("Before")
    # donne une valeur à la variable "as xxx"
    return self
  
  def __exit__(self, x_type, x_msg, x_tb):
    # exit: peut capturer une exception déclenchée dans le bloc
    print(x_type, x_msg)
    print("After")
    # en retournant qqch vrai: __exit__ capture réellement l'exception
    return True

with Ctx() as c:
  print(f"variable de contexte: {c}")
  3 / 0
  print("dans le bloc")

print("fin")

# %%
