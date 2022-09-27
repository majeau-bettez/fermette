#!/bin/bash

killall camera_surveillance

/home/pi/take_picture.py

/home/pi/camera_surveillance.py &
