# create a file in /tmp.
file { '/tmp/test' :
path => '~/.ssh/config '
line => ['PasswordAuthentication no','IdentifyFile ~/.ssh/school'],
owner   => 'ubuntu',

}
