import time

from picamera2 import Picamera2, Preview
#this will output a jepg file.
picam2 = Picamera2()

#preview_config = picam2.create_preview_configuration(main={"size": (640 , 2464)})
#picam2.configure(preview_config)

#picam2.start_preview(Preview.QTGL)

picam2.start()
while(1):
    time.sleep(0.1)
    metadata = picam2.capture_file("test.jpg")
    print(metadata)

picam2.close()