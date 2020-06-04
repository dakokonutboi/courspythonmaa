semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

print(semaine)


print("Cinq premiers jours :",semaine[0:5])

print("Deux derniers jours :",semaine[-2:])

print("Deux derniers jours :",semaine[5:])

print("Dernier jour :", semaine[-1])

print("Dernier jour :", semaine[6])

print("Dernier jour :", semaine[len(semaine) - 1])

semaine.reverse()

print("Semaine inversee :", semaine)

print("Semaine inversee :", semaine[::-1])
