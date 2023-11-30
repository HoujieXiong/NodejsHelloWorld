#!/usr/bin/python3

import time
from PIL import Image
import zbarlight 

# Encode a VGA stream, and capture a higher resolution still image half way through.

while (True):
    # It's better to capture the still in this thread, not in the one driving the camera.
    #with open('test.jpg','rb') as image_file:
    image_file=Image.open("test.jpg")
    image_file=image_file.convert('L')
    #image_file.load()
    
    time.sleep(0.5)
    codes=zbarlight.scan_codes(['qrcode'],image_file)
    print('QR codes: $s' % codes)

    f = open("test.txt", "w")
    #f.write(codes)
    f.close()

    #open and read the file after the appending:
    f = open("test.txt", "r")
    print(f.read())
