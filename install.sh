#!/bin/sh
if ! hash python; then
    echo "python is not installed"
    sudo apt-get python
fi
python -c "import playsound"
if [ echo$? == 1 ]
then
    pip install playsound
fi
python main.py