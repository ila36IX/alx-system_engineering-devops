package { 'nginx':
	ensure   => installed,
	name     => "nginx",
	provider => "apt",
}

file { '/var/www/html/index.html':
	path => '/var/www/html/index.html',
	ensure => present,
	content => "Hello World!",
}

file { '/etc/nginx/sites-available/default':
	path => '/etc/nginx/sites-available/default',
	ensure => present,
	line => "server_name _;\n\tlocation /redirect_me {\n\t\treturn 301 \$scheme://google.com;\n\t}",
	match => "server_name _;$",
}
