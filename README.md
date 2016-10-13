# 安装 rpm build 环境
./prepare-rpmbuild.sh

# 编译 consul rpm 包，复制到 /www/repo/7/x86_64 目录，然后更新 repo
./build-rpm

# 安装 consul-server，然后验证 consul 是否被成功安装
./verify-install

# UI

wget https://dl.bintray.com/mitchellh/consul/0.4.1_web_ui.zip -O /tmp/webui.zip
mkdir -p /opt/consul && cd /opt/consul && unzip /tmp/webui.zip && mv dist ui
ls /opt/consul/ui
index.html  static/

# rpmbuild
yum install rpm-build make gcc
yum install rpmdevtools rpmlint
rpmdev-setuptree
||
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

# fpm
yum install ruby-devel make gcc
gem install fpm
fpm -s dir -t rpm -v 1.0 -n consul -C consul-server-0.4.1 .
rpm2cpio consul-1.0-1.x86_64.rpm|cpio -idmv
./etc/consul.d/server.json
./usr/bin/consul
./usr/lib/systemd/system/consul.service


# links
http://www.consul.io/docs/agent/options.html

# Verify

getent passwd consul
ps axjf | grep consul
systemctl status -l consul
