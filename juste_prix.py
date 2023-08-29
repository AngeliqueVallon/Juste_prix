from random import *

prix = randint(1,50)
essai = None

def justePrix(prix):
    for i in range(1,6):
        try : 
            a = int(input(f"prix {i} ? "))
        except :
            print("Valeur incorrecte")
            continue # Redémarre à l'itération suivante
        if prix == a:
            return("Bravo")
        elif prix > a :
            print("Trop bas")
        elif prix < a :
            print("Trop haut")
    if prix != a:    
        return("Perdu")

print(justePrix(prix))