# congigure new server
package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

exec {'sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/getalien.tech':
  path   => '/usr/bin:/usr/sbin:/bin',
  unless => 'grep -c "add_header X-Served-By" /etc/nginx/sites-available/getalien.tech'
}

exec {'reload the web server':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'service nginx reload'
}
