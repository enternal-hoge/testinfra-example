# Azure AD Service Principal Credentials
from azure.common.credentials import ServicePrincipalCredentials
# Azure Resource Group
from azure.mgmt.resource import ResourceManagementClient
# Azure VM Client
from azure.mgmt.compute import ComputeManagementClient
# Azure Network Client
from azure.mgmt.network import NetworkManagementClient
# Azure DNS Client
from azure.mgmt.dns import DnsManagementClient
# Azure Storage Acount Client
from azure.mgmt.storage import StorageManagementClient
# Azure SQL Client
from azure.mgmt.sql import SqlManagementClient
# Azure Container Registry Client
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
# Azure Graph RBAC Client
from azure.graphrbac import GraphRbacManagementClient

class azure : 

  def __init__(self) :
    self.subscription_id = None
    self.client_id = None
    self.secret = None
    self.tenant_id = None
    self.credentials = None
    self.compute_client = None
    self.network_client = None
    self.storage_client = None 
    self.container_regisry_client = None
    self.sql_client = None
    self.dns_client = None

  def getCredential(self) : 
    self.credentials = ServicePrincipalCredentials(
      client_id = self.client_id,
      secret = self.secret,
      tenant = self.tenant_id
    )
    
    self.compute_client = ComputeManagementClient(self.credentials, self.subscription_id)
    self.network_client = NetworkManagementClient(self.credentials, self.subscription_id)
    self.storage_client = StorageManagementClient(self.credentials, self.subscription_id)
    self.container_regisry_client = ContainerRegistryManagementClient(self.credentials, self.subscription_id)
    self.sql_client = SqlManagementClient(self.credentials, self.subscription_id)
    self.dns_client = DnsManagementClient(self.credentials, self.subscription_id)

  #####  Resource Group
  def is_resouce_group_exist(self, resource_group_name) : 
    resource_client = ResourceManagementClient(self.credentials, self.subscription_id)
    for resources in resource_client.resource_groups.list():
      if resources.name == resource_group_name:
        return True
        break
    return False


  #### Azure Network Resource
  # VPN
  def is_virtual_network_exist(self, resource_group_name, virtual_network_name) : 
    try:
      result_get = self.network_client.virtual_networks.get(resource_group_name, virtual_network_name)
      if result_get.name == virtual_network_name:
        return  True
    except:
      return False

  # NIC
  def is_network_internace_card_exist(self, resource_group_name, network_interface_card_name) :
    try:
      result_get = self.network_client.network_interfaces.get(resource_group_name, network_interface_card_name)
      if result_get.name == network_interface_card_name:
        return True
    except:
      return False

  # subnet
  def is_subnet_exist(self, resource_group_name, virtual_network_name, subnet_name) :
    try:
      result_get = self.network_client.subnets.get(resource_group_name, virtual_network_name, subnet_name)
      if result_get.name == subnet_name:
        return True
    except:
      return False

  # subnet address prefix
  def is_subnet_address_prefix_valid(self, resource_group_name, virtual_network_name, subnet_name, address_prefix) :
    try:
      result_get = self.network_client.subnets.get(resource_group_name, virtual_network_name, subnet_name)
      if result_get.address_prefix == address_prefix:
        return True
    except:
      return False

  # NSG
  def is_network_security_group_exist(self, resource_group_name, network_security_group_name) :
    try:
      result_get = self.network_client.network_security_groups.get(resource_group_name, network_security_group_name)
      if result_get.name == network_security_group_name:
        return True
    except:
      return False

  # L/B
  def is_load_balancer_exist(self, resource_group_name, load_balancer_name) :
    try:
      result_get = self.network_client.load_balancers.get(resource_group_name, load_balancer_name)
      if result_get.name == load_balancer_name:
       return True
    except:
      return False

  # public ip
  def is_public_ip_exist(self, resource_group_name, public_ip_name) :
    try:
      result_get = self.network_client.public_ip_addresses.get(resource_group_name, public_ip_name)
      if result_get.name == public_ip_name:
        return True
    except:
      return False

  # Application Gateway
  def is_application_gateway_exist(self, resource_group_name, application_gateway_name) : 
    try:
      result_get = self.network_client.application_gateways.get(resource_group_name, application_gateway_name)
      if result_get.name == application_gateway_name:
        return True
    except:
      return False

  # route table
  def is_route_table_exist(self, resource_group_name, route_table_name) :
    try:
      result_get = self.network_client.route_tables.get(resource_group_name, route_table_name)
      if result_get.name == route_table_name:
        return True
    except:
      return False

  # DNS zone
  def is_dns_zone_exist(self, resource_group_name, zone_name) :
    try:
      result_get = self.dns_client.zones.get(resource_group_name, zone_name)
      if result_get.name == zone_name:
        return True
    except:
      return False

  # DNS record
  def is_dns_record_exist(self, resource_group_name, zone_name, record_set_name) :
    try:
      result_get = self.dns_client.record_sets.get(resource_group_name, zone_name, record_set_name, 'A')
      if result_get.name == record_set_name:
        return True
    except:
      return False

  # DNS record registerd ip address
  def is_dns_arecord_ip_address_exist(self, resource_group_name, zone_name, record_set_name, ip_address) :
    result_get = self.dns_client.record_sets.get(resource_group_name, zone_name, record_set_name, 'A')
    for arecord in result_get.arecords:
      if arecord.ipv4_address == ip_address:
        return True
        break
    return False

  '''
  To Be implementation...
  def is_network_security_group_rule_exist(network_security_group_rule_name) : 
  def is_express_route_circuit_exist(express_route_circuit_name) :
  '''

  ######  Azure VM
  # VM
  def is_virtual_machine_exist(self, resource_group_name, virtual_machine_name) : 
    try:
      result_get = self.compute_client.virtual_machines.get(resource_group_name, virtual_machine_name)
      if result_get.name == virtual_machine_name:
        return True
    except:
      return False

  def is_virtual_machine_location(self, resource_group_name, virtual_machine_name, location) :
    try:
      result_get = self.compute_client.virtual_machines.get(resource_group_name, virtual_machine_name)
      if result_get.location == location:
        return True
    except:
      return False

  def is_virtual_machine_size(self, resource_group_name, virtual_machine_name, vm_size) :
    try:
      result_get = self.compute_client.virtual_machines.get(resource_group_name, virtual_machine_name)
      if result_get.hardware_profile.vm_size == vm_size:
        return True
    except:
      return False

  def is_managed_disk_exist(self, resource_group_name, disk_name) :
    try:
      result_get = self.compute_client.disks.get(resource_group_name, disk_name)
      if result_get.name == disk_name:
        return True
    except:
      return False

  # Availebility Set
  def is_availability_set_exist(self, resource_group_name, availability_set_name) : 
    try:
      result_get = self.compute_client.availability_sets.get(resource_group_name, availability_set_name)
      if result_get.name == availability_set_name:
        return True
    except:
      return False
  
  ##### Azure Storage
  # Storage Account
  def is_storage_account_exist(self, resource_group_name, storage_account_name) : 
    result_list = self.storage_client.storage_accounts.list_by_resource_group(resource_group_name)
    for result in result_list:
      if result.name == storage_account_name:
        return True
        break  
    return False

  ##### Azure Container Registry
  def is_container_regsitry_exist(self, container_registry_name) : 
    name_status = self.container_regisry_client.registries.check_name_availability(container_registry_name)
    if name_status.reason == 'AlreadyExists':
      return True
    return False

  ###### Azure SQL Databse
  # Elastic Pool
  def is_sql_elastic_pool_exist(self, resource_group_name, server_name, pool_name) :
    try:
      result_get = self.sql_client.elastic_pools.get(resource_group_name, server_name, pool_name)
      print result_get
      if result_get.name == pool_name:
        return True
    except:
      return False

  def is_sql_elastic_pool_location(self, resource_group_name, server_name, pool_name, location) :
    try:
      result_get = self.sql_client.elastic_pools.get(resource_group_name, server_name, pool_name)
      print result_get
      if result_get.location == location:
        return True
    except:
      return False

  def is_sql_elatic_pool_edition(self, resource_group_name, server_name, pool_name, edition) :
    try:
      result_get = self.sql_client.elastic_pools.get(resource_group_name, server_name, pool_name)
      print result_get
      if result_get.edition == edition:
        return True
    except:
      return False

  def is_sql_elastic_pool_dtu(self, resource_group_name, server_name, pool_name, dtu) :
    try:
      result_get = self.sql_client.elastic_pools.get(resource_group_name, server_name, pool_name)
      print result_get
      if result_get.dtu == dtu:
        return True
    except:
      return False

  def is_sql_elastic_pool_storage_max(self, resource_group_name, server_name, pool_name, storage_mb) :
    try:
      result_get = self.sql_client.elastic_pools.get(resource_group_name, server_name, pool_name)
      print result_get
      if result_get.storage_mb == storage_mb:
        return True
    except:
      return False

  # SQL Server
  def is_sql_server_exist(self, resource_group_name, server_name) : 
    try:
      result_get = self.sql_client.servers.get(resource_group_name, server_name)
      if result_get.name == server_name:
        return True
    except:
      return False

  # SQL Database
  def is_sql_database_exist(self, resource_group_name, server_name, db_name) :
    try:
      result_get = self.sql_client.databases.get(resource_group_name, server_name, db_name)
      if result_get.name == db_name:
        return True
    except:
      return False
  '''
  To Be implementaion...
  SQL Database Elastic Pool
  '''

  ##### RBAC
  '''
  To Be implementaion...
  '''
