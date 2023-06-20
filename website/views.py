#Home page blueprint

import cv2
from flask import Blueprint, render_template, Response
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# Function to capture video frames
def capture_frames():
    camera = cv2.VideoCapture(0)  # Use the appropriate camera index if multiple cameras are available
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #640
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #480

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break

        # Yield the resulting image frame
        yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n'

    # Release the camera
    camera.release()

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/video_feed')
@login_required
def video_feed():
    return Response(capture_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
