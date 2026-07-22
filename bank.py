def withdraw(account: dict, amount: float) -> float:
  if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
  elif amount > account["balance"] + account["overdraft"]:
    print(f"Transaction refusée: {amount} fonds insuffisants")
  else:
    account["balance"] -= amount
    return account

if __name__ == "__main__":
    print("coucou")