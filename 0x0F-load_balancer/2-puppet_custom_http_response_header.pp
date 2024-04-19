# Update package lists
package { 'apt':
  ensure => 'present',
} -> Exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
  ensure => 'present',
}

# Add custom HTTP header
file_line { 'http_header':
  path         => '/etc/nginx/nginx.conf',
  match        => 'server_name',
  # Insert line after the matching line
  insert_after => true,
  line         => "add_header X-Served-By \"${hostname}\";",
}

# Restart nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

