# Fixing Apache is returning a 500 error and
# automate it using Puppet.

$file_to_edit = '/var/www/html/wp-settings.php'


exec { 'fix-typo':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
