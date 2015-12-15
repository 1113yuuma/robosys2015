#!/usr/bin/env python
#coding: UTF-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

while 1:
	ch = input()

	if ch == "w":
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
	elif ch == "s":
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
	elif ch == "d":
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
	elif ch == "a":
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
	elif ch == "x":
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.HIGH)
	elif ch == "b":
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.HIGH)
		break

GPIO.cleanup()
