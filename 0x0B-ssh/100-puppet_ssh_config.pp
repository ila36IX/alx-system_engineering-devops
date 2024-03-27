# >et up the node SSH configuration file so connecting
# to it doesn't require typing a password.

file { '/etc/ssh/ssh_config':
  'ensure'  => 'present',
  'content' => "
	Host *
	    SendEnv LANG LC_*
	    HashKnownHosts yes
	    GSSAPIAuthentication yes
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
	"
}
