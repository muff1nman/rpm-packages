%global srcname pbkdf2
%global sum A module for a password-based key derivation function

Name:           python-%{srcname}
Version:        1.3
Release:        5%{?dist}
Summary:        %{sum}
Group:          Development/Languages
License:        MIT
URL:            https://www.dlitz.net/software/python-%{srcname}/
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         pbkdf2-license.patch

BuildArch:      noarch
BuildRequires:  python2-devel

%if 0%{!?el7:1}
BuildRequires:  python3-devel
%endif

%description
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%if 0%{!?el7:1}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A pure Python Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.
%endif

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

#remove egg-info
rm -rf %{srcname}.egg-info

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

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)
 
%files -n python2-%{srcname}
%doc PKG-INFO
%license LICENSE
%{python2_sitelib}/*

%if 0%{!?el7:1}
%files -n python%{python3_pkgversion}-%{srcname}
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
* Sat May 13 2017 Andrew DeMaria <lostonamountain@gmail.com> 1.3-5
- Added build for el7

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-4
- Build for python2 and python3
- Use pybuild and pyinstall

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-3
- Added proper license file and fixed license

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-2
- Fixed to be only for python2

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-1
- Created the initial packaging for pkbdf2 on fedora.
