from multiprocessing.connection import wait
import os
from statistics import mean
import sys
import time
from tkinter import image_types
from PIL import Image

def main(BASEDIMAGE, THUMBNAILFOLDER, IMAGE20X20FOLDER, DIM):
    """
    Main function
    """
    # Vérifier si le dossier Image20x20 existe // Check if the folder Image20x20 exists
    if not os.path.exists(IMAGE20X20FOLDER):
        print("The folder Image20x20 doesn't exist, creating it")
        # Créer le dossier Image20x20 // Create the folder Image20x20
        os.makedirs(IMAGE20X20FOLDER)
    # Vérifier si le dossier Thumbnail existe // Check if the folder Thumbnail exists
    if not os.path.exists(THUMBNAILFOLDER):
        print("Vérification du dossier Thumbnail // Check if the folder Thumbnail exists")
        sys.exit("Le dossier Thumbnail n'existe pas // The Thumbnail folder does not exist")
    # Vérifier si l'image existe // Check if the image exists
    if not os.path.exists(BASEDIMAGE):
        print("Vérification de l'image // Check if the image exists")
        sys.exit("L'image n'existe pas // The image does not exist")
    
    print("Tous les checks sont terminés, on peut commencer le traitement // All checks are completed, we can start the processing")
    print("Transformation de l'image // Transformation of the image")
    img = open_image(BASEDIMAGE)
    save_image(convert_to_gray(img), BASEDIMAGE + "_gray.jpg")
    save_image(crop_image(BASEDIMAGE + "_gray.jpg", DIM), BASEDIMAGE + "_crop.jpg")
    print("Création des miniatures de la grande image // Creation of thumbnails of the big image")
    time.sleep(5)
    cutImageInto20x20(open_image(BASEDIMAGE + "_crop.jpg"), IMAGE20X20FOLDER)
    save_image(createNewBlankImage(open_image(BASEDIMAGE + "_crop.jpg")), BASEDIMAGE + "_blank.jpg")
    print("Analyse des grandes images, cette opération peut prendre du temps // Analysis of the large images, this operation can take some time")
    time.sleep(5)
    dico_grandeImage = mean_folder(IMAGE20X20FOLDER)
    print("Analyse des miniatures, cette opération peut prendre du temps // Analysis of the thumbnails, this operation can take some time")
    time.sleep(5)
    dico_petiteImage = mean_folder(THUMBNAILFOLDER)
    print("Analyse terminée // Analysis completed")
    print("Association des miniatures avec les grandes images, cette étape peut prendre du temps // Association of thumbnails with the large images, this operation can take some time")
    time.sleep(5)
    dicoCompare = compare_dict(dico_grandeImage, dico_petiteImage)
    print("Association terminée // Association completed")
    print("Création de la mosaique // Creation of the mosaic")
    create_mosaic(dicoCompare, BASEDIMAGE + "_blank.jpg", THUMBNAILFOLDER)
    print("Mosaique créée // Mosaic created")


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
        # a = a / i
        return a
    else:
        print("You need to execute the crop_image function before the mean_value function")

# Redimensionner les images d'un dossier et le places dans un autre dossier // Resize the images of a folder and put them in another folder
def resize_folder(path_in, path_out):
    """
    Resize all the images in a folder and put them in another folder
    """
    ImageInCourse = 0
    ImageTotal = len(os.listdir(path_in))
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path_in):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path_in + file)
            print("Resize processing, " + str(ImageInCourse) + "/" + str(ImageTotal))
            # Redimensionner l'image // Resize the image
            resizeTo20x20(img, path_out + file)
            ImageInCourse = ImageInCourse + 1

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
    ImageInCourse = 0
    ImageTotal = len(os.listdir(path))
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path + file)
            print("Image processing, " + str(ImageInCourse) + "/" + str(ImageTotal))
            # Calculer la valeur moyenne des niveaux de gris de chaque pixel de l'image // Calculate the average value of the grayscale levels of each pixel of the image
            mean_value(img)
            ImageInCourse = ImageInCourse + 1
            for i in range(len(file)):
                dict_mean[file] = mean_value(img)
    return dict_mean

