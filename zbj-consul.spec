%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Consul
Name: zbj-consul
Version: 0.7.5
Release: 1
License: GPL+
Group: Applications/Internet
SOURCE0 : %{name}-%{version}.tar.gz
URL: http://consul.io/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: nmap
Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/mkdir, /usr/bin/chown
Requires(postun): /usr/sbin/userdel, /usr/bin/systemctl

%pre
/usr/bin/mkdir /var/lib/consul
/usr/bin/getent group consul || /usr/sbin/groupadd -r consul
/usr/bin/getent passwd consul || /usr/sbin/useradd -r -d /var/lib/consul -s /sbin/nologin -g consul consul
/usr/bin/chown -R consul:consul /var/lib/consul

%post
/usr/bin/systemctl daemon-reload
# /usr/bin/systemctl enable consul
# /usr/bin/systemctl start consul
# /usr/bin/systemctl status -l consul

%postun
/usr/bin/systemctl stop consul
/usr/bin/systemctl disable consul
# /usr/sbin/userdel consul

%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/consul.d/
/usr/local/sbin/consul
/usr/local/sbin/checkport
/usr/lib/systemd/system/consul.service

%changelog
* Mon Mar 24 2017 Luo Tao <luotao@gmail.com> 0.7.5-1
- Upgrade consul to 0.7.5

* Mon Jan 23 2017 Luo Tao <luotao@gmail.com> 0.7.2-1
- Upgrade consul to 0.7.2

* Thu Oct 16 2016 Luo Tao <luotao@gmail.com> 0.7.0-1
- Upgrade consul to 0.7.0

* Wed Jul 20 2016 Luo Tao <luotao@gmail.com> 0.6.4-1
- Upgrade consul to 0.6.4

* Fri Dec 18 2015 Luo Tao <luotao@gmail.com> 0.6.0-1
- First Build
