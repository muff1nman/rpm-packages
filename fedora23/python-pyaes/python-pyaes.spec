%global srcname pyaes


Name:		python-%{srcname}
Version:	1.6.0
Release:	1%{?dist}
Summary:	Pure-Python implementation of AES block-cipher and common modes of operation
Group:          Development/Languages
License:	MIT
URL:		https://github.com/ricmoo/%{srcname}
Source0:	https://github.com/ricmoo/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		python-pyaes-0001-Use-relative-imports-during-tests.patch
BuildArch:      noarch


%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%package -n python2-%{srcname}
Summary:	%{summary}
BuildRequires:  python2-crypto
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-crypto
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
%{__python2} tests/test-aes.py
%{__python2} tests/test-blockfeeder.py
%{__python2} tests/test-util.py

%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/*


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*


%changelog
* Fri Mar 31 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Initial build
