#!/bin/sh

# testinfra innstall commands
apt-get update
apt-get install python-pip
apt-get install python-py
apt-get install python-pytest
pip install --upgrade pip
pip install testinfra

# use modules azure sdk for python
pip install azure.common.credentials
pip install azure.mgmt.resource
pip install azure.mgmt.network
pip install azure.mgmt.dns
pip install azure.mgmt.compute
pip install azure.mgmt.sql
pip install azure.mgmt.storage
pip install azure.mgmt.containerregistry
pip install azure.graphrbac

# use kubernetes client module
pip install kubernetes
