from argparse import ArgumentParser
import threading
import RPi.GPIO as GPIO

parser = ArgumentParser()
parser.add_argument("-d", "--duration", type=int, default=30, dest="duration")

args = parser.parse_args();


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def start():
	GPIO.output(16, True)
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


