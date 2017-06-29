from BiblioPixelAnimations.matrix.bloom import Bloom
from BiblioPixelAnimations.matrix.Text import ScrollText
from bibliopixel.drivers.serial.driver import TeensySmartMatrix
import bibliopixel.colors as colors
from bibliopixel.layout import Matrix
import bibliopixel.log as log
import time

log.setLogLevel(log.DEBUG)

w = 64
h = 32
driver = TeensySmartMatrix(w, h)

led = Matrix(driver, width=w, height=h,
             serpentine=False, threadedUpdate=False)


# load channel test animation
# from bibliopixel.animation import MatrixCalibrationTest
# anim = MatrixCalibrationTest(led)
# anim.run(fps=30)

try:
    anim = Bloom(led)
    anim.run(amt=6, fps=10)
except:
    led.all_off()
    led.update()
    time.sleep(1)
    led.all_off()
    led.update()

# anim = ScrollText(led, "Maniacal Labs Rules!", xPos = 128, yPos = 0, color = colors.Red, bgcolor = colors.Off, size = 4)
# try:
#     anim.run(amt=6, fps=30)
# finally:
#     led.all_off()
#     led.update()
#     time.sleep(1)
#
# led.all_off()
# led.update()a
# time.sleep(1)
# led.all_off()
# led.update()
# time.sleep(1)
