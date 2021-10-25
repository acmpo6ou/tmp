#!/usr/bin/env python3.8

"""
Generates colorful icons from simpleicons pack.
"""

import os
from simpleicons.all import icons

os.mkdir("icons")

for name, icon in icons.items():
    xml = icon.get_xml_bytes(fill=f"#{icon.hex}")
    with open(f"icons/{name}.svg", "wb") as file:
        file.write(xml)
