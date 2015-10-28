Name:     dunst
Version:  1.1.0
Release:  3%{?dist}
Summary:  Simple and configurable notification-daemon
Group:    User Interface/X
License:  BSD and MIT
URL:      http://www.knopwob.org/dunst
Source0:  http://www.knopwob.org/public/dunst-release/%{name}-%{version}.tar.bz2

Requires: dbus

BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXft-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: libnotify-devel
BuildRequires: pango-devel
BuildRequires: cairo-devel
BuildRequires: libpng-devel
BuildRequires: dbus-devel
BuildRequires: /usr/bin/pod2man

Provides: desktop-notification-daemon

%description
Dunst is a highly configurable and lightweight notification daemon with the
similar look and feel to dmenu.


%prep
%setup -q


%build
make %{?_smp_mflags} VERSION=%{version} PREFIX=%{_prefix} EXTRACFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}


%files
%doc AUTHORS CHANGELOG LICENSE README.pod
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/org.knopwob.%{name}.service
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.1.0-2
- Removed unnecessary numlock patch from 1.0.0

* Wed Jan 07 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.1.0-1
- Bumped to version 1.1.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-3
- Backported numlock fix (RHBZ 1103216)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.0.0-1
- bump to stable version 1.0.0

* Mon Jan 28 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.5.0-1
- version bump
- inih library is no longer required

* Mon Sep 03 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-3
- package review

* Wed Aug 29 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-2
- package review

* Mon Aug 27 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-1
- initial version
