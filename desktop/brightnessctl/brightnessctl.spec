Name:           brightnessctl
Version:        0.4
Release:        0%{?dist}
Summary:        Read and control device brightness

License:        MIT
URL:            https://github.com/Hummer12007/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Utility to read and control the display brightness.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
export MODE="4755"
%make_build

%install
%make_install DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3-1
- Upgrade to 0.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Jan 18 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2-1
- Update to 0.2

* Sun Nov 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1_p2-2
- Improvements thanks to Igor review

* Sun Nov 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1_p2-1
- Initial packaging
