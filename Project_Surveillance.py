import cv2
import time
from djitellopy import tello
import key_press_module as kp


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

global img
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): ud = speed
    elif kp.getKey("DOWN"): ud = -speed

    if kp.getKey("w"): fb = speed
    elif kp.getKey("s"): fb = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    elif kp.getKey("e"): me.takeoff()

    if kp.getKey("p"):
        cv2.imwrite(f'Resources/images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    #print(kp.getKey("s"))

    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)






