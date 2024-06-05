from flask import Blueprint, render_template, redirect, Response
import cv2
import time
import RPi.GPIO as GPIO
from .xaxis import rotate_clockwisez,rotate_counterclockwisez, stop_rotation, stop_rotationy, stop_rotationz, rotate_clockwise, rotate_counterclockwise, rotate_counterclockwisey, rotate_clockwisey, clamp_close, clamp_open

GPIO.setmode(GPIO.BOARD)
LimitSwitch = 40
LimitSwitchy = 16
LimitSwitchz = 18
GPIO.setup(LimitSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LimitSwitchy, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LimitSwitchz, GPIO.IN, pull_up_down=GPIO.PUD_UP)

man = Blueprint('man', __name__)

# emulated camera
from .campi_html import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

@man.route('/manual')
def manual():
    """Video streaming home page."""
    return render_template('manual.html')

#def gen(camera):
#	"""Video streaming generator function."""
#prev_frame_time = 0
#new_frame_time = 0
#
#while True:
#	new_frame_time = time.time()
#	frame = camera.get_frame()
#	fps = 1/(new_frame_time-prev_frame_time)
#	prev_frame_time = new_frame_time
#	fps = int(fps)
#	fps = str(fps)
#	frame=cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
#	yield(b'--frame\r\n' 
#	      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
prev_frame_time = 0
new_frame_time = 0
def gen(camera):
    """Video streaming generator function."""
    prev_frame_time = 0
    new_frame_time = 0
    while True:
        frame = camera.get_frame()
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps = str(fps)
#        cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@man.route('/manual/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
x_counter = 0
x_limiter = 2
y_counter = 0
y_limiter = 2
z_counter = 0
z_limiter = 1
c_counter = 0
c_limiter = 1

@man.route("/XCW/on")
def XCW_ON():
    global x_counter, x_limiter
    print("XCW_ON")
    if x_counter > 0:
        x_counter -=1
        if x_counter == 1:
            rotate_clockwise(2900)
            stop_rotation()  # Stop X motor rotation
        elif x_counter ==0:
            rotate_clockwise(1300)
            stop_rotation()  # Stop X motor rotation
    else:
        stop_rotation()
        #flash("Error",category='error')
        
    return render_template('manual.html')

@man.route("/XCW/off")
def XCW_OFF():
    print("XCW_OFF")
    stop_rotation()
    return render_template('manual.html')

@man.route("/XCCW/on")
def XCCW_ON():
    global x_counter
    print("XCCW_ON")
    if x_counter < x_limiter:
        x_counter +=1
        if x_counter == 1:
            rotate_counterclockwise(1300)
            stop_rotation()  # Stop X motor rotation
        elif x_counter == 2:
            rotate_counterclockwise(2900)
            stop_rotation()  # Stop X motor rotation
    return render_template('manual.html')

@man.route("/XCCW/off")
def XCCW_OFF():
    print("XCCW_OFF")
    stop_rotation()
    return render_template('manual.html')

@man.route("/YCW/on")
def YCW_ON():
    global y_counter
    print("YCCW_ON")
    if y_counter > 0:
        y_counter -=1
        if y_counter ==1:
            rotate_clockwisey(1600)
        elif y_counter ==0:
            rotate_clockwisey(3000)
    else:
        stop_rotationy()
    return render_template('manual.html')

@man.route("/YCW/off")
def YCW_OFF():
    print("YCW_OFF")
    stop_rotationy()
    return render_template('manual.html')

@man.route("/YCCW/on")
def YCCW_ON():
    global y_counter, y_limiter
    print("YCW_ON")
    if y_counter < y_limiter:
        y_counter +=1
        if y_counter == 1:
            rotate_counterclockwisey(3000)
        else:
            rotate_counterclockwisey(1600)
    return render_template('manual.html')

@man.route("/YCCW/off")
def YCCW_OFF():
    print("YCCW_OFF")
    stop_rotationy()
    return render_template('manual.html')

@man.route("/ZCW/on")
def ZCW_ON():
    global z_counter, z_limiter
    print("ZCW_ON")
    if z_counter < z_limiter:
        z_counter +=1
        rotate_clockwisez(20000)
    return render_template('manual.html')

@man.route("/ZCW/off")
def ZCW_OFF():
    print("ZCW_OFF")
    stop_rotationz()
    return render_template('manual.html')

@man.route("/ZCCW/on")
def ZCCW_ON():
    global z_counter
    print("ZCCW_ON")
    if z_counter > 0:
        z_counter -=1
        rotate_counterclockwisez(20000)
    else:
        stop_rotationz()
    return render_template('manual.html')

@man.route("/ZCCW/off")
def ZCCW_OFF():
    print("ZCCW_OFF")
    stop_rotationz()
    return render_template('manual.html')

@man.route("/COPEN")
def C_0PEN():
    global c_counter
    print("CLAMP OPEN")
    if c_counter > 0:
        c_counter -=1
        clamp_open()
    return render_template('manual.html')

@man.route("/CCLOSE")
def C_CLOSE():
    global c_counter, c_limiter
    print("CLAMP CLOSE")
    if c_counter < c_limiter:
        c_counter +=1
        clamp_close()
    return render_template('manual.html')

@man.route("/reset")
def reset():
    global x_counter, y_counter, z_counter, c_counter
    #if x_counter != 0:
    #    for x in range (x_counter):
    #        rotate_clockwise()
    #if y_counter != 0:
    #    for x in range (y_counter):
    #        rotate_clockwisey()
    #if z_counter != 0:
    #    for x in range (z_counter):
    #        rotate_counterclockwisez()
    #if c_counter != 0:
    #    clamp_open()
    while GPIO.input(LimitSwitchy) == 0:
        rotate_clockwisey(100)
        if GPIO.input(LimitSwitchy) == 1:
            #print("pressed")
            stop_rotationy()
            break
    
    while GPIO.input(LimitSwitch) == 0:
        rotate_clockwise(100)
        if GPIO.input(LimitSwitch) == 1:
            #print("pressed")
            stop_rotation()
            break

    while GPIO.input(LimitSwitchz) == 0:
        rotate_counterclockwisez(100)
        if GPIO.input(LimitSwitchz) == 1:
            #print("pressed")
            stop_rotationz()
            break

        
    x_counter = 0
    y_counter = 0        
    z_counter = 0            
    c_counter = 0
    return render_template('manual.html')

