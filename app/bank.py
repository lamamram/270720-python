from datetime import datetime


class Person:
  def __init__(self, firstname: str, name: str):
    self.firstname = firstname
    self.name = name

  ## dans l'héritage: comportement hérité client peut utiliser çà
  def get_full_name(self):
      return f"{self.firstname.capitalize()} {self.name.upper()}"


class Client(Person):
  ## dans l'héritage: une surcharge (override) on doit utiliser le __init__ de person MAIS avec l'objet client
  ## et on complète le __init__ de client avec ses propres attributs
  def __init__(
      self, 
      firstname: str, 
      name: str, date_joint: str, 
      format: str="%Y-%m-%d"
  ):
    super().__init__(firstname, name)
    self.date_joint: datetime = datetime.strptime(date_joint, format)

  ## dans l'héritage: comportement spécifique au client
  def get_date_joint(self, format: str="%Y-%m-%d"):
    return self.date_joint.strftime(format)




class Account:
  """
  le premier paramètre de toute méthode est nommé par convention self
  """

  def __init__(self, client: Client, balance: float, overdraft: float=200) -> dict:
    """
    __init__: méthode "magique" qui a pour but d'initialiser les attributs d'objets
    """
    ## préfixer un attribut avec "__" rend l'attribut PRIVE
    # permet de protéger l'utilisation des attributs: 
    # seules les méthodes publiques peuvent les manipuler
    # les méthodes publiques sont un "sas" d'entrée / sortie avec l'extérieur
    self.client = client
    self.__balance = balance
    self.overdraft = overdraft
  
  def __str__(self):
    """
    méthode magagique (dunder): permet la conversion des objets account en str
    """
    return f"Account de {self.client.get_full_name()} avec solde {self.__balance} et découvert autorisé {self.overdraft}"

  def __eq__(self, other):
    """
    méthode magagique (dunder): permet la comparaison des objets account
    """
    return self.__balance == other.__balance and self.overdraft == other.overdraft

  def __getitem__(self, key):
    return "acc[key]"

  def __setitem__(self, key, value):
    return "acc[key] = value"

  def __call__(self, *args, **kwds):
    return "acc()"

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

  def get_client_full_name(self):
    return self.client.get_full_name()