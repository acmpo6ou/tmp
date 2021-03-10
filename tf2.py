#!/usr/bin/env python3

from PIL import Image, ImageGrab
from pymouse import PyMouse
import time
import pyautogui
import sys

time.sleep(3)

while True:
    # find a game
    pyautogui.moveTo(1470, 220)
    time.sleep(1)
    pyautogui.click()

    # casual
    pyautogui.moveTo(1509, 322)
    time.sleep(1)
    pyautogui.click()

    # start search
    pyautogui.moveTo(1531, 815)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(100, 100)

    # wait for join msg and join
    while True:
        time.sleep(1)
        img = ImageGrab.grab()
        p = img.load()[1025, 313]
        if p == (75, 107, 28):
            pyautogui.moveTo(1025, 313)
            time.sleep(1)
            pyautogui.click()
            break

# check the connecting message and cancel
    while True:
        time.sleep(1)
        img = ImageGrab.grab()
        p = img.load()[1558, 886]
        p2 = img.load()[1264, 891]

        if p == (163, 152, 132) and p2 == (39, 36, 34):
            pyautogui.moveTo(1558, 886)
            time.sleep(1)
            pyautogui.click()

            pyautogui.moveTo(1044, 312)
            time.sleep(1)
            pyautogui.click()

            pyautogui.moveTo(977, 634)
            time.sleep(1)
            pyautogui.click()
            break
        elif p == (163, 152, 132) and p2 == (255, 255, 255):
            sys.exit()
