# kill the process
exec { 'killmenow_process':
  command  => 'pkill killmenow',
  
provider => 'shell'
}
