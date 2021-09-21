#!/bin/bash

cp -r packages /usr/share/mime
cp -r mimetypes /usr/share/icons/Mint-Y-Dark

update-mime-database /usr/share/mime
sudo update-icon-caches /usr/share/icons
