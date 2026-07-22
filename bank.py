def withdraw(account: dict, amount: float):
  if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
  elif amount > account["balance"] + account["overdraft"]:
    print(f"Transaction refusée: {amount} fonds insuffisants")
  else:
    account["balance"] -= amount
    print(f"Transaction acceptée")

if __name__ == "__main__":
    print("coucou")