#!/bin/bash
PIC=$(ls $PWD/*.jpg | shuf -n1)
gconftool -t string -s /desktop/gnome/background/picture_filename $PIC
