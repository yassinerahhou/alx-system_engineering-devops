file { '/tmp/school':
  ensure  => 'file',        # Ensure that the path is a file, not a directory
  owner   => 'www-data',    # Replace with the desired owner's username
  group   => 'www-data',    # Replace with the desired group name
  mode    => '0744',        # Correct file permission mode
  content => 'I love Puppet',  # Specify the file content here
}
