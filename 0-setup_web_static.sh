#!/usr/bin/env bash
# preparing server for deployment

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo service ngingx start

# do we want sudo?
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# may not need touch
sudo touch /data/web_static/releases/test/index.html
sudo echo "Dummy Data" | sudo tee /data/web_static/releases/test/index.html

ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data

find="^\tlocation / {"
replace="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"

sudo sed -i "s@${find}@${replace}@" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
