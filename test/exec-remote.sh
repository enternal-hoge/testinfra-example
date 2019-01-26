#!/bin/sh

py.test -v azure-services-test.py
py.test -v aaaaa-vm-test.py --connection=ssh --hosts=hoge-user@X.X.X.X --ssh-config=/home/hoge-user/.ssh/ssh_config
py.test -v bbbbb-vm-test.py --connection=ssh --hosts=hoge-user@X.X.X.X --ssh-config=/home/hoge-user/.ssh/ssh_config
py.test -v k8s-master-test.py --connection=ssh --hosts=hoge-user@X.X.X.X --ssh-config=/home/hoge-user/.ssh/ssh_config
py.test -v k8s-agent-test.py --connection=ssh --hosts=hoge-user@X.X.X.X --ssh-config=/home/hoge-user/.ssh/ssh_config

