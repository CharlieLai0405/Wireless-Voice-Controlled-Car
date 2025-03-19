import RPi.GPIO as GPIO
import time  
import sys  

# GPIO setting
GPIO.setmode(GPIO.BOARD)
# Motor pin setting
Motor1A = 16
Motor1B = 18
Motor2A = 23
Motor2B = 21
ENA = 12
ENB = 13

# Ultrasound pin setting
TRIG = 7
ECHO = 11

# Output setting
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
    
# PWM setting
global pwm_1, pwm_2
pwm_1 = GPIO.PWM(ENA, 100)  # Frequency 100Hz
pwm_2 = GPIO.PWM(ENB, 100)  # Frequency 100Hz
pwm_1.start(0)  # Initial speed 0
pwm_2.start(0)  # Initial speed 0

def send_trigger_pulse():
    GPIO.output(TRIG, True)
    time.sleep(0.001)
    GPIO.output(TRIG, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(ECHO) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340* 100 /2
    return distance_cm

# Signal generation
def forward():  
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_1.ChangeDutyCycle(50)
    pwm_2.ChangeDutyCycle(50) 
def backward():  
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    pwm_1.ChangeDutyCycle(50)
    pwm_2.ChangeDutyCycle(50)  
def turn_right():  
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    pwm_1.ChangeDutyCycle(20)
    pwm_2.ChangeDutyCycle(20)  
def turn_left():  
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_1.ChangeDutyCycle(20)
    pwm_2.ChangeDutyCycle(20) 
def stop():  
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_1.ChangeDutyCycle(0)
    pwm_2.ChangeDutyCycle(0)
def auto():
    while True:
        distance = get_distance()
        #print(f"Distance: {distance}")
        if distance > 30:
            forward()
            time.sleep(1)
        else:
            stop()
            time.sleep(0.5)
            print("Obstacløe detected! Turning left.")
            turn_left()
            time.sleep(0.5)
            stop()
            time.sleep(0.5)

# Command & Execute
if sys.argv[1] == "f":    
    forward()  
    print("forward")  
    time.sleep(1)  
    stop()  
if sys.argv[1] == "b":  
    backward()  
    print("backward")  
    time.sleep(1)  
    stop()  
if sys.argv[1] == "r":  
    turn_right()  
    print("turn_right")  
    time.sleep(0.5)  
    stop()  
if sys.argv[1] == "l":  
    turn_left()  
    print("turn_left")  
    time.sleep(0.5)  
    stop()  
if sys.argv[1] == "s":  
    stop()  
    print("stop")
if sys.argv[1] == "auto":
    print("Entering auto mode...")
    auto()
