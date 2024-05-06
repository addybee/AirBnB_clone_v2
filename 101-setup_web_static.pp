# Content of home page
$index_content = '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
'

# Define nginx configuration
$sys_conf = '
events {
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
}
'

# Update packages
exec { 'update packages':
  command => 'sudo apt-get -y update',
  before  => Exec['install Nginx'],
  provider => 'shell',
}

# Install Nginx
exec { 'install Nginx':
  command => 'sudo apt-get -y install nginx',
  before  => Exec['allow HTTP'],
  provider => 'shell',
}

# Allow HTTP traffic
exec { 'allow HTTP':
  command => 'sudo ufw allow "Nginx HTTP"',
  before  => Exec['make directory'],
  provider => 'shell',
}

# Create necessary directories
exec { 'make directory':
  command => 'sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/',
  before  => File['create index.html'],
  provider => 'shell',
}

# Create index.html file
file { 'create index.html':
  path     => '/data/web_static/releases/test/index.html',
  ensure   => file,
  content  => $index_content,
  before   => File['create link'],
}

# Create symbolic link
file { 'create link':
  ensure   => link,
  path     => '/data/web_static/current',
  target   => '/data/web_static/releases/test/',
  force    => true,
  before   => File['set_data_ownership'],
}

# Set ownership recursively for /data directory
exec { 'set_data_ownership':
  command => 'sudo chown -hR ubuntu:ubuntu /data/',
  before  => File['config file'],
  provider => 'shell',
}

# Apply nginx configuration
file { 'config file':
  path    => '/etc/nginx/nginx.conf',
  ensure  => file,
  content => $sys_conf,
  before  => Service['nginx'],
}

# Restart nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['config file'],
}
