import sys
sys.path.append("../lib")
import infra_azure_common as aztest

azure = aztest.azure();

# for test
azure.subscription_id = 'XXX'
azure.client_id = 'XXX'
azure.secret = 'XXX'
azure.tenant_id = 'XXX'

resource_group_name = 'test-kubernetes'

azure.getCredential()

# Resource Group
def test_resouce_group_exist(host):
    assert azure.is_resouce_group_exist(resource_group_name)

# Load Balancer
#def test_load_balancer_exist(host):
#    assert azure.is_load_balancer_exist(resource_group_name, "")

# NIC
def test_network_internace_card_exist(host):
    assert azure.is_network_internace_card_exist(resource_group_name, "k8s-master-XXXXXXX-nic-0")
    assert azure.is_network_internace_card_exist(resource_group_name, "k8s-k8sagent-XXXXXXX-nic-0")
    assert azure.is_network_internace_card_exist(resource_group_name, "k8s-k8sagent-XXXXXXX-nic-1")

# NSG
def test_network_security_group_exist(host):
    assert azure.is_network_security_group_exist(resource_group_name, "k8s-master-XXXXXXX-nsg")

# availability set
def test_availability_set_exist(host):
    assert azure.is_availability_set_exist(resource_group_name, "master-availabilityset-XXXXXXX")
    assert azure.is_availability_set_exist(resource_group_name, "k8sagent-availabilitySet-XXXXXXX")

# VM
def test_virtual_machine_exist(host):
    assert azure.is_virtual_machine_exist(resource_group_name, "k8s-master-XXXXXXX-0")
    assert azure.is_virtual_machine_exist(resource_group_name, "k8s-k8sagent-XXXXXXX-0")
    assert azure.is_virtual_machine_exist(resource_group_name, "k8s-k8sagent-XXXXXXX-1")

# Storage Account
def test_storage_account_exist(host):
    assert azure.is_storage_account_exist(resource_group_name, "00gnowqehhnyxe4websagnt0")

# Managed Disk
def test_managed_disk_exist(host):
    assert azure.is_managed_disk_exist(resource_group_name, "k8s-master-XXXXXXX-0-etcddisk")
    assert azure.is_managed_disk_exist(resource_group_name, "k8s-master-XXXXXXX-0_OsDisk_1_6a93a771db5f432c8737998162b23b3f")

# Route Table
def test_route_table_exist(host):
    assert azure.is_route_table_exist(resource_group_name, "k8s-master-XXXXXXX-routetable")

#Todo test route
"""
route = self.network_client.routes.get(
    resource_group.name,
    route_table.name,
    route.name
)
"""

