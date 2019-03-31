#!/usr/bin/env python3
'''
If you delete training images this script will delete the json file
'''
import os
import glob
import json

for file in glob.glob('*.json'):
    with open(file, 'r') as fh:
        data = json.load(fh)
        if ('cam/image_array' in data.keys()):
            image = data['cam/image_array']
            if not os.path.isfile(image):
                print("Json File: " + file + " image: " + image + " File does not exist\n")
                os.remove(file)
