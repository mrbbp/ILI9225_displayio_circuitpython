import board
import displayio
import digitalio
import busio
from ili9225_displayio import ILI9225
import adafruit_imageload

# Activer displayio (inutile dans versions récentes, mais safe)
displayio.release_displays()

# SPI & écran
spi = busio.SPI(clock=board.GP6, MOSI=board.GP3)

# spi = busio.SPI(clock=board.GP6, MOSI=board.GP3)
# cs = board.GP5
# dc = board.GP7
# rst = board.GP8

display_bus = displayio.FourWire(
    spi,
    command=board.GP7,         # <-- directement la pin ici
    chip_select=board.GP5,
    reset=board.GP8
)
display = ILI9225(
    display_bus,
    width=176,
    height=220
)


# Charger un PNG (image en palette ou 8-bit max)
bitmap, palette = adafruit_imageload.load(
    "176_220.png",  # Chemin vers l’image PNG
    bitmap=displayio.Bitmap,
    palette=displayio.Palette
)

# Créer un TileGrid
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.root_group = group

# Loop forever so you can enjoy your image
while True:
    pass

# import board
# import displayio
# import busio
# from ili9225_displayio import ILI9225
# 
# displayio.release_displays()
# 
# spi = busio.SPI(clock=board.GP6, MOSI=board.GP3)
# 
# display_bus = displayio.FourWire(
#     spi,
#     command=board.GP7,
#     chip_select=board.GP5,
#     reset=board.GP8
# )
# 
# display = ILI9225(display_bus, width=176, height=220)
# 
# bitmap = displayio.Bitmap(100, 100, 1)
# palette = displayio.Palette(1)
# palette[0] = 0x0000FF  # Bleu
# 
# tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=10, y=10)
# group = displayio.Group()
# group.append(tile_grid)
# display.root_group = group
# 
# while True:
#     pass
