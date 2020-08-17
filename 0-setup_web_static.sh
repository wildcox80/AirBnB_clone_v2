#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

#Nginx install
if ! which nginx > /dev/null
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	echo "Nginx not installed"

#Create folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#Create fake html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#Create Soft link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Change permissions
sudo chown -hR ubuntu:ubuntu /data/

#Update configuration Nginx
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#Nginx service restart
sudo service nginx start

