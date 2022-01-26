import os
from statistics import mean
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

# Calcule la valeur moyenne des niveaux de gris par bloc de 20x20 pixels et range cette valeur dans un dictionnaire // Calculate the average value of the grayscale levels by block of 20x20 pixels and range this value in a dictionary
def mean_value(img):
    """
    Calcule la valeur moyenne des niveaux de gris par bloc de 20x20 pixels // Calculate the average value of the grayscale levels of each pixel of a 20x20 pixel block
    """
    w = img.width
    h = img.height
    image_dict = {}
    if w == 20 and h == 20:
        for x in range(w):
            for y in range(h):
                pixel = img.getpixel((x, y))
                image_dict[(x, y)] = pixel
        a = 0
        for i in image_dict.values():
            a = a + i  
        a = a / i
        return a
    else:
        print("Pas vignette")

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
    dict_mean = {}
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path + file)
            # Calculer la valeur moyenne des niveaux de gris de chaque pixel de l'image // Calculate the average value of the grayscale levels of each pixel of the image
            mean_value(img)
            for i in range(len(file)):
                dict_mean[file] = mean_value(img)
    return dict_mean

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
    img_size = img.size
    w = img_size[0]
    h = img_size[1]
    c = 20
    new_w = w // c
    new_h = h // c
    margeW = w - (new_w * c)
    margeH = h - (new_h * c)
    new_img = img.crop((0, 0, w - margeW, h - margeH))
    return new_img
