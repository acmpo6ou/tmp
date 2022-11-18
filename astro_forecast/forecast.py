#!/usr/bin/env python3

"""
pip install PyUserInput pyautogui pillow numpy
"""

from PIL import Image, ImageGrab
from pymouse import PyMouse
import time
import pyautogui
import sys
import numpy as np

# TODO: remove this
time.sleep(3)

for i in range(30):
    # TODO: wait for image
    pyautogui.click("img/precise_aspects.png")

    money_location = pyautogui.locateOnScreen("img/money.png")
    x = money_location.left
    y = money_location.top + money_location.height

    # screenshot transits
    screenshot_fullscreen = ImageGrab.grab()
    screen_part = screenshot_fullscreen.crop((x, y, x + 400, y + 25))
    screen_part.save(f"part-{i}.png")

    pyautogui.click("img/plus_1_day.png")
    break
