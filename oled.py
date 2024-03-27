from machine import Pin, I2C
from flash.pico.ssd1306 import ssd1306

i2c=I2C(0,sda=Pin(8), scl=Pin(9), freq=400000)
oled = SSD1306(128, 64, i2c)

oled.fill(1)
oled.show()

oled.text("WELCOME!", 0, 0)
oled.text("This is a text", 0, 16)
oled.text("GOOD BYE", 0, 32)
oled.show()