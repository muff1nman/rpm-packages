%global srcname hidapi
%global sum Python wrapper for the hidapi

Name:           python-%{srcname}
Version:        0.7.99.post17
Release:        1%{?dist}
Summary:        %{sum}

License:        GPL
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/75/53/7c6789e1ff820ae9732f117de8658830b3d33420a8ef2de72faa9419d049/hidapi-0.7.99.post17.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel

%description
Python wrapper for the hidapi

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Python wrapper for the hidapi

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python wrapper for the hidapi

%prep 
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*

%changelog
