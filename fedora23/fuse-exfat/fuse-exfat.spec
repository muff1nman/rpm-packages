Name:           fuse-exfat
Summary:        Free exFAT file system implementation
Version:        1.1.0
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Source0:        https://docs.google.com/uc?export=download&id=0B7CLI-REKbE3VTdaa0EzTkhYdU0#/%{name}-%{version}.tar.gz
URL:            http://code.google.com/p/exfat/
BuildRequires:  fuse-devel
BuildRequires:  scons

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q

%build
scons CFLAGS="%{optflags}"

%install
scons install DESTDIR=%{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8/
cp -a fuse/mount.exfat-fuse.8 %{buildroot}%{_mandir}/man8/mount.exfat-fuse.8
ln -s %{_mandir}/man8/mount.exfat-fuse.8 %{buildroot}%{_mandir}/man8/mount.exfat.8

%files
%doc COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/*

%changelog
* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.0-1
- Update to 1.1.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 17 2013 TingPing <tingping@tingping.se> - 1.0.1-1
- Initial package

