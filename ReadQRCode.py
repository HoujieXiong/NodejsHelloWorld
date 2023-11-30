#!/usr/bin/python3

import time
from PIL import Image
import zbarlight 

# Encode a VGA stream, and capture a higher resolution still image half way through.

while (True):
    # It's better to capture the still in this thread, not in the one driving the camera.
    #with open('test.jpg','rb') as image_file:
    try:
        image_file=Image.open("test.jpg")
        greyScale=image_file.convert('L')
        image_file.close()
        #image_file.load()
        codes=zbarlight.scan_codes(['qrcode'],greyScale)
        print("found test.jpg")
        if(codes):
            print('QR codes: %s' % codes)

            f = open("test.txt", "w")
            #f.write(codes)
            f.close()
            #open and read the file after the appending:
            f = open("test.txt", "r")
            
            print(f.read())
            f.close()
    except:
        print("Not found")
    time.sleep(0.1)
