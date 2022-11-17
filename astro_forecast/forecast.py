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

time.sleep(3)

for i in range(30):
    pyautogui.click("img/precise_aspects.png")

    # screenshot transits
    screenshot_fullscreen = ImageGrab.grab()
    screen_part = screenshot_fullscreen.crop((10, 412, 335, 425))
    screen_part.save(f"part-{i}.png")

    # +1 day
    pyautogui.moveTo(30, 700)
    time.sleep(0.1)
    pyautogui.click()

    break
