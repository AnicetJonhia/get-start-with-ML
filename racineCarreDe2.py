""" calcule de la racine carrée de 2 en utilisant la méthode Héron"""
import math
# initialisation
x = 1
erreur = 1
précision = 0.001
# boucle itérative
while erreur > précision:
    # mise à jour de l'estimation
    x = (x + 2/x)/2
    # mise à jour de l'erreur avec la nouvelle valeur de x
    erreur = abs(x**2 - 2)
    print(f"x = {x}")

print(f"la racine carrée de 2 vaut : {x}")
