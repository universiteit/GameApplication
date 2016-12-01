#!/bin/bash
pip3 install -r requirements.txt # Sets up dependencies
rsync -r $WORKSPACE /var/www/ --exclude .git
sudo /usr/sbin/service apache2 reload