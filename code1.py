"""
All coordinates assume 1920x1200, and firefox with bookmarks toolbar enabled.
Down Key has been hit 6 times
x_pad = 521
y_pad = 330
Play area = x_pad+1, y_pad+1, 800,600
"""


import os
import time
import win32api, win32con
from PIL import ImageGrab, ImageOps
from numpy import *
# Global
#_________________________

x_pad = 521
y_pad = 330


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("click")


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left Down')


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left release')


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def getCords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x ,  y)


def startGame():
    # location of first menu
    mousePos((204, 137))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((477, 382))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((255, 304))
    leftClick()
    time.sleep(.1)


class Cord:
    f_shrimp = (-66,265)
    f_rice = (-16,269)
    f_nori = (-6, 323)
    f_roe = (-59, 325)
    f_salmon = (-67, 378)
    f_unagi = (-19, 376)

    phone = (484, 298)

    menu_toppings = (432, 210)

    t_shrimp = (385, 155)
    t_unagi = (468, 164)
    t_nori = (376, 216)
    t_roe = (481, 213)
    t_salmon = (398, 275)
    t_exit = (489, 274)

    delivery = (390, 230)

    menu_rice = (436, 236)
    buy_rice = (441, 220)



def clearTables():
    mousePos((-25, 152))
    leftClick()

    mousePos((76, 151))
    leftClick()

    mousePos((176, 148))
    leftClick()

    mousePos((279, 148))
    leftClick()

    mousePos((384, 148))
    leftClick()

    mousePos((483, 148))
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((Cord.f_rice[0]+50,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        print("Making Gunkan")
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)


def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()

        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()

        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (43,43,43):
            print("rice is available")
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)

        else:
            print("rice is not available")
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(5)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        # print
        # 'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (28,28,28):
            # print
            # 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            # print
            # 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (43,43,43):
            # print
            # 'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            # print('roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i,j in foodOnHand.items():
        if i == 'nori' or i == 'roe' or i =='rice':
            if j <= 4:
                print("buying " + i)
                buyFood(i)



"""
Plate Coords
-25 152
76 151
176 148
279 149
384 151
483 147



"""



def screenGrab():
    box = (x_pad+1,y_pad+1, 800,600)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '//full-snap__' + str(int(time.time())) + '.png', 'PNG')
    return  im

def main():
    getCords()


if __name__ == '__main__':
    # im = screenGrab()
    # print(im.getpixel(Cord.t_roe))
    # print(im.getpixel(Cord.t_salmon))
    # print(im.getpixel(Cord.t_shrimp))
    # print(im.getpixel(Cord.t_nori))
    # print(im.getpixel(Cord.t_unagi))
    # print(im.getpixel(Cord.buy_rice))
    getCords()



