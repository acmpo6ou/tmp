#!/usr/bin/env python3

from PIL import Image, ImageGrab
from pymouse import PyMouse
import time
import pyautogui
import sys

time.sleep(3)

while True:
    pyautogui.press("g")
    pyautogui.press("x")
    time.sleep(0.4)
    pyautogui.press("5")
    pyautogui.press("g")
