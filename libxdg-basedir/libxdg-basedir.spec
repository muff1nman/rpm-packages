Name:           libxdg-basedir
Version:        1.2.0
Release:        8%{?dist}
Summary:        Implementation of the XDG Base Directory Specifications

Group:          System Environment/Libraries
License:        MIT
URL:            http://n.ethz.ch/student/nevillm/download/libxdg-basedir
Source0:        http://n.ethz.ch/student/nevillm/download/libxdg-basedir/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:         libxdg-basedir-leak.patch


%description
The XDG Base Directory Specification defines where should user files 
be looked for by defining one or more base directories relative in 
with they should be located.

This library implements functions to list the directories according 
to the specification and provides a few higher-level functions.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation files for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildRequires:  doxygen

%description    doc
The %{name}-doc package contains doxygen generated files for
developing applications that use %{name}.


%prep
%setup -q

%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}
make doxygen-run


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


#%check
#make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%defattr(-,root,root,-)
%doc doc/html/

%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 Jon Ciesla <limburgher@gmail.com> - 1.2.0-5
- Patch for memory leak, BZ 1018527.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.0-1
- New upstream, BZ 783762.
- Temporarily disabling make check tests.  Succeeding locally, failing in RPM.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 16 2010 Michal Nowak <mnowak@redhat.com> - 1.1.1-1
- 1.1.1

* Sun May  9 2010 Michal Nowak <mnowak@redhat.com> - 1.1.0-1
- 1.1.0

* Tue Sep  1 2009 Michal Nowak <mnowak@redhat.com> - 1.0.2-1
- 1.0.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  9 2009 Michal Nowak <mnowak@redhat.com> - 1.0.1-2
- removed bogus ownership of %%{_libdir}/pkgconfig/
- "docs" sub-package renamed to "doc"

* Mon Jun  8 2009 Michal Nowak <mnowak@redhat.com> - 1.0.1-1
- 1.0.1
- -devel: require pkgconfig, own %%{_libdir}/pkgconfig/
- -docs: sub-package
- make check tests
- SPEC cleanups

* Thu May  7 2009 Michal Nowak <mnowak@redhat.com> - 1.0.0-1
- 1.0.0

