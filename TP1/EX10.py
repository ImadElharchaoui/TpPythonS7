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
