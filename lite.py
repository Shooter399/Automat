import sys
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

chan = pca.channels[0]
my_servo = servo.Servo(chan, min_pulse=600, max_pulse=2400)