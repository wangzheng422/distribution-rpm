Name:           docker-distribution
Version:        2.8.1
Release:        0%{?dist}
Summary:        package for docker-distribution
ExclusiveArch:  x86_64

License:        GPL
Source0:        src.tar.gz
%undefine _disable_source_fetch
Source1:        https://github.com/distribution/distribution/releases/download/v%{version}/registry_%{version}_linux_amd64.tar.gz

Requires:       bash

%description
package for docker-distribution

%prep
# %setup -q
cp -f %{_sourcedir}/* %{_topdir}/BUILD/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/var/lib/registry
mkdir -p $RPM_BUILD_ROOT/etc/docker-distribution/registry
cp config.yml $RPM_BUILD_ROOT/etc/docker-distribution/registry/
cp docker-distribution.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
tar zxf registry_%{version}_linux_amd64.tar.gz
cp registry $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/registry
/usr/lib/systemd/system/docker-distribution.service
/etc/docker-distribution/registry/config.yml
/var/lib/registry

%changelog
* Fri Sep  09 2022 wangzheng <wangzheng422@gmail.com> - 2.8.1
- First version being packaged