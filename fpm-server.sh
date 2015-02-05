NAME=consul-server
VERSION=0.4.1
PKG=${NAME}-${VERSION}
ROOT=build/$PKG

[ -d $ROOT ] && rm -r $ROOT

mkdir -p $ROOT
mkdir -p $ROOT/usr/bin
mkdir -p $ROOT/etc/consul.d
mkdir -p $ROOT/usr/lib/systemd/system

install -m 755 src/consul-${VERSION}/consul $ROOT/usr/bin
install -m 644 etc/consul.d/server.json $ROOT/etc/consul.d
install -m 644 consul.service $ROOT/usr/lib/systemd/system

cd build
tar -zcvf ${PKG}.tar.gz ${PKG}

cd ..

cp build/${PKG}.tar.gz ~/rpmbuild/SOURCES/
cp ${NAME}.spec ~/rpmbuild/SPECS/

rpmbuild -ba ~/rpmbuild/SPECS/${NAME}.spec

yum remove -y ${NAME}
yum localinstall ~/rpmbuild/RPMS/x86_64/${PKG}-3.x86_64.rpm
rpm -ql ${NAME}