# Fonction pour convertir toutes les images d'un dossier en niveau de gris // Function to convert all the images of a folder to grayscale
def convert_to_gray_folder(path):
    """
    Convert all the images of a folder to grayscale
    """
    ImageInCourse = 0
    ImageTotal = len(os.listdir(path))
    # Parcourir tous les fichiers d'un dossier // Iterate through all the files of a folder
    for file in os.listdir(path):
        # Vérifier si le fichier est une image // Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png"):
            # Ouvrir l'image // Open the image
            img = open_image(path + file)
            print("Image processing, " + str(ImageInCourse) + "/" + str(ImageTotal), flush=True, end='\r')
            # Convertir l'image en niveau de gris // Convert the image to grayscale
            img_gray = convert_to_gray(img)
            # Sauvegarder l'image en niveau de gris // Save the grayscale image
            save_image(img_gray, path + file)
            ImageInCourse = ImageInCourse + 1

# Fonction pour rogner une image dans un multiple de 20 // Function to crop an image in a multiple of 20
def crop_image(img, DIM):
    """
    Crop an image in a multiple of 20
    """
    img = open_image(img)
    img_size = img.size
    w = img_size[0]
    h = img_size[1]
    c = 20
    new_w = w // c
    new_h = h // c
    margeW = w - (new_w * c)
    margeH = h - (new_h * c)
    new_img = img.crop((0, 0, w - margeW, h - margeH))
    new_img_big = new_img.resize((new_img.size[0]*DIM,new_img.size[1]*DIM))
    # return new_img
    return new_img_big

def cutImageInto20x20(img, folder):
    """
    Cut the image into several 20x20 thumbnails
    """
    (w, h) = img.size
    nbOfThumbnails = (w // 20) * (h // 20)
    for i in range(nbOfThumbnails):
        print("Cut processing, " + str(i) + "/" + str(nbOfThumbnails))
        x = i % (w // 20) * 20
        y = i // (w // 20) * 20
        img.crop((x, y, x + 20, y + 20)).save(folder + "thumbnail" + str(i) + ".jpg")

def createNewBlankImage(img):
    """
    Create a new blank image with the same size as the original image
    """
    (w, h) = img.size
    new_img = Image.new("RGB", (w, h), (255, 255, 255))
    return new_img

# Fonction qui compare chaque élements du dictionnaire de la grande image et trouve la valeur la plus proche dans la liste des vignettes // Function that compares each element of the dictionary of the large image and finds the value closest to the list of thumbnails
def compare_dict(dict_mean, dict_thumbnail):
    """
    Compare each element of the dictionary of the large image and finds the value closest to the list of thumbnails
    """
    dict_compare = {}
    ImageCourse = 0
    ImageTotal = len(dict_mean)
    for key, value in dict_mean.items():
        print("Compare processing, " + str(ImageCourse) + "/" + str(ImageTotal))
        dict_compare[key] = min(dict_thumbnail, key=lambda k: abs(dict_thumbnail[k] - value))
        ImageCourse = ImageCourse + 1
    return dict_compare

# Fonction pour créer la mosaïque qui prends en paramètre le dictionnaire dict_compare, l'image vierge, le dossier des vignettes. La fonction crée ensuite la mosaique en placant sur l'image vierge les vignettes de 20x20 correspondantes à la thumbnails de la grande image // Function to create the mosaic that takes as parameter the dictionary dict_compare, the blank image, the folder of thumbnails. The function creates then the mosaic by placing on the blank image the thumbnails of 20x20 corresponding to the thumbnails of the large image
def create_mosaic(dict_compare, img, folder_vignette):
    """
    Create the mosaic by placing on the blank image the thumbnails of 20x20 corresponding to the thumbnails of the large image
    """
    img = open_image(img)
    (w, h) = img.size
    countW = 0
    countH = 0
    count = 0
    ImageCourse = 0
    ImageTotal = len(dict_compare)
    for key, value in dict_compare.items():
        print("Mosaic processing, " + str(ImageCourse) + "/" + str(ImageTotal))
        img_vignette = open_image(folder_vignette + dict_compare["thumbnail" + str(count) + ".jpg"])
        img.paste(img_vignette, (countW * 20, countH * 20))
        countW = countW + 1
        if countW == (w // 20):
            countW = 0
            countH = countH + 1
        ImageCourse = ImageCourse + 1
        count = count + 1
    img.save("mosaic.jpg")
    

