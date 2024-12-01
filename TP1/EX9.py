# ex 9
def analyse_texte(texte):
    return {"mots": len(texte.split()), "chars": len(texte) - texte.count(" ")}
    
#exemple EX 9
print(analyse_texte("as987sd89 7fa/-*-*-/"))