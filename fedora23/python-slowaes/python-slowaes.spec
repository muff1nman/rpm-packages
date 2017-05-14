%global srcname slowaes
%global sum An Implementation of AES in Python

Name:           python-%{srcname}
Version:        0.1a1
Release:        6%{?dist}
Summary:        %{sum}

Group:          Development/Languages
License:        ASL 2.0 
URL:            http://code.google.com/p/%{srcname}
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         slowaes-license.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
A pure Python AES Implementation.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A pure Python AES Implementation.

%prep
%setup -q -n %{srcname}-%{version}

#remove egg-info
rm -rf %{srcname}.egg-info
%patch0 -p1

%build
%py2_build

%install

%py2_install

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

%changelog
* Sat May 13 2017 Andrew DeMaria <lostonamountain@gmail.com> 0.1a1-6
- Package build for el7

* Mon Apr 25 2016 Samuel Gyger <gyger@fsfe.org> - 0.1a1-5
- Added correct versioning for python2
- Use pybuild and pyinstall

* Mon Apr 25 2016 Samuel Gyger <gyger@fsfe.org> - 0.1a1-4
- Added proper license file.

* Sat Feb 14 2015 Samuel Gyger <gyger@fsfe.org> - 0.1a1-3
- Rebuild with proper python2 dependence.

* Sat Feb 07 2015 Samuel Gyger <gygers@fsfe.org> - 0.1a1-2
- Fixed Issues from initial Packaging

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 0.1a1-1
- Created the initial packaging for slowaes 0.1a1 on fedora.
