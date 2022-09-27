#!/usr/bin/python3

import os
import datetime
import time
import picamera
import subprocess

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1640, 1232)

now = datetime.datetime.now().isoformat()
filename = '/var/www/html/{}_maison.jpg'.format(now)

camera.capture(filename, quality=30)

os.system('cp {} /var/www/html/latest.jpg'.format(filename))

camera.close()
