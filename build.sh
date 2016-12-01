#!/bin/bash

PYENV_HOME=$WORKSPACE/.pyenv

echo "Setting environment to: $PYENV_HOME"

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
virtualenv --no-site-packages $PYENV_HOME -p python3
source $PYENV_HOME/bin/activate
pip3 install -r requirements.txt # Sets up dependencies
nosetests --with-xunit app
pylint -f parseable app/ | tee pylint.out