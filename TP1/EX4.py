
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
