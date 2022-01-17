# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:28:21 2022

@author: Louis & Damien & GitHub Copilot
"""

# Importation des modules 
from final_preliminar_exo import *
from functions import *

resize_folder("image/", "mosaic-test/")
convert_to_gray_folder("mosaic-test/")
mean_folder("mosaic-test/")
newIMG = resize_to_multiple_of_20("tim-cook.jpg")
open_image(newIMG)