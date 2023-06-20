from flask import Blueprint, render_template, redirect

man = Blueprint('man', __name__)

@man.route("/manual")
def manual():
    return render_template('manual.html')

@man.route("/XCW/on")
def XCW_ON():
    print("XCW_ON")
    # Perform actions for XCW ON
    return render_template('manual.html')

@man.route("/XCW/off")
def XCW_OFF():
    print("XCW_OFF")
    # Perform actions for XCW OFF
    return render_template('manual.html')

@man.route("/XCCW/on")
def XCCW_ON():
    print("XCCW_ON")
    # Perform actions for XCCW ON
    return render_template('manual.html')

@man.route("/XCCW/off")
def XCCW_OFF():
    print("XCCW_OFF")
    # Perform actions for XCCW OFF
    return render_template('manual.html')

@man.route("/YCW/on")
def YCW_ON():
    print("YCW_ON")
    # Perform actions for YCW ON
    return render_template('manual.html')

@man.route("/YCW/off")
def YCW_OFF():
    print("YCW_OFF")
    # Perform actions for YCW OFF
    return render_template('manual.html')

@man.route("/YCCW/on")
def YCCW_ON():
    print("YCCW_ON")
    # Perform actions for YCCW ON
    return render_template('manual.html')

@man.route("/YCCW/off")
def YCCW_OFF():
    print("YCCW_OFF")
    # Perform actions for YCCW OFF
    return render_template('manual.html')

@man.route("/ZCW/on")
def ZCW_ON():
    print("ZCW_ON")
    # Perform actions for ZCW ON
    return render_template('manual.html')

@man.route("/ZCW/off")
def ZCW_OFF():
    print("ZCW_OFF")
    # Perform actions for ZCW OFF
    return render_template('manual.html')

@man.route("/ZCCW/on")
def ZCCW_ON():
    print("ZCCW_ON")
    # Perform actions for ZCCW ON
    return render_template('manual.html')

@man.route("/ZCCW/off")
def ZCCW_OFF():
    print("ZCCW_OFF")
    # Perform actions for ZCCW OFF
    return render_template('manual.html')

