import RPi.GPIO as GPIO
import sys
import select
import termios
import tty
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define motor pins
motor1pin1 = 16  # BOARD number for BCM 23
motor1pin2 = 18  # BOARD number for BCM 24
motor2pin1 = 11  # BOARD number for BCM 17
motor2pin2 = 13  # BOARD number for BCM 27

# Setup GPIO pins
GPIO.setup(motor1pin1, GPIO.OUT)
GPIO.setup(motor1pin2, GPIO.OUT)
GPIO.setup(motor2pin1, GPIO.OUT)
GPIO.setup(motor2pin2, GPIO.OUT)

# Motor control functions
def move_forward():
    GPIO.output(motor1pin1, GPIO.HIGH)
    GPIO.output(motor2pin2, GPIO.HIGH)
    GPIO.output(motor1pin2, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.LOW)

def move_backward():
    GPIO.output(motor1pin1, GPIO.LOW)
    GPIO.output(motor2pin2, GPIO.LOW)
    GPIO.output(motor1pin2, GPIO.HIGH)
    GPIO.output(motor2pin1, GPIO.HIGH)

def steer_left():
    GPIO.output(motor1pin1, GPIO.HIGH)
    GPIO.output(motor2pin1, GPIO.LOW)

def steer_right():
    GPIO.output(motor1pin1, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.HIGH)

def stop_car():
    GPIO.output(motor1pin1, GPIO.LOW)
    GPIO.output(motor1pin2, GPIO.LOW)
    GPIO.output(motor2pin1, GPIO.LOW)
    GPIO.output(motor2pin2, GPIO.LOW)

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin.fileno())

    while True:
        if is_data():
            c = sys.stdin.read(1)
            if c == 'w':
                move_forward()
            elif c == 's':
                move_backward()
            elif c == 'a':
                steer_left()
            elif c == 'd':
                steer_right()
            elif c == '\x1b':  # x1b is ESC
                break
        else:
            stop_car()
        time.sleep(0.1)
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    GPIO.cleanup()
