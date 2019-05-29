%define commit 316eac0

Name:           compton
Version:        0.1
Release:        5.20170729%{commit}%{?dist}
Summary:        Compositor for X11

License:        MIT
URL:            https://github.com/chjj/%{name}

# The source for this package was pulled from upstream's vcs.  Use the
# following command to generate the tarball:
# wget -O chjj-compton-%{commit}.tar.gz --no-check-certificate --content-disposition http://github.com/chjj/compton/tarball/%{commit}

Source0:        chjj-%{name}-%{commit}.tar.gz

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: asciidoc
BuildRequires: git
BuildRequires: gcc

BuildRequires: desktop-file-utils

Requires:       xorg-x11-utils

%description
Compton is a compositor for X, and a fork of xcompmgr-dana.

%prep
%autosetup -n chjj-compton-%{commit}

%build
%make_build
make docs

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-trans.1.*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed May 29 2019 Andrew DeMaria <lostonamountain@gmail.com> 0.1-5.20170729316eac0
- Bump release (lostonamountain@gmail.com)
- Add gcc dependency (lostonamountain@gmail.com)

* Wed May 29 2019 Andrew DeMaria <lostonamountain@gmail.com> 0.1-4.20170729316eac0
- Add requires git (lostonamountain@gmail.com)

* Sat Jul 29 2017 Andrew DeMaria <lostonamountain@gmail.com> 0.1-3.20170729316eac0
- Change source name (lostonamountain@gmail.com)

* Fri Jul 28 2017 Andrew DeMaria <lostonamountain@gmail.com> 0.1-1.20170729316eac0
- Updated to 316eac0 (lostonamountain@gmail.com)

* Mon Jan 18 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.1-1
- Initial version of the Compton specfile

