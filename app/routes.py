from flask import render_template, request
import board
import neopixel
import time
from rpi_ws281x import *
import argparse

from app import app

#LED strip configuration:
LED_COUNT      = 300    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()

def ledcolor(strip, color):
    strip.fill(color, 0, strip.numPixels())
    strip.show()

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        color = request.form["colorChange"]
        if color == "colorpicker": 
            print(hex_to_rgb(request.form.get('colorpicker')))
            ledcolor(strip, Color(hex_to_rgb(request.form.get('colorpicker'))[0], hex_to_rgb(request.form.get('colorpicker'))[1], hex_to_rgb(request.form.get('colorpicker'))[2])) 
            return render_template("home.html")
        if color == "clearLED":
            ledcolor(strip, Color(0,0,0))
            return render_template("home.html")
        if color == "red":
            ledcolor(strip, Color(255,0,0))
            return render_template("home.html")
    else:
        return render_template("home.html")