import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

# Initialize I2C and PCA9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

# Configure servo on channel 0
chan = pca.channels[0]
my_servo = servo.Servo(chan, min_pulse=600, max_pulse=2400)

# Move servo back and forth
while True:
    for angle in range(0, 181, 5):
        my_servo.angle = angle
        time.sleep(0.02)

    for angle in range(180, -1, -5):
        my_servo.angle = angle
        time.sleep(0.02)