
# exerices 5
def factorielle(n):
    if n == 1:
        return n
    return factorielle(n - 1) * n
# Exemple 5
print(factorielle(10))