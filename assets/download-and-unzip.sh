#!/usr/bin/env bash
CWD=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $CWD

wget https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip
unzip consul_0.7.0_linux_amd64.zip
rm consul_0.7.0_linux_amd64.zip
