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

# time.sleep(3)

for i in range(30):
    # точние аспекти
    pyautogui.moveTo(45, 965)
    time.sleep(0.1)
    pyautogui.click()

    # screenshot transits
    screenshot_fullscreen = ImageGrab.grab()
    screen_part = screenshot_fullscreen.getdata()
    numpy_array = np.array(screen_part)[10:335, 412:425]
    print(len(numpy_array))

    # save image
    screen_part.save("test.png")
    break
