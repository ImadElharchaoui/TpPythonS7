# Exercice 1 
def somme_liste(list):
    return sum(list)

# Exemple exercice 1
print(somme_liste([1, 2, 3, 4]))

# Exercice 2
def max_tuple(tuple):
    return max(tuple)

# Exemple Ex 2
print(max_tuple((8, 6, 7, 3, 1)))

# EX 3
def intersection(ensemble1, ensemble2):
    return ensemble1 & ensemble2
# exemple Ex3
print(intersection({1, 2, 69}, {1, 2, 654544}))

# EX4
def compte_occurence(list):
    dic = {}
    for mot in list:
        if(mot in dic):
            dic[mot] +=1
        else:
            dic[mot] = 1
    return dic
            
# exemple EX4
print(compte_occurence(["n", "n", "m", "l", "m"]))

# exerices 5
def factorielle(n):
    if n == 1:
        return n
    return factorielle(n - 1) * n
    
print(factorielle(10))

# exercice 6
carre = lambda a: a * a
print(carre(2))

# exercice 7
def salutation(nom, message="Bonjour"):
    print(f"{message} {nom}")
    
salutation("ali")

# EX 8
def somme_args(*arg):
    return sum(arg);
#exemple 8
print(somme_args(4,5,2,1))

# ex 9
def analyse_texte(texte):
    return {"mots": len(texte.split()), "chars": len(texte) - texte.count(" ")}
    
#exemple EX 9
print(analyse_texte("as987sd89 7fa/-*-*-/"))

#ex 10
def fusionner_dicts(dic1, dic2):
    TheDIC = {}
    for key, val in dic1.items():
        if(key in dic2.keys()):
            TheDIC[key] = val + dic2[key]
        else:
            TheDIC[key] = val
    for key, val in dic2.items():
        if(key not in TheDIC.keys()):
            TheDIC[key] = val;
    return(TheDIC)
#exemple 10
dic1 = {"num": 2, "nn": 3 }
dic2 = {"num": 4, "yy": 0 }
print(fusionner_dicts(dic1, dic2))
