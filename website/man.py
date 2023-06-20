#import RPi.GPIO as GPIO
from flask import Blueprint, redirect, request

# GPIO.setmode(GPIO.BCM)

man = Blueprint('man', __name__)

# pins = {
#    23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
#    24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
# }

# for pin in pins:
#    GPIO.setup(pin, GPIO.OUT)
#    GPIO.output(pin, GPIO.LOW)


@man.route("/XCW", methods=["GET", "POST"])
def XCW():
    if request.method == "POST":
        print("XCW_ON")
        # GPIO.output(23, GPIO.HIGH)
    else:
        print("XCW_OFF")
        # GPIO.output(23, GPIO.LOW)
    return redirect("/manual")


@man.route("/XCCW", methods=["GET", "POST"])
def XCCW():
    if request.method == "POST":
        print("XCCW_ON")
        # GPIO.output(24, GPIO.HIGH)
    else:
        print("XCCW_OFF")
        # GPIO.output(24, GPIO.LOW)
    return redirect("/manual")


@man.route("/YCW", methods=["GET", "POST"])
def YCW():
    if request.method == "POST":
        print("YCW_ON")
        # GPIO.output(23, GPIO.HIGH)
    else:
        print("YCW_OFF")
        # GPIO.output(23, GPIO.LOW)
    return redirect("/manual")


@man.route("/YCCW", methods=["GET", "POST"])
def YCCW():
    if request.method == "POST":
        print("YCCW_ON")
        # GPIO.output(24, GPIO.HIGH)
    else:
        print("YCCW_OFF")
        # GPIO.output(24, GPIO.LOW)
    return redirect("/manual")


@man.route("/ZCW", methods=["GET", "POST"])
def ZCW():
    if request.method == "POST":
        print("ZCW_ON")
        # GPIO.output(23, GPIO.HIGH)
    else:
        print("ZCW_OFF")
        # GPIO.output(23, GPIO.LOW)
    return redirect("/manual")


@man.route("/ZCCW", methods=["GET", "POST"])
def ZCCW():
    if request.method == "POST":
        print("ZCCW_ON")
        # GPIO.output(24, GPIO.HIGH)
    else:
        print("ZCCW_OFF")
        # GPIO.output(24, GPIO.LOW)
    return redirect("/manual")