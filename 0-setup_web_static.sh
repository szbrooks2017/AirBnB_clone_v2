#!/usr/bin/env bash
# preparing server for deployment

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo service ngingx start

# do we want sudo?
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

sudo echo "Pokemon" | sudo tee /data/web_static/releases/test/index.html

# add sudo
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# add /data/
sudo chown -hR ubuntu:ubuntu /data/

find="^\tlocation / {"
replace="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"
sudo sed -i "s@${find}@${replace}@" /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
