# kill the process
exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
}
