#!/bin/sh
if ! hash python; then
    echo "python is not installed"
    sudo apt-get python
fi
python main.py