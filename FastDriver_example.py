import board
import busio
import time
from ILI9225_Fast import ILI9225

# Configuration de l'écran
spi = busio.SPI(clock=board.GP6, MOSI=board.GP3)
cs = board.GP5
dc = board.GP7
rst = board.GP8
display = ILI9225(spi, cs=cs, dc=dc, rst=rst)

# Nom du fichier image - changez cette valeur pour votre fichier
IMAGE_FILENAME = "176_220.raw"

# Dimensions de l'écran
WIDTH = 176
HEIGHT = 220

# Définir l'orientation qui fonctionne
display.set_orientation(2)

# Afficher l'image
print(f"Affichage de l'image: {IMAGE_FILENAME}")
try:
    # Ouvrir et lire le fichier RAW
    with open(IMAGE_FILENAME, "rb") as file:
        image_data = file.read()
    
    # Configurer la fenêtre d'affichage
    display.set_window(0, 0, WIDTH-1, HEIGHT-1)
    display._write_command(0x22)
    
    # Écrire tous les pixels
    display.write_pixels(bytearray(image_data))
    print("Affichage terminé")
    
except OSError as e:
    print(f"Erreur lors de l'ouverture du fichier: {e}")
    
    # En cas d'erreur, afficher un écran rouge
    print("Affichage d'un écran rouge")
    display.set_window(0, 0, WIDTH-1, HEIGHT-1)
    display._write_command(0x22)
    line = bytearray([0xF8, 0x00] * WIDTH)  # Rouge pur RGB565
    for y in range(HEIGHT):
        display.write_pixels(line)
