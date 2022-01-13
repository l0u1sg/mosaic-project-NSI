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

# Calculer la valeur moyenne des niveaux de gris de chaque pixel // Calculate the average value of the grayscale levels of each pixel
def mean_value(img):
    d = {}
    mean_value = 0
    # Récupérer les dimensions de l'image dans les variable width et height // Get the dimensions of the image in the variables width and height
    width, height = img.size
    # Parcourir toutes les lignes (nombre hauteur de ligne) // Iterate through all the lines (number of lines)
    for i in range(height):
        # Parcourir chaque point de cette ligne (nombre largeur de points) // Iterate through each point of this line (number of points)
        for j in range(width):
            r,g,b = img.getpixel((j, i))
            mgris = (r + g + b) // 3
            d[mgris] = "v"+str(i)
            mean_value = mean_value + mgris
    mean = mean_value // (width * height)
    return d

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