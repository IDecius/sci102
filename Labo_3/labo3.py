#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Mikael Fortin and Mariane Maynard
# Description: Labo exercices created for Universite de Sherbrooke's IFT099 class
# Borrowed and adapted by Mariane Maynard for SCI102's class
#
# Copyright (c) 2015 Mikael Fortin
# All rights reserved. No warranty, explicit or implicit, provided.
#
# Copyright (c) 2022 Mariane Maynard
# All rights reserved. No warranty, explicit or implicit, provided.

# from ift099 import *
from math import *
import numpy as np


# 1a. Écrire une fonction qui calcule la moyenne d'un array numpy
# indice : vous êtes encouragés à utiliser les fonctions de la librairie
def moyenne(array):
    return np.average(array)
    
# 1b. écrire une fonction qui retourne le plus petit élément d'un array reçu en paramètre.
def pluspetit(array):
    return np.min(array)

# 2a. Écrire une fonction qui calcule le quotient et le reste de divisions.
# Vous recevez en paramètre 2 arrays numpy de même taille : les dividendes et les diviseurs
# Retournez le résultat sous forme de tuple de 2 arrays numpy
# indice : n'oubliez pas que numpy surcharge les opérateurs arithmétiques
def quotientReste(dividendes,diviseurs):
    quotient = dividendes // diviseurs
    reste = dividendes % diviseurs
    return (quotient, reste)

# Exemple d'utilisation :
quotientReste(np.array([752, 451]), np.array([95, 333]))


# 2b. Définir une fonction qui applique la fonction f(x) = x² + 5x - 4 à tous les termes d'un array numpy
def f(xs):
    return xs**2 + 5*xs - 4

# 3a. faire la somme des éléments d'un numpy array
def somme(array):
    return sum(array)

# 3b. Repérez un nombre se trouvant une ou plusieurs fois dans un array.
# Appelons ce nombre x.
# Utilisez la condition booléenne pour sélectionner tous les éléments de votre array qui sont égaux à x.
# retournez cet array
def trouverx(array, x):
    array = array[array == x]
    return array

# 4a. Multiplier une matrice reçue en paramètre par sa transposée et retourner le résultat. La fonction doit gérer
# n'importe quelle taille de matrice.
def produit_matriciel(matrice):
    return np.matmul(matrice, matrice.T)


# 4b. Calculer la norme (euclidienne) d'un vecteur reçu en paramètre https://fr.wikipedia.org/wiki/Norme_(math%C3%A9matiques).
# La fonction doit pouvoir calculer la norme peu importe le nombre de dimensions du vecteur (peut être plus grand que 3)..
def norme_vecteur(vecteur):
    return sqrt(np.matmul(vecteur, vecteur.T))

# 4c. Calculer le vecteur unitaire d'un vecteur reçu en paramètre https://fr.wikipedia.org/wiki/Vecteur_unitaire. La
# fonction doit pouvoir gérer plusieurs dimensions (potentiellement plus que 3).
def vecteur_unitaire(vecteur):
    return vecteur / sqrt(np.matmul(vecteur, vecteur.T))

# 5. Écrire une fonction qui décrit la comparaison de deux vecteurs.
# Voir https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-comparaison-entre-deux-vecteurs-m1301
# - Si les 2 vecteurs sont parallèles, de même norme et de même sens, la fonction retourne "Équipollents"
# - Si les 2 vecteurs sont perpendiculaires, la fonctione retourne "Orthogonaux"
# - Si les 2 vecteurs sont parallèles et de même norme mais qu'ils sont de sens contraire, la fonction retourne "Opposés"
# - Si les 2 vecteurs sont parallèles, (mais pas de même norme), la fonction retourne "Colinéaires"
# - Enfin, dans les autres cas, la fonctione retourne "Aucune caractéristique de comparaison notable".
# indice : vous pouvez utiliser les fonctions précédemment définies
def comparer(vecteur1, vecteur2):
    norme1 = norme_vecteur(vecteur1)
    norme2 = norme_vecteur(vecteur2)

    if norme1 < 1e-9 or norme2 < 1e-9:
        return "Un des deux vecteurs est de norme nulle"
    
    produitScalaire = np.dot(vecteur1, vecteur2)
    produitVectoriel = np.cross(vecteur1, vecteur2)

    if produitScalaire == norme1 * norme2 or produitScalaire == -norme1 * norme2:
        if produitScalaire > 0:
            return "Équipollents"
        else:
            return "Opposés"
    elif produitScalaire < 1e-9:
        return "Orthogonaux"
    elif norme_vecteur(produitVectoriel) < 1e-9:
        return "Colinéaires"

    return "Aucune caractéristique de comparaison notable"


