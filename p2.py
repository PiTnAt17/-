def printPetNames(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet,name in pets.items():
        print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"]
              