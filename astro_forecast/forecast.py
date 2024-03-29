#!/usr/bin/env python3

"""
pip install PyUserInput pyautogui pillow numpy python-dateutil
"""
import calendar
import datetime
import glob
import os
import sys

import pyautogui
from PIL import Image, ImageGrab, ImageDraw, ImageFont
from dateutil.relativedelta import relativedelta

if len(sys.argv) < 2 or sys.argv[1] not in ("--current", "--next"):
    print("Вкажи --current або --next для теперішнього або наступного місяця.")
    sys.exit()

month = datetime.date.today()
if sys.argv[1] == "--next":
    month += relativedelta(months=1)

month_range = calendar.monthcalendar(month.year, month.month)
DAYS = calendar.monthrange(month.year, month.month)[1]

SCREENSHOT_WIDTH = 350
SCREENSHOT_HEIGHT = 25
DAYS_NUMS_WIDTH = 50


def waitFor(src):
    while not pyautogui.locateOnScreen(src):
        pass
    pyautogui.click(src)


for file in glob.glob("screenshots/*.png"):
    os.remove(file)

print("1. Запусти Неву")
print("2. Прогнозування")
print("3. Транзити")
print("Чекаю...")

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

num_week_separators = len(month_range) - 1
width = SCREENSHOT_WIDTH + DAYS_NUMS_WIDTH
height = (DAYS + num_week_separators) * SCREENSHOT_HEIGHT
merged_img = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(merged_img)
font = ImageFont.truetype("Ubuntu-Nerd.ttf", 12)
images = (Image.open(f"screenshots/part-{i}.png") for i in range(DAYS))
y = 0

for week in month_range:
    for day in week:
        if not day:
            continue

        day_name = datetime.datetime(month.year, month.month, day).strftime("%a")
        day_num = f"{day:02} {day_name}"
        try:
            img = next(images)
        except StopIteration:
            break

        draw.text((5, y + 3), day_num, (255, 255, 255), font=font)
        merged_img.paste(img, (DAYS_NUMS_WIDTH, y))
        y += SCREENSHOT_HEIGHT
    y += SCREENSHOT_HEIGHT

merged_img.save(f"forecast-{month.strftime('%B')}.png")
