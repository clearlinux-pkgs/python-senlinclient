#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-senlinclient
Version  : 1.11.0
Release  : 27
URL      : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.11.0.tar.gz
Source0  : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.11.0.tar.gz
Source1 : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-1.11.0.tar.gz.asc
Summary  : OpenStack Clustering API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-senlinclient-license = %{version}-%{release}
Requires: python-senlinclient-python = %{version}-%{release}
Requires: python-senlinclient-python3 = %{version}-%{release}
Requires: Babel
Requires: PyYAML
Requires: keystoneauth1
Requires: openstacksdk
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-heatclient
Requires: requests
Requires: six
BuildRequires : Babel
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : keystoneauth1
BuildRequires : openstacksdk
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-heatclient
BuildRequires : requests
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-senlinclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

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
%setup -q -n python-senlinclient-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566665716
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
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
