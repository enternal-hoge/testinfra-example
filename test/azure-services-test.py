import sys
sys.path.append("../lib")
import infra_azure_common as aztest

azure = aztest.azure();

# for test
azure.subscription_id = 'XXX'
azure.client_id = 'XXX'
azure.secret = 'XXX'
azure.tenant_id = 'XXX'

resource_group_name = 'test'

azure.getCredential()

# Resource Group
def test_resouce_group_exist(host):
    assert azure.is_resouce_group_exist(resource_group_name)

# VNet
def test_virtual_network_exist(host):
    assert azure.is_virtual_network_exist(resource_group_name, "test-vnet")

# Application Gateway
def test_application_gateway_exist(host):
    assert azure.is_application_gateway_exist(resource_group_name, "application-gateway")

# NIC
def test_network_internace_card_exist(host):
    assert azure.is_network_internace_card_exist(resource_group_name, "aaaaa-vm-network-interface")
    assert azure.is_network_internace_card_exist(resource_group_name, "bbbbb-vm-network-interface")
    assert azure.is_network_internace_card_exist(resource_group_name, "ccccc-vm-network-interface")

# Load Balancer
#def test_load_balancer_exist(host):
#    assert azure.is_load_balancer_exist(resource_group_name, "")

# Subnet
def test_subnet_exist(host):
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "kubernetes-master-subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "application-subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "dmz-subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "application-gateway-subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "kubernetes-agent-subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "aaaaa-vm--subnet")
    assert azure.is_subnet_exist(resource_group_name, "test-vnet", "GatewaySubnet")

# Subnet Address Prefix
def test_subnet_address_prefix_valid(host):
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "kubernetes-master-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "application-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "dmz-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "application-gateway-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "kubernetes-agent-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "aaaaa-vm-subnet", "xxx.xxx.xxx.xxx/xx")
    assert azure.is_subnet_address_prefix_valid(resource_group_name, "test-vnet", "GatewaySubnet", "xxx.xxx.xxx.xxx/xx")

# NSG
def test_network_security_group_exist(host):
    assert azure.is_network_security_group_exist(resource_group_name, "application-gateway-subnet-nsg")
    assert azure.is_network_security_group_exist(resource_group_name, "aaaaa-vm-nsg")
    assert azure.is_network_security_group_exist(resource_group_name, "bbbbb-vm--nsg")
    assert azure.is_network_security_group_exist(resource_group_name, "ccccc-vm-nsg")
    assert azure.is_network_security_group_exist(resource_group_name, "ddddd-vm-nsg")

# Public IP
def test_public_ip_exist(host):
    assert azure.is_public_ip_exist(resource_group_name, "aaaaa-vm--dynamic-ip")
    assert azure.is_public_ip_exist(resource_group_name, "bbbbb-vm-dynamic-ip")
    assert azure.is_public_ip_exist(resource_group_name, "test-vpn-gateway")

# DNS zone
def test_dns_zone_exist(host):
    assert azure.is_dns_zone_exist(resource_group_name, "test.com")

# DNS record
def test_dns_record_exist(host):
    assert azure.is_dns_record_exist(resource_group_name, "test.com", "gateway")
    assert azure.is_dns_record_exist(resource_group_name, "test.com", "vm")

# DNS record registerd ip address
def test_dns_arecord_ip_address_exist(host):
    assert azure.is_dns_arecord_ip_address_exist(resource_group_name, "test.com", "gateway", "XXX.XXX.XXX.XXX")
    assert azure.is_dns_arecord_ip_address_exist(resource_group_name, "test.com", "vm", "XXX.XXX.XXX.XXX")

# VM
def test_virtual_machine_exist(host):
    assert azure.is_virtual_machine_exist(resource_group_name, "aaaaa-vm")
    assert azure.is_virtual_machine_exist(resource_group_name, "bbbbb-vm")
    assert azure.is_virtual_machine_exist(resource_group_name, "ccccc-vm")
    assert azure.is_virtual_machine_exist(resource_group_name, "ddddd-vm")

def test_virtual_machine_(host):
    assert azure.is_virtual_machine_location(resource_group_name, "aaaaa-vm", "japanwest")
    assert azure.is_virtual_machine_location(resource_group_name, "bbbbb-vm", "japanwest")
    assert azure.is_virtual_machine_location(resource_group_name, "ccccc-vm", "japanwest")
    assert azure.is_virtual_machine_location(resource_group_name, "ddddd-vm", "japanwest")

def test_virtual_machine_size(host):
    assert azure.is_virtual_machine_size(resource_group_name, "aaaaa-vm", "Basic_A2")
    assert azure.is_virtual_machine_size(resource_group_name, "bbbbb-vm", "Basic_A0")
    assert azure.is_virtual_machine_size(resource_group_name, "ccccc-vm", "Basic_A1")
    assert azure.is_virtual_machine_size(resource_group_name, "ddddd-vm", "Basic_A2")

# Storage Account
def test_storage_account_exist(host):
    assert azure.is_storage_account_exist(resource_group_name, "diagnostics4test")
    assert azure.is_storage_account_exist(resource_group_name, "vhd2str4test")

