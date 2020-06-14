%global debug_package %{nil}
%global __strip /bin/true

Name:           libspotify
Version:        12.1.51
Release:        2%{?dist}
Summary:        Libspotify SDK
License:        Proprietary
URL:            https://mopidy.github.io/libspotify-archive/

Source0:        %{url}/%{name}-%{version}-Linux-i686-release.tar.gz
Source1:        %{url}/%{name}-%{version}-Linux-x86_64-release.tar.gz

%description
Build your own personal music streaming applications using the LibSpotify SDK.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%ifarch %{ix86}
%setup -q -n %{name}-%{version}-Linux-i686-release
%endif

%ifarch x86_64
%setup -q -T -b 1 -n %{name}-%{version}-Linux-x86_64-release
%endif

%install
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_mandir}/

cp -a lib/* %{buildroot}%{_libdir}/
cp -a include/* %{buildroot}%{_includedir}/
cp -a share/man3/ %{buildroot}%{_mandir}/

sed -i -e 's|PKG_PREFIX|%{_prefix}|g' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
gzip -9 %{buildroot}%{_mandir}/man3/*

%ldconfig_scriptlets

%files
%license LICENSE licenses.xhtml
%doc README ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%doc share/doc/%{name}/*
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

%changelog
* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 12.1.51-2
- Update URL and source links.

* Sat Feb 17 2018 Simone Caronni <negativo17@gmail.com> - 12.1.51-1
- First build.
