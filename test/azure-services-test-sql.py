import sys
sys.path.append("../lib")
import infra_azure_common as aztest

azure = aztest.azure();

# for test-sql
azure.subscription_id = 'XXX'
azure.client_id = 'XXX'
azure.secret = 'XXX'
azure.tenant_id = 'XXX'

resource_group_name = 'test-sql'

azure.getCredential()

def test_sql_server_exist(host):
    assert azure.is_sql_server_exist(resource_group_name, "eval-sql-server")

def test_sql_elastic_pool_exist(host):
    assert azure.is_sql_elastic_pool_exist(resource_group_name, "eval-sql-server", "eval-pool")

def test_sql_database_exist(host): 
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "aaaaa")
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "bbbbb")
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "ccccc")
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "ddddd")
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "eeeee")
    assert azure.is_sql_database_exist(resource_group_name, "eval-sql-server", "fffff")

def test_sql_elastic_pool_location(host):
    assert azure.is_sql_elastic_pool_location(resource_group_name, "eval-sql-server", "eval-pool", "Japan West")

def test_sql_elatic_pool_edition(host):
    assert azure.is_sql_elatic_pool_edition(resource_group_name, "eval-sql-server", "eval-pool", "Basic")

def test_sql_elastic_pool_dtu(host):
    assert azure.is_sql_elastic_pool_dtu(resource_group_name, "eval-sql-server", "eval-pool", 50)

def test_sql_elastic_pool_storage_max(host):
    assert azure.is_sql_elastic_pool_storage_max(resource_group_name, "eval-sql-server", "eval-pool", 5000)

