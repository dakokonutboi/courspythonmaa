# Cours Python Maa
## Ressources
### Logiciels
**Edupython (Windows uniquement)** : https://edupython.tuxfamily.org/  
**Python pour terminal de commandes (Tous les systemes)** : https://www.python.org/downloads/  
**JuPyter** : https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb  
## Notes de cours
### Rappel
Assigner une valeur a une variable
```python
x = y
```
On assigne a la variable x la valeur y

### Listes
**IMPORTANT**  
**La fiche de cours est disponible dans les fichiers. Cherchez 'Fiche de cours.pdf'**
#### Introduction
Exemple de liste :
```python
animaux = ['girafe', 'tigre', 'singe', 'souris']
```
#### Indices (Index)
Les indices (index) d'elements d'une liste commencent a 0 et finissent a la longueur de la liste -1  
Obtenir l'element de la liste x d'index y
```python
x[y]
```
Exemple :
```python
animaux = ['girafe', 'tigre', 'singe', 'souris']
print("Element d'index 0 de la liste animaux :",animaux[0])
```
Resultat :
`Element d'index 0 de la liste animaux : giraffe`

#### Operations sur les listes
Concatenation (addition) de listes  
Mettre tous les elements de deux listes x et y dans une nouvelle liste z
```python
x = [1,2,3]
y = [4,5,6]
z = x + y
print("Nouvelle liste z =",z)
```
Resultat :
`Nouvelle liste z = [1,2,3,4,5,6]`
