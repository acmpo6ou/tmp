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
import datetime

DAYS = 3
SCREENSHOT_WIDTH = 350
SCREENSHOT_HIGHT = 25


def waitFor(src):
    while not pyautogui.locateOnScreen(src):
        pass
    pyautogui.click(src)


# TODO: clean screenshot dir


print("1. Запусти Неву")
print("2. Прогнозування")
print("3. Транзити")
print("Чекаю...")


# TODO: make a cli argument for day num
for i in range(DAYS):
    waitFor("img/precise_aspects.png")

    # move mouse out of the way not to mess up the screenshot
    pyautogui.moveTo(100, 100)

    # locate screenshot beginning
    money_location = pyautogui.locateOnScreen("img/money.png")
    x = money_location.left
    y = money_location.top + money_location.height

    # screenshot transits
    screenshot_fullscreen = ImageGrab.grab()
    screen_part = screenshot_fullscreen.crop(
        (x, y, x + SCREENSHOT_WIDTH, y + SCREENSHOT_HIGHT)
    )
    screen_part.save(f"screenshots/part-{i}.png")

    waitFor("img/plus_1_day.png")

images = [Image.open(f"screenshots/part-{i}.png") for i in range(DAYS)]
# TODO: add header to the table
#   as well as day numbers
merged_img = Image.new(images[0].mode, (SCREENSHOT_WIDTH, DAYS * SCREENSHOT_HIGHT))

y = 0
for img in images:
    merged_img.paste(img, (0, y))
    y += img.height

today = datetime.date.today()
merged_img.save(f"forecast-{today.strftime('%B')}.png")
