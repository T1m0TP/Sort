# On importe le module numpy
import numpy as np

print('''
                 ((((( ☻ )))))
     ______   ____|_|_____
    | ♥    \ /|_||_||_||_|\  Instagram: @codeur.tim
    |_______|_|_||_||_||_|_| Github: T1m0TP
            /___\    /___\

''')

# On définit l'array
toSort = np.random.randint(0, 100, 50)
# On crée 2 boucles
for i in range(len(toSort)):
    for j in range(len(toSort)):
        # On crée une condition qui donne l'ordre de rangement des nombres
        if toSort[i] <= toSort[j]:
            # On classe les nombres
            toSort[i], toSort[j] = toSort[j], toSort[i]
print(toSort)
