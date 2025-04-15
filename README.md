# ILI9225_displayio_circuitpython

a simple driver for ILI9225 TFT display, for using with displayIo and tileGrid from adafruit, because the one found online was useless.
Coded with ChatGPT with ST7735R driver as model.  
There is no rotation added, and display is in portrait mode.  
This is more an experiment with ai agent (Mistral.ai vs Claude.ai vs ChatGPT) than a true driver. But i think this is a clean start for implement more features.  

There is too, as is, a "fast" driver version (the earlier version) who does not use displayio, and support only raw RGB565 pictures. with it with a RP2040, it is able to load and display 4,5 img / sec. Not so fast but faster than with displayio.

In folder, i put the python script for encode picture files (.png, .tiff, .jpeg, .gif, .tga) in the same place as the script to transform to .raw file (coded with claude.ai)
