# ILI9225_displayio_circuitpython

A simple driver for ILI9225 TFT display (cheap display, red pcb with µsdcard reader) in 176px x 220px, for using with displayIo and tileGrid from Adafruit. I did it because the one found online was a copy of Adafruit's Arduino driver and useless for my own experiments.
Coded with ChatGPT with ST7735R driver as model.  
There is no rotation on display (TODO), and display is used in portrait mode.  
This is more an experiment with ai agent for coding driver (Mistral.ai vs Claude.ai vs ChatGPT) than a true driver. But i think this is a clean start for implement more features (please fork it!).  

There is too, given "as is", a "fast" driver version (the earlier version) who does not use displayio, and support only raw RGB565 pictures. With this driver on a RP2040, it is able to load and display 4,5 img / sec. Not so fast but faster than with displayio.

In the folder, i share the python script for encode picture files (.png, .tiff, .jpeg, .gif, .tga in the same place's script) to transform to .raw file (coded with Claude.ai)

I'm not a dev, so apology for the work.
