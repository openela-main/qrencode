Name:           qrencode
Version:        3.4.4
Release:        5%{?dist}
Summary:        Generate QR 2D barcodes
Summary(fr):    Génère les code-barres en 2D QR

License:        LGPLv2+
URL:            http://fukuchi.org/works/qrencode/
Source0:        http://fukuchi.org/works/qrencode/%{name}-%{version}.tar.bz2

BuildRequires:	chrpath
BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
## For ARM 64 support (RHBZ 926414)
BuildRequires:	autoconf >= 2.69

%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%description -l fr
Qrencode est un logiciel utilitaire utilisant libqrencode pour encoder
les données dans un QR Code et sauvegarde dans une image PNG.


%package        devel
Summary:        QR Code encoding library - Development files
Summary(fr):    Bibliothèque d'encodage QR Code - Fichiers de développement
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.

%description    devel -l fr
Le paquet qrencode-devel contient les bibliothèques et les fichiers d'en-tête
pour le développement d'applications utilisant qrencode.


%package        libs
Summary:        QR Code encoding library - Shared libraries
Summary(fr):    Bibliothèque d'encodage QR Code - Bibliothèque partagée

%description    libs
The qrencode-libs package contains the shared libraries and header files for
applications that use qrencode.

%description    libs -l fr
Le paquet qrencode-libs contient les bibliothèques partagées et les fichiers
d'en-tête pour les applications utilisant qrencode.


%prep
%setup -q


%build
## Rebuild configure scripts for ARM 64 support. (RHBZ 926414)
%{__autoconf}
%configure --with-tests
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT%{_libdir}/libqrencode.la
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/qrencode


%check
cd ./tests
sh test_all.sh

%ldconfig_scriptlets libs


%files
%{_bindir}/qrencode
%{_mandir}/man1/qrencode.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NEWS README TODO
%{_libdir}/libqrencode.so.*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.4-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Peter Gordon <peter@thecodergeek.com> - 3.4.4-1
- Update to new upstream bug-fix release (3.4.4).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 3.4.2-3
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Peter Gordon <peter@thecodergeek.com> - 3.4.2-1
- Update to new upstream release (3.4.2)
  - Fixes a memory leak, string-splitting, and Micro QR encoding bugs.
- Run autoconf in %%build to add ARM 64 (aarch64) to the configure scripts.
- Resolves:  #926414 (qrencode: Does not support aarch64 in f19 and rawhide)
- Update source/homepage URLs.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Fri Sep 21 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-4
- Add libs subpackage (fix RHBZ #856808)

* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-3
- Add French translation in spec file
- Fix incomplete removing Group tags in spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.3.1-1
- update to 3.3.1
- remove "Group" tag in spec file
- fix manfile suffix
- remove patch to fix improper LIBPTHREAD macro in the pkgconfig file:
  - upstream issue

* Sat Feb 25 2012 Peter Gordon <peter@thecodergeek.com> - 3.2.0-3
- Fix applying the LIBPTHREAD patch. (Thanks to Matthieu Saulnier.)

* Thu Feb 23 2012 Peter Gordon <peter@thecodergeek.com> - 3.2.0-2
- Add patch to fix improper LIBPTHREAD macro in the pkgconfig file:
  + fix-LIBPTHREAD-macro.patch
- Resolves: #795582 (qrencode-devel: Malformed pkgconfig file causes build to
  fail ("@LIBPTHREAD@: No such file or directory"))

* Sun Jan 15 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- remove BuildRoot tag in spec file
- remove "rm -rf $RPM_BUILD_ROOT" at the beginning of %%install section
- remove %%clean section
- remove %%defattr lines
- add a joker for libqrencode.so.* files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.1.1-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-4
- Fixed the rpath problem.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-3
- Fixed some small spec mistakes.

* Mon Jul 12 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-2
- Fixed some small errors.

* Thu Jul 08 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 3.1.1-1
- Initial build.
