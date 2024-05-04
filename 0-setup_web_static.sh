#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R 'ubuntu':'ubuntu' /data/
sudo sed -i "/http {/a\\
    server {\\
        location \/hbnb_static {\\
            alias \/data\/web_static\/current\/;\\
        }\\
    }\n" /etc/nginx/nginx.conf
sudo sudo sed -i "s/include \/etc\/nginx\/sites-enabled/\
#include \/etc\/nginx\/sites-enabled/g" /etc/nginx/nginx.conf
sudo nginx -s reload