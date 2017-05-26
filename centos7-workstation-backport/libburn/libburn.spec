Name:           libburn
Version:        1.2.8
Release:        4%{?dist}
Summary:        Library for reading, mastering and writing optical discs

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://libburnia-project.org/
Source0:        http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
Patch0:         libburn-multilib_doc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libtool intltool gettext doxygen graphviz


%description
Libburn is an open-source library for reading, mastering and writing
optical discs. For now this means only CD-R and CD-RW.

The project comprises of several more or less interdependent parts which
together strive to be a usable foundation for application development.
These are libraries, language bindings, and middleware binaries which emulate
classical (and valuable) Linux tools.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     cdrskin
Summary:        Limited cdrecord compatibility wrapper to ease migration to libburn
Group:          Applications/Multimedia
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some libburn 
features from the command line.


%prep
%setup -q
%patch0 -p1 -b .multilibdoc
echo "<!-- empty html footer do defeat multilib conflicts - do not insert current time -->" > doc/empty_footer.html
#overwrite old autoconf scripts which do not recognize aarch64
autoreconf -vfi

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
doxygen doc/doxygen.conf


%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT README
%{_libdir}/%{name}*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%doc doc/html

%files -n cdrskin
%defattr(-,root,root,-)
%{_mandir}/*/*
%{_bindir}/cdrskin


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.2.8-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.8-3
- Mass rebuild 2013-12-27

* Tue Apr 02 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.2.8-2
- Run autoreconf to overwrite old scripts => recognize aarch64

* Tue Mar 19 2013 Robert Scheck <robert@fedoraproject.org> 1.2.8-1
- Update to upstream 1.2.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Robert Scheck <robert@fedoraproject.org> 1.2.6-1
- Update to upstream 1.2.6 (#893692)

* Wed Dec 05 2012 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.2.4-5
- renamed patch - added package name to match naming guidelines

* Tue Dec 04 2012 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.2.4-4
- current time in doxygen footer caused multilib difference - inserted empty footer instead

* Thu Nov 22 2012 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.2.4-3
- Minor spec-file cleanup

* Wed Aug 29 2012 Honza Horak <hhorak@redhat.com> 1.2.4-2
- Changed license from GPLv2 to GPLv2+ to correspond with source

* Fri Aug 10 2012 Robert Scheck <robert@fedoraproject.org> 1.2.4-1
- Update to upstream 1.2.4 (#842077)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Robert Scheck <robert@fedoraproject.org> 1.2.2-1
- Update to upstream 1.2.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Robert Scheck <robert@fedoraproject.org> 1.1.8-1
- Update to upstream 1.1.8

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 1.1.6-1
- Update to upstream 1.1.6

* Sun Sep 18 2011 Robert Scheck <robert@fedoraproject.org> 1.1.4-1
- Update to upstream 1.1.4

* Sun Jul 10 2011 Robert Scheck <robert@fedoraproject.org> 1.1.0-1
- Update to upstream 1.1.0

* Sun Apr 17 2011 Robert Scheck <robert@fedoraproject.org> 1.0.6-1
- Update to upstream 1.0.6

* Mon Feb 28 2011 Honza Horak <hhorak@redhat.com> - 1.0.2-1
- Update to upstream 1.0.2

* Thu Feb 17 2011 Honza Horak <hhorak@redhat.com> - 1.0.0-1
- Update to upstream 1.0.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 22 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 0.8.0-1
- Update to upstream 0.8.0

* Wed Sep 30 2009 Denis Leroy <denis@poolshark.org> - 0.7.0-1
- Update to upstream 0.7.0
- Fixed binary installation
- Removed rpath

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Denis Leroy <denis@poolshark.org> - 0.6.0-2
- Updating to pl01 tarball from upstream
- Fixed project URL

* Wed Jan 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.0-1
- New upstream version

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.8-2
- fix license tag

* Wed Jun 11 2008 Denis Leroy <denis@poolshark.org> - 0.4.8-1
- Update to upstream 0.4.8

* Thu Feb 14 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-2
- Autorebuild for GCC 4.3

* Thu Dec 13 2007 Denis Leroy <denis@poolshark.org> - 0.4.0-1
- Update to 0.4.0

* Wed Oct 10 2007 Jesse Keating <jkeating@redhat.com> - 0.3.8-2
- Rebuild for BuildID

* Fri Aug 10 2007 Denis Leroy <denis@poolshark.org> - 0.3.8-1
- Update to upstream 0.3.8
- Fixed project URL

* Sun Mar 25 2007 Denis Leroy <denis@poolshark.org> - 0.2.6.3-3
- Fixed unowned include directory (#233860)

* Tue Mar 20 2007 Denis Leroy <denis@poolshark.org> - 0.2.6.3-2
- Moved documentation into devel package, #228372
- Updated source URL to new upstream location

* Tue Jan 02 2007 Jesse Keating <jkeating@redhat.com> - 0.2.6.3-1
- Update to 0.2.6.3
- Remove libisofs stuff as it's packaged seperately now.
- Add a manpage for cdrskin

* Sat Oct 21 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2-2
- Point to a real URL in source, now that we have a tarball

* Fri Oct 20 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2-1
- 0.2.2 release

* Tue Sep 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2-5.20060808svn
- Create doxygen docs

* Fri Sep  8 2006 Jesse Keating <jkeating@redhat.com> - 0.2-4.20060808svn
- rebuild with new snapshot

* Sun Aug 27 2006 Jesse Keating <jkeating@redhat.com> - 0.2-3.20060823svn
- don't install dupe headers in -devel packages
- libisofs requires libburn devel for directory ownership

* Sun Aug 27 2006 Jesse Keating <jkeating@redhat.com> - 0.2-2.20060823svn
- Fix cdrskin require
- Fix tabs
- Added doc files

* Wed Aug 23 2006 Jesse Keating <jkeating@redhat.com> - 0.2-1.20060823svn
- Initial package for review