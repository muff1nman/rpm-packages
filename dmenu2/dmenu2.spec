Name:           dmenu2
Conflicts:      dmenu
Provides:       dmenu
Version:        0.3
Release:        1%{?dist}
Summary:        Generic menu for X
License:        MIT
URL:            https://github.com/muff1nman/dmenu2
Source0:	https://github.com/muff1nman/%{name}/archive/v%{version}.tar.gz
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel
Requires:       libXft
Requires:       terminus-fonts

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It manages
huge amounts (up to 10.000 and more) of user defined menu items efficiently.

%prep
%autosetup
# Nuke the silent build.
sed -i -e 's|\t@|\t|' Makefile
# Insert optflags.
sed -i -e 's|-Os|%{optflags}|' config.mk
# No strip for debuginfo, and insert ldflags to enhance the security.
sed -i -e 's|-s ${LIBS}|%{?__global_ldflags} ${LIBS}|' config.mk
# X includedir path fix
sed -i -e 's|X11INC = .*|X11INC = %{_includedir}|' config.mk
# libdir path fix
sed -i -e 's|X11LIB = .*|X11LIB = %{_libdir}|' config.mk

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/dmenu*
%{_bindir}/stest
%{_mandir}/man*/dmenu.*
%{_mandir}/man*/stest.*

%changelog
