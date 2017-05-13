%define major 2
%define minor 6
%define patchlevel 4 

%global srcname electrum
%global sum A lightweight Bitcoin Client

Name:           %{srcname}
Version:        %{major}.%{minor}.%{patchlevel}
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://electrum.org/
Source0:        https://download.electrum.org/%{version}/Electrum-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  PyQt4-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:       python2
Requires:       python-ecdsa
Requires:       python-slowaes
Requires:       python-dns
Requires:       python-requests
Requires:       python-qrcode
Requires:       protobuf-python
Requires:       python-pbkdf2
Requires:       python-jsonrpclib
Requires:       PyQt4

%if 0%{?fedora}
Recommends:     python2-trezor
%endif

%description
Electrum is an easy to use Bitcoin client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
%setup -q -n Electrum-%{version}

%build
pyrcc4 icons.qrc -o gui/qt/icons_rc.py
%{py2_build}

%install
mkdir -p %{buildroot}/usr/share
%{py2_install}

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Install Desktop file, fix categories
desktop-file-install                                    \
--remove-category="Network"                             \
--add-category="Office"                                 \
--add-category="Finance"                                \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc README.rst RELEASE-NOTES AUTHORS
%license LICENCE
%{_bindir}/electrum
%{_datadir}/pixmaps/electrum.png
%{_datadir}/applications/electrum.desktop
%{python2_sitelib}/*

%changelog
* Tue Apr 26 2016 gyger@fsfe.org - 2.6.4-2
- Fixed for python2 and new packaging requirements.

* Mon Apr 25 2016 gyger@fsfe.org - 2.6.4-1
- Upgrade to new Version.
- Relicenced to MIT.

* Sat Nov 7 2015 gyger@fsfe.org - 2.5.2-1
- Upgrade to new Version.

* Sat Jul 25 2015 gyger@fsfe.org - 2.3.3-1
- Upgrade to new Version. 

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-4
- Add Dependency on Pbkdf2

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-1
- Packaging the Beta Version.

* Wed Jan 28 2015 gyger@fsfe.org - 1.9.8-1
- Initial Packaging for electrum on Fedora
