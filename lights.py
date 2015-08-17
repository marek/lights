# parser for command line options
from argparse import ArgumentParser
import threading
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

def start():
	# setting the digital output of a pin to True
	# will drive it to 3.3V
	GPIO.output(16, True)
	# pin output is set to 0V
	GPIO.output(18, False)
	GPIO.output(22, False)

def yellow():
	GPIO.output(16, False)
	GPIO.output(18, True)

def stop():
	GPIO.output(18, False)
	GPIO.output(22, True)

start();

t1 = threading.Timer(min(args.duration, args.duration-10), yellow).start()
t2 = threading.Timer(args.duration, stop).start()


