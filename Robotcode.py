from bluedot import BlueDot
from gpiozero import Robot
from gpiozero import LED
from signal import pause

#GPIO pins for motors.
robot = Robot(left=(24, 23), right=(20, 21))
#GPIO pins for front and rear led's.
led1 = LED(18)
led2 = LED(16)
led3 = LED(25)
led4 = LED(26)
#GPIO pin for on led.
led5 = LED(17)

#Commands for robot movement
def up():
   robot.forward()

def down():
    robot.backward()

def left():
    robot.left()

def right():
    robot.right()

def stop():

#Bludeot interface - tells bluedot what layout to use and what not to show
bd = BlueDot(cols=7, rows=3)
bd.color = "green"

bd[0,0].visible = False
bd[2,0].visible = False
bd[0,2].visible = False
bd[2,2].visible = False
bd[1,1].visible = False
bd[3,0].visible = False
bd[3,1].visible = False
bd[3,2].visible = False
bd[4,0].visible = False
bd[4,1].visible = False
bd[4,2].visible = False
bd[5,1].visible = False
bd[6,0].visible = False
bd[6,1].visible = False
bd[6,2].visible = False

bd[1,0].when_pressed = up
bd[1,0].square = True
bd[1,2].when_pressed = down
bd[1,2].square = True
bd[0,1].when_pressed = left
bd[0,1].square = True
bd[2,1].when_pressed = right
bd[2,1].square = True

bd.when_released = stop

#turning on leds when button pressed
def pressed_1():
   led1.on()
   led2.on()
   led3.on()
   led4.on()

def pressed_2():
   led1.off()
   led2.off()
   led3.off()
   led4.off()

bd[5,0].when_pressed = pressed_1
bd[5,2].when_pressed = pressed_2
bd[5,0].color = "yellow"
bd[5,2].color = "red"

while True:
  led5.on()

pause()

