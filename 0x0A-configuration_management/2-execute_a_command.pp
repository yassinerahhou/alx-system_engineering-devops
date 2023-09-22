# kill the process
exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  provider => 'shell'
}
