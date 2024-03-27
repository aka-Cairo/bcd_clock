""" main()

Copyright (C) 2023 Martin J Levy - W6LHI/G8LHI - @mahtin - https://github.com/mahtin
"""

# This is key - once done, all the imports work
import os
os.chdir('/flash')

from pico.wwvb_lite import wwvb_lite
from machine import Pin
import utime

def main():
    
    # Define the pin number
    #pin_number = 22  # This corresponds to GP22 on the Raspberry Pi Pico

    # Initialize the pin as an output
    #pin = Pin(pin_number, Pin.OUT)

    # Set the pin to high
    #pin.value(1)

    # Delay (optional)
    #utime.sleep(1)  # Sleep for 1 second to keep the pin high
    wwvb_lite()


main()
