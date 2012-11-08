#!/usr/bin/python
from pynotify import *
import sys
#import os

def notify(message=""):
    n = Notification("New Mail for you Feni!", message)
    n.show()

notify()
#cmd = 'aplay /path/to/mysound.wav'
#os.system(cmd)

