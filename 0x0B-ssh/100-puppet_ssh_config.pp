# Create an SSH client configuration file and set its content
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
  owner   => 'ubuntu',
  mode    => '0644',
}
