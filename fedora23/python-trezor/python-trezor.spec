%global srcname trezor
%global sum A library to support trezor via python

Name:           python-%{srcname}
Version:        0.7.0
Release:        5%{?dist}
Summary:        %{sum}

License:        LGPL
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/%{srcname}/python-%{srcname}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
Requires:       python2-hidapi python3-hidapi
Requires:       python2-mnemonic python3-mnemonic
Requires:       protobuf-python
Requires:       python3-ecdsa python-ecdsa
# For test
BuildRequires:  python2-hidapi python3-hidapi python-ecdsa python3-ecdsa protobuf-python python2-mnemonic python3-mnemonic


%description
A python module for trezor.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A python module for trezor.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A python module for trezor.

%prep 
%autosetup -n python-%{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license COPYING
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/trezorctl

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/trezorctl

%changelog
