import re
from kubernetes import client, config

class k8s :

  def __init__(self) :
    config.load_kube_config()
    self.v1 = client.CoreV1Api()
    self.return_obj = None

  def is_namespace_exist(self, target_namespace):
    self.return_obj = self.v1.list_pod_for_all_namespaces(watch=False)
    for item in self.return_obj.items:
      if item.metadata.namespace == target_namespace:
        return True
        break
    return False

  def is_pod_exist(self, target_pod_prefix):
    self.return_obj = self.v1.list_pod_for_all_namespaces(watch=False)
    for item in self.return_obj.items:
      match = re.match(target_pod_prefix, item.metadata.name)
      if match != None:
        return True
        break
    return False
  '''
  To Be implementation...
  ConfigMap
  ...
  and so on.
  '''
