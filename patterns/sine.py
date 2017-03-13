#this file contains sinusoidal patterns, e.g. sinewave (although this is not a
#   true sine wave)

#import points list, time.sleep, and fundamental plotting functions
from core import points
from time import sleep
from plot import *

#makes a pseudo-sinusoidal pattern; this will probably use real sines
#   eventually, but for now it's hardcoded (which makes it unbelievably long,
#   sorry about that)
#has variants 'sine', 'worm', and 'bounce'
def sinewave(variant="sine", times=1, speed=0.075):
    for t in range(times):
        if variant == "sine":
            if t==0:
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 2)
                plotFill(0, 1, 3, 3, 1, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 1)
                plotFill(0, 1, 2, 3, 1, 2)
                plotFill(0, 2, 3, 3, 2, 3)
                sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            
            if t==(times-1):
                plotFill(0, 1, 0, 3, 1, 0)
                plotFill(0, 0, 1, 3, 0, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 3)
                sleep(speed)
            
            else:
                plotFill(0, 1, 0, 3, 1, 0)
                plotFill(0, 0, 1, 3, 0, 2)
                plotFill(0, 1, 3, 3, 1, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 1)
                plotFill(0, 1, 2, 3, 1, 2)
                plotFill(0, 2, 3, 3, 2, 3)
                sleep(speed)
            
        elif variant == "worm":
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 0, 1, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
            
        elif variant == "bounce":
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 2)
            plotFill(3, 1, 0, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 0, 1, 3, 0, 3)
            sleep(speed)
