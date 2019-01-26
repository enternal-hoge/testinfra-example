import sys
sys.path.append("../lib")
import infra_azure_common as aztest

azure = aztest.azure();

# for test-function
azure.subscription_id = 'XXX'
azure.client_id = 'XXX'
azure.secret = 'XXX'
azure.tenant_id = 'XXX'

resource_group_name = 'test-functions'

azure.getCredential()

def test_storage_account_exist(host):
    assert azure.is_storage_account_exist(resource_group_name, "functions4storagetest")

