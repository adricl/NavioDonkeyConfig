#!/usr/bin/env python3
'''
If you delete training images this script will delete the json file
'''
import os
import sys
import glob
import json

args = sys.argv[:]
directory = args[1]


for file in glob.glob(directory + '*.json'):
    with open(file, 'r') as fh:
        data = json.load(fh)
        if ('cam/image_array' in data.keys()):
            image = data['cam/image_array']
            if not os.path.isfile(directory + image):
                print("Json File: " + file + " image: " + image + " File does not exist\n")
                os.remove(file)

# Filters throttles in reverse to 0 throttle
for file in glob.glob(directory + '*.json'):
    with open(file, 'r') as fh:
        data = json.load(fh)
        if ('cam/image_array' in data.keys()):
            throttle = float(data['user/throttle'])
            if (throttle < 0):
                image = data['cam/image_array']
                print("Json File: " + file + " image: " + directory + image + " Throttle Less than 0\n")
                os.remove(file)
                os.remove(directory + image)