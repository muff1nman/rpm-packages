Name:           bitcoin-release       
Version:        2
Release:        1
Summary:        Bitcoin repository configuration

Group:          System Environment/Base 
License:        MIT

URL:            https://www.ringingliberty.com/bitcoin/
Source0:        https://linux.ringingliberty.com/bitcoin/RPM-GPG-KEY-bitcoin
Source1:        bitcoin.repo-el

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >= 7
Requires:      epel-release >= 7


%description
This package contains the Bitcoin repository GPG key as well as configuration
for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-bitcoin

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/bitcoin.repo

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Wed Dec 30 2015 Michael Hampton <bitcoin@ringingliberty.com> 2-1
- Update Requires: RHEL 7 and EPEL 7
- Update URLs to https

* Thu Mar 20 2014 Michael Hampton <bitcoin@ringingliberty.com> 1-6
- Added bitcoin-test and bitcoin-test-source repos

* Mon Dec 9 2013 Michael Hampton <bitcoin@ringingliberty.com> - 1-5
- New signature on GPG key
- Tweak Requires to support future RHEL 7

* Wed Aug 22 2012 Michael Hampton <bitcoin@ringingliberty.com> - 1-4
- EL-specific build with unique filenames

* Fri Jul 27 2012 Michael Hampton <bitcoin@ringingliberty.com> - 1-1
- Initial Package
