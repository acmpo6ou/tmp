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


def waitFor(src):
    while not pyautogui.locateOnScreen(src):
        time.sleep(0.1)
    pyautogui.click(src)


# TODO: make a cli argument for day num
for i in range(30):
    waitFor("img/precise_aspects.png")

    # locate screenshot beginning
    money_location = pyautogui.locateOnScreen("img/money.png")
    x = money_location.left
    y = money_location.top + money_location.height

    # screenshot transits
    screenshot_fullscreen = ImageGrab.grab()
    screen_part = screenshot_fullscreen.crop((x, y, x + 400, y + 25))
    screen_part.save(f"part-{i}.png")

    waitFor("img/plus_1_day.png")
