from datetime import datetime

class Client:
  def __init__(
      self, 
      firstname: str, 
      name: str, date_joint: str, 
      format: str="%Y-%m-%d"
  ):
    self.firstname = firstname
    self.name = name
    self.date_joint: datetime = datetime.strptime(date_joint, format)




class Account:
  """
  le premier paramètre de toute méthode est nommé par convention self
  """

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