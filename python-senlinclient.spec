#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-senlinclient
Version  : 1.9.0
Release  : 19
URL      : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.9.0.tar.gz
Source0  : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.9.0.tar.gz
Source99 : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.9.0.tar.gz.asc
Summary  : OpenStack Clustering API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-senlinclient-license = %{version}-%{release}
Requires: python-senlinclient-python = %{version}-%{release}
Requires: python-senlinclient-python3 = %{version}-%{release}
Requires: Babel
Requires: PyYAML
Requires: Sphinx
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: openstacksdk
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-heatclient
Requires: reno
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package license
Summary: license components for the python-senlinclient package.
Group: Default

%description license
license components for the python-senlinclient package.


%package python
Summary: python components for the python-senlinclient package.
Group: Default
Requires: python-senlinclient-python3 = %{version}-%{release}

%description python
python components for the python-senlinclient package.


%package python3
Summary: python3 components for the python-senlinclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-senlinclient package.


%prep
%setup -q -n python-senlinclient-1.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540479334
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-senlinclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-senlinclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-senlinclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
