#!/bin/sh

py.test -v azure-services-test.py
py.test -v aaaaaa-vm-test.py
py.test -v bbbbbb-vm-test.py
py.test -v k8s-master-test.py
py.test -v k8s-agent-test.py
