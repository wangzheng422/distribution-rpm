# package rpm for docker distribution

[distribution](https://github.com/distribution/distribution) is a member of cncf, it had rpm long before, but now we can't find the rpm for newest version. So we build a new one for it.

Note: this is a demo, and only build for openshift 4 / rhcos / coreos

# build step

```bash
dnf install -y rpmdevtools rpmlint

git clone https://github.com/wangzheng422/distribution-rpm

cp -r distribution-rpm/rpmbuild ~/rpmbuild

rpmbuild -bb ./rpmbuild/SPECS/docker-distribution.spec

```

# how to use

```bash

wget https://github.com/wangzheng422/distribution-rpm/releases/download/v2.8.1-0/docker-distribution-2.8.1-0.el8.x86_64.rpm

dnf install docker-distribution-2.8.1-0.el8.x86_64.rpm

```

# reference

- [How to create a Linux RPM package](https://www.redhat.com/sysadmin/create-rpm-package)
