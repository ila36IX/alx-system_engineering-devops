# Increasing the maximum number of open file descriptors (ulimit) for the Nginx
# web server by modifying the configuration file /etc/default/nginx.
exec { 'Increating the ULIMIT':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart the NGINX server
exec { 'Restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
