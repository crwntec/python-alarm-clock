#!/bin/sh
if ! hash python; then
    sudo apt-get install python3
    echo "Python installed!"
fi

sudo python ./main.py