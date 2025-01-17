with open("TP5/phrases.txt", "a") as file:
    while True:
        add_more = input("ajouter d'autres phrases? (y/n): ").strip().lower()
        if add_more == "y":
            phrase = input("Enter a phrase: ")
            file.write(phrase + "\n")
        else:
            break
