#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de conversion d'images en format RGB565 RAW
Compatible avec les écrans comme ILI9225
"""

import os
import sys
import glob
from PIL import Image

# Taille de redimensionnement par défaut
DEFAULT_WIDTH = 176
DEFAULT_HEIGHT = 220

def convert_to_rgb565(input_file, output_dir, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    """Convertit une image en format RGB565 RAW pour écrans embarqués"""
    filename = os.path.basename(input_file)
    name = os.path.splitext(filename)[0]
    output_file = os.path.join(output_dir, f"{name}.raw")

    print(f"Conversion de {input_file} vers {output_file}")

    try:
        # Ouvrir et redimensionner l'image
        img = Image.open(input_file).convert("RGB")
        img = img.resize((width, height))

        # Créer le fichier de sortie
        with open(output_file, "wb") as f:
            # Convertir chaque pixel en RGB565 (16 bits, format big-endian)
            for y in range(img.height):
                for x in range(img.width):
                    r, g, b = img.getpixel((x, y))
                    # Conversion en RGB565: RRRRRGGG GGGBBBBB
                    rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                    # Écriture big-endian (octet de poids fort en premier)
                    f.write(bytes([rgb565 >> 8, rgb565 & 0xFF]))

        print(f"Conversion terminée: {output_file}")
        return True

    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return False

def main():
    """Fonction principale"""
    # Déterminer le répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Travail dans le répertoire: {script_dir}")

    # Créer le répertoire de sortie s'il n'existe pas
    output_dir = os.path.join(script_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Extensions d'images prises en charge
    extensions = ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.tiff", "*.tif", "*.tga"]

    # Trouver toutes les images dans le répertoire
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(script_dir, ext)))

    if not image_files:
        print("Aucune image trouvée dans le répertoire.")
        return

    print(f"Début de la conversion des images en RGB565...")

    # Convertir chaque image
    for img_file in image_files:
        convert_to_rgb565(img_file, output_dir)

    print("Toutes les conversions sont terminées.")
    print(f"Les fichiers RAW ont été enregistrés dans: {output_dir}")

if __name__ == "__main__":
    main()
