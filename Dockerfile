FROM centos
RUN curl -L http://mirrors.zbjwork.com/repo/repo-install.sh | sh
RUN yum install -y rpm-build rpmdevtools rpmlint make gcc &&  rpmdev-setuptree
