import time
import board
import busio
import digitalio

class ILI9225:
    def __init__(self, spi, cs, dc, rst=None):
        self.spi = spi

        self.cs = digitalio.DigitalInOut(cs)
        self.cs.direction = digitalio.Direction.OUTPUT
        self.cs.value = 1

        self.dc = digitalio.DigitalInOut(dc)
        self.dc.direction = digitalio.Direction.OUTPUT
        self.dc.value = 0

        self.rst = None
        if rst:
            self.rst = digitalio.DigitalInOut(rst)
            self.rst.direction = digitalio.Direction.OUTPUT
            self.rst.value = 0
            time.sleep(0.01)
            self.rst.value = 1
            time.sleep(0.05)

        self._init_display()

    def _write_command(self, cmd):
        while not self.spi.try_lock():
            pass
        #self.spi.configure(baudrate=24000000, phase=0, polarity=0)
        self.spi.configure(baudrate=8000000, phase=0, polarity=0)

        self.dc.value = 0
        self.cs.value = 0
        self.spi.write(bytes([cmd]))
        self.cs.value = 1
        self.spi.unlock()

    def _write_data(self, data):
        while not self.spi.try_lock():
            pass
        # self.spi.configure(baudrate=24000000, phase=0, polarity=0)
        self.spi.configure(baudrate=8000000, phase=0, polarity=0)

        self.dc.value = 1
        self.cs.value = 0
        self.spi.write(bytes([data]))
        self.cs.value = 1
        self.spi.unlock()

    def _write_register(self, reg, value):
        self._write_command(reg >> 8)
        self._write_command(reg & 0xFF)
        self._write_data(value >> 8)
        self._write_data(value & 0xFF)

    def _init_display(self):
        self._write_register(0x10, 0x0000)
        self._write_register(0x11, 0x0000)
        time.sleep(0.04)
        self._write_register(0x11, 0x0018)
        self._write_register(0x12, 0x6121)
        self._write_register(0x13, 0x006F)
        self._write_register(0x14, 0x495F)
        self._write_register(0x10, 0x0800)
        time.sleep(0.01)
        self._write_register(0x11, 0x103B)
        time.sleep(0.05)
        self._write_register(0x01, 0x011C)
        self._write_register(0x02, 0x0100)
        self._write_register(0x03, 0x1038)  # BGR=1, Hinc=1, Vdec=1
        self._write_register(0x07, 0x0000)
        self._write_register(0x08, 0x0808)
        self._write_register(0x0B, 0x1100)
        self._write_register(0x0C, 0x0000)
        self._write_register(0x0F, 0x0D01)
        self._write_register(0x15, 0x0020)
        self._write_register(0x20, 0x0000)
        self._write_register(0x21, 0x0000)
        self._write_register(0x36, 0x00AF)
        self._write_register(0x37, 0x0000)
        self._write_register(0x38, 0x00DB)
        self._write_register(0x39, 0x0000)
        self._write_register(0x50, 0x0000)
        self._write_register(0x51, 0x0808)
        self._write_register(0x52, 0x080A)
        self._write_register(0x53, 0x000A)
        self._write_register(0x54, 0x0A08)
        self._write_register(0x55, 0x0808)
        self._write_register(0x56, 0x0000)
        self._write_register(0x57, 0x0A00)
        self._write_register(0x58, 0x0710)
        self._write_register(0x59, 0x0710)
        self._write_register(0x07, 0x0012)
        time.sleep(0.05)
        self._write_register(0x07, 0x1017)

    def set_window(self, x0, y0, x1, y1):
        self._write_register(0x36, x1)
        self._write_register(0x37, x0)
        self._write_register(0x38, y1)
        self._write_register(0x39, y0)
        self._write_register(0x20, x0)
        self._write_register(0x21, y0)
        self._write_command(0x22)

    def write_pixels(self, buffer):
        # print("writing...")
        while not self.spi.try_lock():
            pass
#         self.spi.configure(baudrate=24000000, phase=0, polarity=0)
        self.spi.configure(baudrate=8000000, phase=0, polarity=0)
        self.dc.value = 1
        self.cs.value = 0
        self.spi.write(buffer)
        self.cs.value = 1
        self.spi.unlock()
        
    def set_orientation(self, rot):
        if rot == 0:
            self._write_register(0x03, 0x1038)  # portrait
        elif rot == 1:
            self._write_register(0x03, 0x1028)  # landscape 90°
        elif rot == 2:
            self._write_register(0x03, 0x1000)  # upside down
        elif rot == 3:
            self._write_register(0x03, 0x1018)  # landscape 270°

