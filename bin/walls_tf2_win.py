#!/usr/bin/env python3

import os
import shutil
import random
import getpass

MOD_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\custom/rayshud/"
WALLS_DIR = f"{MOD_DIR}/materials/wallpapers/"
WALL_PATH = f"{MOD_DIR}/materials/console/background_classic.vtf"

num_walls = len(os.listdir(WALLS_DIR))
nums = range(1, num_walls) # note: we need to exclude .gitignore
wall = random.choice(nums)

if os.path.exists(WALL_PATH):
    os.remove(WALL_PATH)
shutil.copy(f"{WALLS_DIR}/{wall}.vtf", WALL_PATH)
