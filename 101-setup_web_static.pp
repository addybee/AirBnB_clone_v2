# Content of home page
$content = 'sudo apt-get update;
sudo apt-get -y install nginx;
sudo ufw allow 'Nginx HTTP';
sudo mkdir -p /data/web_static/shared/;
sudo mkdir -p /data/web_static/releases/test/;
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html;
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
sudo chown -hR ubuntu:ubuntu /data/;
echo "events {
  }
http {
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 65;
  types_hash_max_size 2048;
  include /etc/nginx/mime.types;
  default_type application/octet-stream;
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;

  server {
    location /hbnb_static {
      alias /data/web_static/current/;
    }
  }
}" | sudo tee /etc/nginx/nginx.conf;
sudo service nginx restart;
'


# Install Nginx and configure a server
exec { 'install Nginx':
  command => $content,
  provider => 'shell',
}
