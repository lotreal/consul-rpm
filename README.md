# UI

wget https://dl.bintray.com/mitchellh/consul/0.4.1_web_ui.zip -O /tmp/webui.zip
mkdir -p /opt/consul && cd /opt/consul && unzip /tmp/webui.zip && mv dist ui
ls /opt/consul/ui
index.html  static/

# Verify

getent passwd consul
ps axjf | grep consul
systemctl status -l consul
