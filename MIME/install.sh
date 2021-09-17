#!/bin/bash

cp x-kotlin.xml /usr/share/mime/packages
cp -r mimetypes /usr/share/icons/Mint-Y-Dark
update-mime-database /usr/share/mime
sudo update-icon-caches /usr/share/icons
