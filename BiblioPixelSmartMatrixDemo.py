#from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.serial.driver import *
#driver = DriverSerial(type = LEDTYPE.GENERIC, num = 32*32, hardwareID = "16C0:0483", dev="")
driver = Serial(ledtype = LEDTYPE.GENERIC, num = 32*32, hardwareID = "16C0:0483", dev="")

import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

import bibliopixel.colors as colors

#load the LEDStrip class
#from bibliopixel.led import *
from bibliopixel.layout import *
#led = LEDMatrix(driver, serpentine = False, threadedUpdate=True)
led = Matrix(driver, width = 32, height = 32, serpentine = False, threadedUpdate=True)

#load channel test animation
#from bibliopixel.animation import MatrixCalibrationTest
from bibliopixel.animation.tests import MatrixCalibrationTest
anim = MatrixCalibrationTest(led)

try:
	anim.run()
finally:
	led.all_off()
	led.update()

time.sleep(0.1)
