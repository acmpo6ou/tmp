#!/usr/bin/env python3

"""
pip install PyUserInput pyautogui pillow numpy
"""
import calendar

from PIL import Image, ImageGrab, ImageDraw
from pymouse import PyMouse
import time
import pyautogui
import sys
import numpy as np
import datetime

DAYS = 3
SCREENSHOT_WIDTH = 350
SCREENSHOT_HEIGHT = 25
DAYS_NUMS_WIDTH = 50


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
        (x, y, x + SCREENSHOT_WIDTH, y + SCREENSHOT_HEIGHT)
    )
    screen_part.save(f"screenshots/part-{i}.png")

    waitFor("img/plus_1_day.png")

images = [Image.open(f"screenshots/part-{i}.png") for i in range(DAYS)]
# TODO: add header to the table, as well as day numbers
merged_img = Image.new(
    images[0].mode,
    (SCREENSHOT_WIDTH + DAYS_NUMS_WIDTH, DAYS * SCREENSHOT_HEIGHT),
)

y = 0
for img in images:
    merged_img.paste(img, (DAYS_NUMS_WIDTH, y))
    y += img.height

draw = ImageDraw.Draw(merged_img)
month = calendar.monthcalendar()
for week in month:
    for day in week:
        draw.text((5, 5), "Sample Text", (255, 255, 255))

today = datetime.date.today()
merged_img.save(f"forecast-{today.strftime('%B')}.png")
