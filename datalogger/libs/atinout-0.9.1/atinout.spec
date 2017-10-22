Name:           atinout
Version:        0.9.1
Release:        1%{?dist}
Summary:        AT commands as input are sent to modem and responses given as output
Group:          Applications/Communications
License:        GPLv3+
URL:            http://atinout.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%global _hardened_build 1

%description
This program will read a file (or stdin) containing a list of AT
commands. Each command will be send to the modem, and all the response
for the command will be output to file (or stdout).

Example, to hang up any ongoing call:

$ echo ATH | atinout - /dev/ttyACM0 -
ATH
OK
$

%prep
%setup -q

%build

make all %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/atinout
%doc %{_mandir}/man1/atinout.1.gz
%doc README atinout.1.html gplv3.txt logo/atinout.svg


%changelog
* Sun Sep  8 2013 Håkon Løvdal <hlovdal@users.sourceforge.net> - 0.9.1-1
- Add RPM spec file, "rpmbuild -ta atinout-0.9.1.tar.gz" will work.
- Fix Makefile so that it works without problems when compiling source
  from tar file (git source was always ok).
- Fixed test checking wrong file when testing if opnening it was ok.

* Wed Apr 24 2013 Håkon Løvdal <hlovdal@users.sourceforge.net> - 0.9-1
- Initial release.
