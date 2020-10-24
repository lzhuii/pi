#!/usr/bin/env python3
from bottle import get, post, run, request, template
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
IN1_PIN1 = 19
IN2_PIN1 = 16
IN1_PIN2 = 20
IN2_PIN2 = 26

GPIO.setup(IN1_PIN1, GPIO.OUT)
p1 = GPIO.PWM(IN1_PIN1, 50)  # 这里的50是频率为50Hz
p1.start(0)

GPIO.setup(IN2_PIN1, GPIO.OUT)
p2 = GPIO.PWM(IN2_PIN1, 50)
p2.start(0)

GPIO.setup(IN1_PIN2, GPIO.OUT)
p3 = GPIO.PWM(IN1_PIN2, 50)
p3.start(0)

GPIO.setup(IN2_PIN2, GPIO.OUT)
p4 = GPIO.PWM(IN2_PIN2, 50)
p4.start(0)

# 可以通过更改括号内的数值改变电机转动的速度，数值范围0~100


def forward(time_sleep):
    p1.start(50)
    p2.start(0)
    p3.start(50)
    p4.start(0)
    time.sleep(time_sleep)


def down(time_sleep):
    p1.start(0)
    p2.start(50)
    p3.start(0)
    p4.start(50)
    time.sleep(time_sleep)


def left(time_sleep):
    p1.start(50)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)


def right(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(50)
    p4.start(0)
    time.sleep(time_sleep)


def stop(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)


@get("/")
def index():
    return template("index")


@post("/cmd")
def cmd():
    print("按下了按钮: "+request.body.read().decode())
    sleep_time = 1
    arg = request.body.read().decode()
    if(arg == 'up'):
        forward(sleep_time)
    elif(arg == 'down'):
        down(sleep_time)
    elif(arg == 'left'):
        left(sleep_time)
    elif(arg == 'right'):
        right(sleep_time)
    elif(arg == 'stop'):
        stop(sleep_time)
    else:
        return False


if __name__ == "__main__":
    run(host="0.0.0.0", port="80")
