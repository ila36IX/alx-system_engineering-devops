package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/not_found.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

$config ="server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
                return 301 https://google.com;
        }

        error_page 404 /not_found.html;

        location /not_found.html {
                internal;
        }
}
"

file { '/etc/nginx/sites-available/getalien.tech':
  ensure  => file,
  backup  => '.backup',
  content => $config,
}

file {'/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/getalien.tech',
}

exec {'sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/getalien.tech':
  path   => '/usr/bin:/usr/sbin:/bin',
  unless => 'grep -c "add_header X-Served-By" /etc/nginx/sites-available/getalien.tech'
}

exec {'Redirect page':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i "/location \/redirect_me {/,/}/ s/return 301 .*;/return 301 https:\/\/exemple.com;/g" \
  /etc/nginx/sites-available/getalien.tech'
}

exec {'reload the web server':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'service nginx reload'
}
