#!/usr/bin/env python3

import glob, sys, os


def bash(*args):
    print("Running:", args[0])
    if os.system(*args):
        sys.exit(1)


# file from which we will get cover
source = glob.glob("*.mp3")[0]

# get the cover
bash(f"ffmpeg -i {source} -an -vcodec copy cover.jpg")

# add cover to each normalized song
for track in glob.glob("*.mp3"):
    bash(
        f"ffmpeg -y -i macro-output/{track} -i cover.jpg"
        f" -map_metadata 0 -map 0 -map 1 {track}"
    )
