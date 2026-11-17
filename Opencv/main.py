import os
import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image_path = 'die.png'

# ÉTAPE DE SÉCURITÉ : Si l'image n'existe pas, on la crée automatiquement pour vous !
if not os.path.exists(image_path):
    print(f"L'image '{image_path}' est introuvable. Création automatique d'une image de test...")
    img_test = Image.new('RGB', (400, 400), color=(120, 180, 220))
    img_test.save(image_path)
    print("Image 'die.png' créée avec succès !")

# Chargement de l'image avec OpenCV
img_bgr = cv.imread(image_path)

if img_bgr is None:
    print(f"Erreur : Impossible de charger l'image '{image_path}'.")
    exit()

print("Image chargée avec succès ! Application du débruitage...")


dst_bgr = cv.fastNlMeansDenoisingColored(img_bgr, None, 10, 10, 7, 21)


img_rgb = cv.cvtColor(dst_bgr, cv.COLOR_BGR2RGB)


plt.figure(figsize=(6, 6))
plt.imshow(img_rgb)
plt.title("Image traitée (Débruitée)")
plt.axis('off')  

plt.show()
