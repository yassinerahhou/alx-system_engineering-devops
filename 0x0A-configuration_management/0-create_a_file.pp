# Replace with the desired
file { '/tmp/school':
ensure  => '/tmp/school',
mode    => '0744',

owner   => 'www-data',   # Replace with the desired owner's 
group   => 'www-data',  # Replace    => '0744',
content => 'I love Puppet',  # Specify the file content here

}
