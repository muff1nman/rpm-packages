Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.1.1
Release:	2%{?dist}
License:	GPLv2+
Group:		System Environment/Base
Source0:	https://docs.google.com/uc?export=download&id=0B7CLI-REKbE3UzNtSkRvdHBpdjQ#/%{name}-%{version}.tar.gz
URL:		http://code.google.com/p/exfat/
BuildRequires:	scons

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q

%build
scons CFLAGS="%{optflags}"

%install
scons install DESTDIR=%{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man8/
cp -a dump/dumpexfat.8 %{buildroot}/%{_mandir}/man8/dumpexfat.8
cp -a fsck/exfatfsck.8 %{buildroot}/%{_mandir}/man8/exfatfsck.8
ln -s %{_mandir}/man8/exfatfsck.8 %{buildroot}/%{_mandir}/man8/fsck.exfat.8
cp -a mkfs/mkexfatfs.8 %{buildroot}/%{_mandir}/man8/mkexfatfs.8
ln -s %{_mandir}/man8/mkexfatfs.8 %{buildroot}/usr/share/man/man8/mkfs.exfat.8
cp -a label/exfatlabel.8 %{buildroot}/%{_mandir}/man8/exfatlabel.8

%files
%doc COPYING
%{_bindir}/dumpexfat
%{_bindir}/exfatfsck
%{_bindir}/fsck.exfat
%{_bindir}/mkexfatfs
%{_bindir}/mkfs.exfat
%{_bindir}/exfatlabel
%{_mandir}/man8/*

%changelog
* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 17 2013 TingPing <tingping@tingping.se> - 1.0.1-1
- Initial package

