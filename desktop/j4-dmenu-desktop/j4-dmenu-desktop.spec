Name:           j4-dmenu-desktop
Version:        2.16
Release:        4%{?dist}
Summary:        Generic menu for X
License:        GPL
URL:            https://github.com/enkore/j4-dmenu-desktop
Source0:        https://github.com/enkore/%{name}/archive/r%{version}.tar.gz
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       terminus-fonts dmenu
# dmenu-4.5 switched to a more generic tool, stest (f17 note)
Obsoletes:      lsx < 0.1-2
Provides:       lsx = 0.1-2

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It manages
huge amounts (up to 10.000 and more) of user defined menu items efficiently.

%prep
%autosetup -n %{name}-r%{version}

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Wed May 29 2019 Andrew DeMaria <lostonamountain@gmail.com> 2.16-4
- Rebuild
* Wed May 29 2019 Andrew DeMaria <lostonamountain@gmail.com> 2.16-3
- Add gcc depends (lostonamountain@gmail.com)

* Sat Jul 07 2018 Andrew DeMaria <lostonamountain@gmail.com> 2.16-2
- Update j4 dmenu (lostonamountain@gmail.com)
- Removed symlink (lostonamountain@gmail.com)

