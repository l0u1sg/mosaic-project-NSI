# Mosaic Project
## Introduction
Here is one of the projects we have to do in NSI (Numerical Computer Science), the Mosaic Project. The goal of this project is to create a program that will generate a mosaic of a given image. This program is written in Python and this is the structure of its files :
- The main file is called main.py. It contains the main code of the program.
- The images folder contains the images that will be used in the mosaic.
- The functions.py file contains the functions that will be used in the program.

## The different functions
The functions.py file contains the different functions that will be used in the program.
- The function `open_image()` will open an image and return it as a numpy array.
- The function `save_image()` will save an image as a .png file.
- The function `convert_to_gray()` will convert an image to grayscale.
- The function `show_image()` will display an image.
- The function `mean_value()` will return the average value of the grayscale levels of each pixel of an image
- The function `resize_folder()` will resize all the images in a folder.
- The function `resizeTo20x20()` will resize an image to 20x20 pixels.
- The function `mean_folder()` will return the average value of the grayscale levels of each pixel of all the images in a folder.
- The function `convert_to_gray_folder()` will convert all the images in a folder to grayscale.
- The function `resize_to_multiple_of_20()` will resize all the images in a folder to a multiple of 20.  

*The functions marked above are only provisional and may change by the end of the programme's production*

# The goal of the project 🏁
The goal of the project is to achieve a programme similar to this repo : https://github.com/codebox/mosaic