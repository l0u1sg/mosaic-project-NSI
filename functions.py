import os
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

# Calculer la valeur moyenne des niveaux de gris de chaque pixel d'une image et enregistrer la valeur dans un dictionnaire // Calculate the average value of the grayscale levels of each pixel of an image and save the value in a dictionary
def mean_value(img):
    """
    Calculate the average value of the grayscale levels of each pixel of an image
    """
    # Dictionnaire pour stocker la valeur moyenne des niveaux de gris de chaque pixel de l'image // Dictionary to store the average value of the grayscale levels of each pixel of the image
    mean_dict = {}
    # Parcourir tous les pixels de l'image // Iterate through all the pixels of the image
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # Récupérer la valeur du pixel // Get the pixel value
            pixel = img.getpixel((x,y))
            # Vérifier si la valeur du pixel est déjà dans le dictionnaire // Check if the pixel value is already in the dictionary
            if pixel in mean_dict:
                # Ajouter 1 au compteur de la valeur du pixel // Add 1 to the counter of the pixel value
                mean_dict[pixel] += 1
            else:
                # Ajouter la valeur du pixel au dictionnaire // Add the pixel value to the dictionary
                mean_dict[pixel] = 1
    # Parcourir le dictionnaire pour calculer la valeur moyenne des niveaux de gris de chaque pixel // Iterate through the dictionary to calculate the average value of the grayscale levels of each pixel
    for key, value in mean_dict.items():
        # Calculer la valeur moyenne des niveaux de gris de chaque pixel // Calculate the average value of the grayscale levels of each pixel
        mean_dict[key] = key / value
    # Afficher la valeur moyenne des niveaux de gris de chaque pixel // Display the average value of the grayscale levels of each pixel
    print(mean_dict)

# Redimensionner les images d'un dossier et le places dans un autre dossier // Resize the images of a folder and put them in another folder
def resize_folder(path_in, path_out):
    """
    Resize all the images in a folder and put them in another folder
    """
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path_in):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path_in + file)
            # Redimensionner l'image // Resize the image
            resizeTo20x20(img, path_out + file)

def resizeTo20x20(img, name):
    """
    Resize an image to 20x20 pixels
    """
    img = img.resize((20,20))
    save_image(img, name)

# Fonction pour calculer la valeur moyenne des niveaux de gris de chaque pixel des images d'un dossier // Function to calculate the average value of the grayscale levels of each pixel of the images of a folder
def mean_folder(path):
    """
    Calculate the average value of the grayscale levels of each pixel of the images of a folder
    """
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path + file)
            # Calculer la valeur moyenne des niveaux de gris de chaque pixel de l'image // Calculate the average value of the grayscale levels of each pixel of the image
            mean_value(img)
# Fonction pour convertir toutes les images d'un dossier en niveau de gris // Function to convert all the images of a folder to grayscale
def convert_to_gray_folder(path):
    """
    Convert all the images of a folder to grayscale
    """
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path + file)
            # Convertir l'image en niveau de gris // Convert the image to grayscale
            img_gray = convert_to_gray(img)
            # Sauvegarder l'image en niveau de gris // Save the grayscale image
            save_image(img_gray, path + file)

# Fonction pour rogner une image dans un multiple de 20 // Function to crop an image in a multiple of 20
def crop_image(img):
    """
    Crop an image in a multiple of 20
    """
    # Calculer la taille de l'image // Calculate the size of the image
    size = img.size
    # Calculer la taille de l'image en niveau de gris // Calculate the size of the image in grayscale
    size_gray = img.convert('L').size
    # Calculer la taille de l'image en niveau de gris en fonction de la taille de l'image // Calculate the size of the grayscale image in function of the size of the image
    size_gray = (size_gray[0] // 20, size_gray[1] // 20)
    # Calculer la taille de l'image en fonction de la taille de l'image en niveau de gris // Calculate the size of the image in function of the size of the grayscale image
    size = (size[0] // 20, size[1] // 20)
    # Calculer la taille de l'image en fonction de la taille de l'image en niveau de gris // Calculate the size of the image in function of the size of the grayscale image
    img = img.resize(size)
    # Calculer la taille de l'image en niveau de gris en fonction de la taille de l'image // Calculate the size of the grayscale image in function of the size of the image
    img_gray = img.convert('L').resize(size_gray)
    # Sauvegarder l'image // Save the image
    return img_gray