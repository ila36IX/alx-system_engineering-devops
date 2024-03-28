# Install flask from pip3

package { 'python3-flask':
  provider => 'pip3',
  ensure   => '2.1.0'
}
