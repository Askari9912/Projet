import os
from PIL import Image, ImageFilter


image_path = "test.jpg"

if not os.path.exists(image_path):
    print(f"L'image '{image_path}' est introuvable. Création automatique d'une image de test...")
    img_test = Image.new("RGB", (400, 400), color=(70, 130, 180))
    img_test.save(image_path)
    print("Image 'test.jpg' créée avec succès !")


img = Image.open(image_path)


img_gray = img.convert("L")
img_gray.save("resultat_noir_et_blanc.jpg")
print("1. Filtre Noir et Blanc appliqué (sauvegardé sous resultat_noir_et_blanc.jpg)")

img_blur = img.filter(ImageFilter.GaussianBlur(radius=5))
img_blur.save("resultat_flou.jpg")
print("2. Filtre Flou appliqué (sauvegardé sous resultat_flou.jpg)")


img_contours = img.filter(ImageFilter.FIND_EDGES)
img_contours.save("resultat_contours.jpg")
print("3. Filtre Contours appliqué (sauvegardé sous resultat_contours.jpg)")


img_blur.show()
