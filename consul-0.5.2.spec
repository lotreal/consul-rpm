%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Consul
Name: consul
Version: 0.5.2
Release: 2
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
* Thu Mar 5 2015  Luo Tao <luotao@zhubajie.com> 0.5.2-1
- Use ansible config consul <gito:marvin.git/setup/consul.yml>

* Thu Feb 5 2015  Luo Tao <luotao@zhubajie.com> 0.4.1-1
- First Build
