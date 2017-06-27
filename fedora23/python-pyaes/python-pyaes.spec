%global srcname pyaes

%if 0%{?fedora} > 23
%global python2_pkgversion 2
%else
%global python2_pkgversion %{nil}
%endif

Name:		python-%{srcname}
Version:	1.6.0
Release:	3%{?dist}
Summary:	Pure-Python implementation of AES block-cipher and common modes of operation
Group:          Development/Languages
License:	MIT
URL:		https://github.com/ricmoo/%{srcname}
Source0:	https://github.com/ricmoo/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		python-pyaes-0001-Use-relative-imports-during-tests.patch
BuildArch:      noarch

BuildRequires:  python%{python2_pkgversion}-crypto
BuildRequires:  python2-devel
%{?python_provide:%python_provide python%{python2_pkgversion}-%{srcname}}


%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).

%if 0%{!?el7:1}
%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-crypto
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build
%if 0%{!?el7:1}
%py3_build
%endif


%install
%py2_install
%if 0%{!?el7:1}
%py3_install
%endif


%check
%{__python2} tests/test-aes.py
%{__python2} tests/test-blockfeeder.py
%{__python2} tests/test-util.py

%if 0%{!?el7:1}
%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py
%endif


%files -n python%{python2_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/*


%if 0%{!?el7:1}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*
%endif


%changelog
* Mon Jun 26 2017 Andrew DeMaria <lostonamountain@gmail.com> 1.6.0-3
- Dont build python3 package for centos (lostonamountain@gmail.com)

* Sun May 28 2017 Andrew DeMaria <lostonamountain@gmail.com> 1.6.0-2
- Made python2 main package (lostonamountain@gmail.com)
- Fix python version for f23 (lostonamountain@gmail.com)

* Fri Mar 31 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Initial build
