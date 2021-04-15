#!/usr/bin/python3

import time, os, sys

time_to_sleep = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
time.sleep(time_to_sleep)
os.system("cinnamon-screensaver-command --lock")
