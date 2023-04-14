import requests

while True:
    pok = input("Which pokemon do you want to find ? ")
    pok = pok.lower()
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pok}")
    if req.ok:
        info = req.json()
        name = info['name']
        height = info['height']
        for ability in info['abilities']:
            ability['ability']
        print("\n")
        print("---Pokemon Details---\n")
        print(f"Name\t: {name}")
        print(f"Height\t: {height}")
        print(f"Ability\t: {ability}")
    else:
        print("Pokemon not found")

    find_again = input("Do you want to find pokemon again ?(y/n)")
    if find_again != 'y':
        print("Thanks for Finding !")
        break
