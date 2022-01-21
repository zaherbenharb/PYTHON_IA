#!/usr/bin/env python
# coding: utf-8

# In[1]:


#exercie 1 Écrivez un programme qui trouvera tous ces nombres qui sont divisibles par 7 mais qui ne sont pas un multiple de 5, entre 2000 et 3200 (les deux inclus). 
#Les nombres obtenus doivent être imprimés en séquence sur une seule ligne.
for i in range(2000,3201):
    if (i % 5) != 0 and (i % 7) == 0:
        print (i)


# In[2]:


#exercie2 Écrire un programme capable de calculer la factorielle d'un nombre donné. Les résultats doivent être imprimés en séquence sur une seule ligne. 
#Supposons que l'entrée suivante soit fournie au programme : 5 Alors, la sortie devrait être : 120
nbr = int(input('Entrez un nombre : '))
x = 1
for i in range(1, nbr+1):
    x = x * i
print (nbr,'! = ',x)


# In[3]:


#exercice 3 
#Avec un nombre entier n donné, 
#écrivez un programme pour générer un dictionnaire qui contient (i, i*i) 
#tel qu'il soit un nombre entier compris entre 1 et n (tous deux inclus). 
#puis le programme doit imprimer le dictionnaire. Supposons que l'entrée suivante soit fournie au programme :
# 8 Ensuite, la sortie doit être : {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64 } 

n = int(input('Entrez un nombre : '))
{x: x*x for x in range(1,n+1)}


# In[4]:


#exercice4
#Étant donné une chaîne non vide et un int n, 
#renvoie une nouvelle chaîne où le caractère à l'index n a été supprimé. La valeur de n sera un index valide d'un caractère
#dans la chaîne d'origine (c'est-à-dire que n sera compris entre 0..len(str)-1 inclus). 
#missing_char('kitten', 1) → 'ktten' par exemple ici on supprime "i" qui se trouve dans l'index 1
#missing_char('kitten', 0) → 'itten' ici on supprime "k" qui est dans l'index 0
#missing_char('kitten', 4) → 'kittn' ici on supprime "e" qui est dans l'index 4
mot = str(input("entrez un mot:"))
f = int(input("numero de caractère à supprimer "))
print(mot.replace(mot[f],"",1))


# In[5]:


#exercice5
'''Écrivez un programme NumPy pour convertir un tableau NumPy en une structure de liste Python.

Production attendue: 

Éléments du tableau d'origine : [[0 1] [2 3] [4 5]] 

Tableau à liste : [[0, 1], [2, 3], [4, 5]]
'''
import numpy as np
a=np.array([[0, 1] ,[2 ,3] ,[4 ,5]])
list1 = a.tolist()
print(list1)


# In[6]:


#exercice6
'''Écrivez un programme NumPy pour calculer la matrice de covariance de deux tableaux donnés. 

Tableau d'origine1 : [0 1 2] 

Tableau d'origine2 : [2 1 0] 

Matrice de covariance desdits tableaux : [[ 1. -1.] [-1. 1.]]
'''
import numpy as np
A=np.array([0,1,2])
c=np.array([2,1,0])          
B=np.cov(A,c)
print(B)


# In[8]:


#exercice7

'''Question : Écrivez un programme qui calcule et imprime la valeur selon la formule donnée : Q = Racine carrée de [(2 * C * D)/H] 

Voici les valeurs fixes de C et H : C est 50. H est 30. 

D est la variable dont les valeurs doivent être entrées dans votre programme dans une séquence séparée par des virgules. (cela signifie que D contient plus que la valeur)

Exemple Supposons que la séquence d'entrées séparées par des virgules suivante est donnée au programme : 100,150,180 La sortie du programme doit être : 18,22,24 

Pour expliquer cela plus en détail, nous obtiendrons un résultat pour chaque valeur de D : Q1= Racine carrée de [(2 * C * 100)/H] =18, Q2= Racine carrée de [(2 * C * 150)/H ] = 22 et Q3 = Racine carrée de [(2 * C * 180)/H] = 24

Conseils : Si la sortie reçue est sous forme décimale, elle doit être arrondie à sa valeur la plus proche (par exemple, si la sortie reçue est 26,0, elle doit être imprimée sous la forme 26) En cas de données d'entrée fournies à la question, il doit être supposé être une entrée de console.
'''


import numpy as np 

D1,D2,D3=list(map(int,input('tapez 3 nombres:').split(",")))

res1=(2*50*int(D1))/30
RES1=np.sqrt(res1)

res2=(2*50*int(D2))/30
RES2=np.sqrt(res2)

res3=(2*50*int(D3))/30
RES3=np.sqrt(res3)

print(round(RES1),round(RES2),round(RES3))


# In[ ]:




