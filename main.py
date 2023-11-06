# generation du chiffre (0 à 100) à trouver
import random

guess = random.randint(0, 100)
print(guess)

# boucle jusqu'à avoir trouver
while True:
    # demander le chiffre de l'utilisateur
    chiffre = int(input('Entrez un chiffre entre 0 et 100:'))

    # comparaison et réponse
    if chiffre < guess:
        print('Trop petit.')
    elif chiffre > guess:
        print('Trop grand.')
    else:
        break

# Fin du programme
print('Bravo vous avez trouvé !')
