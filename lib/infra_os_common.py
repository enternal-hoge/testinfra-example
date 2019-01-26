import commands
import os

class os :

  def is_fluentd_plugin_exist(self, plugin_name):
    command_str = "/opt/td-agent/embedded/bin/fluent-gem list | grep " + plugin_name
    if len(commands.getoutput(command_str)) == 0:
      return False
    else:
      return True

  def is_installed(self, path):
    if os.path.isfile(path):
      return True
    else:
      return False

  #def is_port_listenn(self, port):
  #  result = "netstat -an | grep " + port
  #  if result is None:
  #    return False 
  #  else:
  #    return True

