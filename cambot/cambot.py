# sudo python cambot.py
# Imports
import webiopi

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Left motor GPIOs
L1=23  # IN4
L2=24  # IN3

# Right motor GPIOs
R1=25 # IN2
R2=8  # IN1

# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #

def go_forward():
    GPIO.output(R2, GPIO.HIGH)  # IN1
    GPIO.output(R1, GPIO.LOW)   # IN2
    GPIO.output(L2, GPIO.HIGH)  # IN3
    GPIO.output(L1, GPIO.LOW)   # IN4

def go_backward():
    GPIO.output(R2, GPIO.LOW)  # IN1
    GPIO.output(R1, GPIO.HIGH)   # IN2
    GPIO.output(L2, GPIO.LOW)  # IN3
    GPIO.output(L1, GPIO.HIGH)   # IN4

def turn_left():
    GPIO.output(R2, GPIO.LOW)  # IN1
    GPIO.output(R1, GPIO.HIGH)   # IN2
    GPIO.output(L2, GPIO.HIGH)  # IN3
    GPIO.output(L1, GPIO.LOW)   # IN4

def turn_right():
    GPIO.output(R2, GPIO.HIGH)  # IN1
    GPIO.output(R1, GPIO.LOW)   # IN2
    GPIO.output(L2, GPIO.LOW)  # IN3
    GPIO.output(L1, GPIO.HIGH)   # IN4

def stop():
    GPIO.output(R2, GPIO.LOW)  # IN1
    GPIO.output(R1, GPIO.LOW)   # IN2
    GPIO.output(L2, GPIO.LOW)  # IN3
    GPIO.output(L1, GPIO.LOW)   # IN4

    
# -------------------------------------------------- #
# Initialization part                                #
# -------------------------------------------------- #

# Setup GPIOs
GPIO.setFunction(L1, GPIO.OUT)
GPIO.setFunction(L2, GPIO.OUT)
GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(R2, GPIO.OUT)

stop()

# -------------------------------------------------- #
# Main server part                                   #
# -------------------------------------------------- #


# Instantiate the server on the port 8000, it starts immediately in its own thread
server = webiopi.Server(port=8000, login="pi", password="7895123")

# Register the macros so you can call it with Javascript and/or REST API

server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)

# -------------------------------------------------- #
# Loop execution part                                #
# -------------------------------------------------- #

# Run our loop until CTRL-C is pressed or SIGTERM received
webiopi.runLoop()

# -------------------------------------------------- #
# Termination part                                   #
# -------------------------------------------------- #

# Stop the server
server.stop()

# Reset GPIO functions
GPIO.setFunction(L1, GPIO.IN)
GPIO.setFunction(R1, GPIO.IN)
GPIO.setFunction(L2, GPIO.IN)
GPIO.setFunction(R2, GPIO.IN)

