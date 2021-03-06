import ov2640
import gc
import time
import sys
from machine import SD
import os
import math

FNAME = '/sd/test.OV2640_1024x768_JPEG.jpg'#saving to SD card on expansion board
sd = SD()
os.mount(sd, '/sd')

# check the content
print(os.listdir('/sd'))
def main():
    try:
        print("initializing camera")
        #lores: OV2640_320x240_JPEG, OV2640_352x288_JPEG, OV2640_640x480_JPEG
        #hires: OV2640_1024x768_JPEG, OV2640_1280x1024_JPEG, OV2640_1600x1200_JPEG
        #cam = ov2640.ov2640(resolution=ov2640.OV2640_1600x1200_JPEG)
        cam = ov2640.ov2640(resolution=ov2640.OV2640_1024x768_JPEG)
        print(gc.mem_free())

        clen = cam.capture_to_file(FNAME, True)
        print("captured image is %d bytes" % clen)
        print("image is saved to %s" % FNAME)

        time.sleep(10)
        try:
            f = open(FNAME, "r")
            #print(f.read())
            exists = True
            print("real")
            f.close()
        except FileNotFoundError:
            exists = False
        sys.exit()

    except KeyboardInterrupt:
        print("exiting...")
        sys.exit()


if __name__ == '__main__':
    main()
