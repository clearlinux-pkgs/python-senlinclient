#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : python-senlinclient
Version  : 2.1.0
Release  : 34
URL      : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-2.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-2.1.0.tar.gz
Source1  : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-2.1.0.tar.gz.asc
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
Provides: pypi(python_senlinclient)
Requires: pypi(babel)
Requires: pypi(keystoneauth1)
Requires: pypi(openstacksdk)
Requires: pypi(osc_lib)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(python_heatclient)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the python-senlinclient package.


%prep
%setup -q -n python-senlinclient-2.1.0
cd %{_builddir}/python-senlinclient-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594050569
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-senlinclient
cp %{_builddir}/python-senlinclient-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/python-senlinclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-senlinclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
