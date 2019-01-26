import sys
sys.path.append("../lib")
import infra_azure_common as aztest

azure = aztest.azure();

azure.subscription_id = 'XXX'
azure.client_id = 'XXX'
azure.secret = 'XXX'
azure.tenant_id = 'XXX'

resource_group_name = 'test'

azure.getCredential()

azure.is_dns_arecord_ipaddress_exist(resource_group_name, "test.com", "gateway")
