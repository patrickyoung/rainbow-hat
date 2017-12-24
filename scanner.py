import rainbowhat as rh
import time

LEFT = 0
RIGHT = 1  
DISPLAY_PIXELS = 7

RED = (255,0,0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (148, 0, 211)

RAINBOW_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET] 
RED_COLORS = [RED] * 7

def clear(speed=0.0):
  rh.rainbow.clear()
  rh.rainbow.show()
  time.sleep(speed)  

def show_pixel(pixel_id, color=GREEN, brightness=0.5, speed=0.5):
  rh.rainbow.set_pixel(pixel_id, color[0], color[1], color[2], brightness) 
  rh.rainbow.show()
  time.sleep(speed)
  clear()

def chaser_light(pixel_id, color=GREEN, brightness=0.5, speed=0.5):
  show_pixel(pixel_id, color, brightness, speed / 3)
  show_pixel(pixel_id, color, brightness / 10, speed / 3)
  clear(speed=speed / 3)

def wiper_light(colors, direction=RIGHT, speed=1):
  pixels = range(0,DISPLAY_PIXELS) if direction==LEFT else reversed(range(0,DISPLAY_PIXELS))
  for pixel in pixels:
    chaser_light(pixel, colors[pixel], speed=speed / (DISPLAY_PIXELS * 2))

def endless_wiper(colors=RAINBOW_COLORS, speed=0.25):
  while True:
    wiper_light(colors, direction=LEFT, speed=speed)
    wiper_light(colors, direction=RIGHT, speed=speed)



#endless_wiper(RED_COLORS, speed=2.0)
endless_wiper(RAINBOW_COLORS, speed=0.5)
