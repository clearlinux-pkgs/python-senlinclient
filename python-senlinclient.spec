#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-senlinclient
Version  : 0.4.0
Release  : 1
URL      : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-0.4.0.tar.gz
Source0  : http://tarballs.openstack.org/python-senlinclient/python-senlinclient-0.4.0.tar.gz
Summary  : OpenStack Clustering API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-senlinclient-bin
Requires: python-senlinclient-python
BuildRequires : PyYAML-python
BuildRequires : Sphinx-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : futures-python
BuildRequires : hacking
BuildRequires : jsonpatch-python
BuildRequires : jsonpointer-python
BuildRequires : jsonschema-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : openstacksdk-python
BuildRequires : os-client-config-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-dev
BuildRequires : python-glanceclient-python
BuildRequires : python-heatclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python-novaclient-python
BuildRequires : python-openstackclient-python
BuildRequires : python3-dev
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : warlock-python

%description
python-senlinclient
===================
Client library for OpenStack Clustering Service API

%package bin
Summary: bin components for the python-senlinclient package.
Group: Binaries

%description bin
bin components for the python-senlinclient package.


%package python
Summary: python components for the python-senlinclient package.
Group: Default
Requires: PyYAML-python
Requires: openstacksdk-python
Requires: python-heatclient-python
Requires: python-openstackclient-python
Requires: requests-python
Requires: six-python

%description python
python components for the python-senlinclient package.


%prep
%setup -q -n python-senlinclient-0.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/senlin

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
