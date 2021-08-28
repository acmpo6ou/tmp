#!/usr/bin/env python3

import os
import random
import getpass

MOD_DIR = f"/home/{getpass.getuser()}/.steam/steam/steamapps/common/Team Fortress 2/tf/custom/rayshud/"
WALLS_DIR = f"{MOD_DIR}/materials/wallpapers/"
WALL_PATH = f"{MOD_DIR}/materials/console/background_classic.vtf"

num_walls = len(os.listdir(WALLS_DIR))
nums = range(1, num_walls+1)
wall = random.choice(nums)

os.remove(WALL_PATH)
os.symlink(f"{WALLS_DIR}/{wall}.vtf", WALL_PATH)
