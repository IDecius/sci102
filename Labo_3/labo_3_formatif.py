# -*- coding: utf-8 -*-
# 0. Importez numpy
import numpy as np

# Ecrivez le code qui permet de répondre aux questions suivantes. Vous pouvez répondre directement dans ce fichier.
# Utilisez numpy pour répondre à ces questions.
# Réfèrez-vous à la documentation de numpy pour vous aider dans votre démarche.

# 1. Initialisez un array numpy 1D. C'est l'équivalent d'un vecteur.
# Cette structure peut contenir ce que vous voulez.
myArray = np.array([1,2,3,4,5])
# 2. Affichez votre array à l'écran
print(myArray)

# 3. Affichez la dimension (forme) de votre array à l'écran
print(myArray.shape)

# 4. Initialisez un nouvel array numpy. Cette fois-ci 2D. C'est l'équivalent d'une matrice.
# Cette structure peut contenir les éléments que vous souhaitez mais de type float.
my2ndArray = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0], [13.0, 14.0, 15.0, 16.0]])

# 5. Affichez votre array à l'écran
print(my2ndArray)

# 6. Affichez la dimension (forme) de votre array à l'écran
print(my2ndArray.shape)

# 7. Trouvez une façon d'afficher le nombre de dimension de chacune de vos arrays.
print("Dimension de myArray:", myArray.ndim)
print("Dimension de my2ndArray:", my2ndArray.ndim)

# 8. Affichez le type des éléments se trouvant dans chacune de vos arrays
print("Type des éléments de myArray:", myArray.dtype)
print("Type des éléments de my2ndArray:", my2ndArray.dtype)

# 9. Additionner le chiffre 11 à chaque élément de votre matrice 2D créée à l'étape 4.
# Conservez le résultat de l'addition dans un nouvel array
myAddition = my2ndArray + 11

# 10. Affichez ce nouvel array à l'écran.
print(myAddition)

# 11. Multipliez pi à chaque élément de votre matrice 2D créée à l'étape 4.
# Conservez le résultat de la multiplication dans un nouvel array
myPiArray = my2ndArray * np.pi

# 12. Affichez ce nouvel array à l'écran.
print(myPiArray)

# 13. Accedez à l'élément 2 de votre array 1D et affichez le à l'écran.
print(myArray[1])

# 14. Accedez à l'élément sur la deuxième ligne et la deuxième colonne de votre array 2D et affichez le à l'écran.
print(my2ndArray[1,1])

# 15. Affichez, sans boucle for, tous les éléments de la deuxième ligne de votre array 2D.
print(my2ndArray[1,:])

# 16. Trouvez la matrice transposée de votre array 2D et
# sauvegardez le resultat dans une nouvelle matrice nommée transpose.
transpose = my2ndArray.T

# 17. Affichez, sans boucle for, tous les éléments des lignes 2 à 4 votre array 2D transpose.
print(transpose[1:4,:])

# 18. Affichez, sans boucle for, tous les éléments de la première à la troisième ligne de votre matrice 2D transpose.
print(transpose[0:3,:])

# 19. Créez une nouvelle matrice de dimension (6,6), de float. Assurez-vous qu'elle contient une variété d'éléments
# et non juste un même nombre. Affichez cettre matrice.
my6x6Array = np.abs(np.random.randn(6,6) * 10) // 1  # Création d'une matrice 6x6 avec des valeurs aléatoires
print(my6x6Array)

# 20a. Affichez tous les éléments de la première à la troisième ligne et de la troisième à la sixième colonne
# de la matrice créée en 19. Au final, une matrice de dimension (3,4) devrait être affichée.
print(my6x6Array[0:3, 2:6])

# 20b. Utilisez les indices négatifs pour afficher l'élément à l'avant dernière colonne de l'avant dernière ligne
# de la matrice créée en 19. Affichez l'élément à l'écran.
print(my6x6Array[-2,-2])

# 20c. Repérez un nombre se trouvant une ou plusieurs fois dans votre matrice créée en 19.
# Appelons ce nombre x.
# Utilisez la condition booléenne pour sélectionner tous les éléments de votre matrice qui sont égaux à x.
x = my6x6Array[0,0]
print(my6x6Array[my6x6Array == x])

# 21. Calculez en une ligne, avec numpy, la somme de tous les éléments de la matrice en 19. et affichez le résultat.
print(np.sum(my6x6Array))

# 22. Calculez en une ligne, avec numpy, la moyenne de tous les éléments de la matrice en 19. et affichez le résultat.
print(np.average(my6x6Array))

# 23. Créez vous deux arrays 2D de float avec chacune une dimension de (3,3).
# Effectuez la multiplication matricielle de ces deux arrays et affichez la matrice résultante.
# Attention! On veut ici une multiplication matrcielle : https://en.wikipedia.org/wiki/Matrix_multiplication.
myArray1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
myArray2 = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])
result = np.matmul(myArray1, myArray2)
print(result)