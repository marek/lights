# parser for command line options
from argparse import ArgumentParser
import time
# module to control the GPIO on a raspberry pi
import RPi.GPIO as GPIO

parser = ArgumentParser()
parser.add_argument("-d", "--duration", type=int, default=30, dest="duration")

args = parser.parse_args();

# specifies that you are referring to the pins
# by the number of the pin on board.
# GPIO.BCM refers to pins by the Broadcom chip specific pin number
# which are the numbers after "GPIO" on slide #6
GPIO.setmode(GPIO.BOARD)
# set up 'pin mode' as output on all three pins
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def green():
	# setting the digital output of a pin to True
	# will drive it to 3.3V
	GPIO.output(16, True)
	# pin output is set to 0V
	GPIO.output(18, False)
	GPIO.output(22, False)
        time.sleep(max(0, args.duration - 10))

def yellow():
	GPIO.output(16, False)
	GPIO.output(18, True)
        time.sleep(10)

def red():
        GPIO.output(18, False)
	GPIO.output(22, True)

# start with green
green();

# 10 seconds before duration the user specifies ends, the yellow led will turn on
yellow();

# turn on the red led when time runs out
red();
