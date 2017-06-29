from bibliopixel.drivers.serial.driver import TeensySmartMatrix
w = 64
h = 32
driver = TeensySmartMatrix(w, h)

import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

import bibliopixel.colors as colors

#load the LEDStrip class
from bibliopixel.layout import *
led = Matrix(driver, width = 64, height = 32, serpentine = False, threadedUpdate=True)

#load channel test animation
from bibliopixel.animation.tests import MatrixCalibrationTest
anim = MatrixCalibrationTest(led)

try:
	anim.run()
finally:
	led.all_off()
	led.update()

time.sleep(0.1)
