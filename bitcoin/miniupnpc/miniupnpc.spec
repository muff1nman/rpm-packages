%if 0%{?fedora} >= 18
%global with_python3	1
%global basepy3dir	%(echo ../`basename %{py3dir}`)
%else
%global with_python3	0
%endif
%global major	10
%filter_provides_in %{python_sitearch}/.*\.so$ 

Summary:	Library and tool to control NAT in UPnP-enabled routers
Name:		miniupnpc
Version:	1.9
Release:	7%{?dist}
License:	BSD
Group:		System Environment/Libraries
URL:		http://miniupnp.free.fr/
Source:		http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	python2-devel
# Install headers and add extra file to compilation
# Patch originally from Mageia Linux
Patch0:		%{name}-files.patch
# Do not create libminiupnpc.so.%%{version} and libminiupnpc.so.%%{major} linking to it
Patch1:		%{name}-version.patch
# Link to and find libminiupnpc
Patch2:		%{name}-tests.patch
# http://talosintel.com/reports/TALOS-2015-0035/
Patch3:		%{name}-TALOS-2015-0035.patch
Source1:	USAGE

%description
miniupnpc is an implementation of a UPnP client library, enabling
applications to access the services provided by an UPnP "Internet
Gateway Device" present on the network. In UPnP terminology, it is
a UPnP Control Point.

This package includes upnpc, a UPnP client application for configuring 
port forwarding in UPnP enabled routers.

%package	devel
Summary:	Development files for miniupnpc 
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%package	-n python-%{name}
Summary:	Python interface to %{name}
Group:		System Environment/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	-n python-%{name}
This package contains python interfaces to %{name}.

%if %{with_python3}
%package	-n python3-%{name}
Summary:	Python3 interface to %{name}
Group:		System Environment/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires:	python3-devel

%description	-n python3-%{name}
This package contains python3 interfaces to %{name}.
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3
cp %{SOURCE1} .

sed -i "s|\(\tpython setup.py install\)$|\1 --root=\$(DESTDIR)/|" Makefile
%if %{with_python3}
sed -i "s|\(\tpython3 setup.py install\)$|\1 --root=\$(DESTDIR)/|" Makefile
%endif

# version not updated in setup.py
sed -i 's/"1\.7"/"%{version}"/' setup.py

# Changelog says added -ansi without reason, but that
# breaks C files (python module) using C++ comments
sed -i 's/\(CFLAGS += -ansi\)/#\1/' Makefile

%build
mkdir -p build
pushd build
%cmake					\
	-DUPNPC_BUILD_STATIC=OFF	\
	-DUPNPC_BUILD_TESTS=ON		\
	..
    make upnpc-shared all
popd
make pythonmodule
%if %{with_python3}
make pythonmodule3
%endif
make upnpc-shared

%install
make install DESTDIR=$RPM_BUILD_ROOT -C build
make DESTDIR=$RPM_BUILD_ROOT installpythonmodule
%if %{with_python3}
make DESTDIR=$RPM_BUILD_ROOT installpythonmodule3
%endif
install -D -m644 man3/miniupnpc.3 $RPM_BUILD_ROOT/%{_mandir}/man3/miniupnpc.3
install -D -m 0755 upnpc-shared $RPM_BUILD_ROOT%{_bindir}/upnpc

%check
make CFLAGS="%{optflags} -DMINIUPNPC_SET_SOCKET_TIMEOUT" check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc Changelog.txt
%doc LICENSE
%doc README
%{_libdir}/libminiupnpc.so.%{major}
%{_bindir}/upnpc
%doc USAGE

%files		devel
%{_includedir}/miniupnpc
%{_libdir}/libminiupnpc.so
%{_mandir}/man3/miniupnpc.3*

%files		-n python-%{name}
%{python_sitearch}/miniupnpc-%{version}-py?.?.egg-info
%{python_sitearch}/miniupnpc.so

%if %{with_python3}
%files		-n python3-%{name}
%{python3_sitearch}/miniupnpc-%{version}-py?.?.egg-info
%{python3_sitearch}/miniupnpc*.so
%endif

%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 31 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9-6
- Correct buffer overflow in XML parsing (#1270842, #1270182)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9-1
- Update to latest upstream release (#1062206)
- Correct possible DoS crash vector (patch already in tarball) (#1085618)

* Tue Aug 13 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-1
- Update to latest upstream release (#996357)
- Build extra python3 module

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Domingo Becker <domingobecker@gmail.com> - 1.6-9
- Added upnpc, a client side tool, to the main package.
- Added USAGE file with instructions on how to use upnpc.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-6
- Add Changelog.txt to documentation.
- Correct package version in setup.py.
- Correct rpmlint warning on source rpm.
- Filter provides of private python shared object (817311#c19).

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-5
- Build python module (817311#c14).

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-4
- Use %%name for source and patch names.
- Enable %%check.

* Mon May 7 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-3
- Prefer %%global over %%define.
- Add proper documentation to main package.
- Ensure library is built before making simple test programs.

* Wed May 2 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-2
- Rename package to miniupnpc to match source tarball.
- Add patch to enable build of tests.
- Include manual page to devel package.
- Change License to match LICENSE file.

* Sat Apr 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-1
- Initial libminiupnpc spec.
