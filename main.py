# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:28:21 2022

@author: Louis & Damien & GitHub Copilot
"""

# Importation des modules via le fichier final_preliminar_exo.py & Pillow
from final_preliminar_exo import *
from PIL import Image

# Fonction pour ouvrir une image avec pillow // Function to open an image with pillow
def open_image(path):
    img = Image.open(path)
    return img

# Fonction pour sauvegarder une image avec pillow // Function to save an image with pillow
def save_image(img, path):
    img.save(path)

# Fonction pour convertir une image en niveau de gris // Function to convert an image to grayscale
def convert_to_gray(img):
    img_gray = img.convert('L')
    return img_gray

# Fonction pour afficher une image // Function to display an image
def show_image(img):
    img.show()

# Calculer la valeur moyenne des niveaux de gris de chaque pixel // Calculate the average value of the grayscale levels of each pixel
def mean_value(img):
    mean_value = 0
    # Récupérer les dimensions de l'image dans les variable width et height // Get the dimensions of the image in the variables width and height
    width, height = img.size
    # Parcourir toutes les lignes (nombre hauteur de ligne) // Iterate through all the lines (number of lines)
    for i in range(height):
        # Parcourir chaque point de cette ligne (nombre largeur de points) // Iterate through each point of this line (number of points)
        for j in range(width):
            r,g,b = img.getpixel((j, i))
            mgris = (r + g + b) // 3
            mean_value = mean_value + mgris
    mean = mean_value // (width * height)
    return mean

dico = mean_value(open_image("smiley.png"))
print(dico)