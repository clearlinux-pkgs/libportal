#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libportal
Version  : 0.6
Release  : 7
URL      : https://github.com/flatpak/libportal/releases/download/0.6/libportal-0.6.tar.xz
Source0  : https://github.com/flatpak/libportal/releases/download/0.6/libportal-0.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: libportal-data = %{version}-%{release}
Requires: libportal-lib = %{version}-%{release}
Requires: libportal-license = %{version}-%{release}
Requires: xdg-desktop-portal
BuildRequires : buildreq-kde
BuildRequires : buildreq-meson
BuildRequires : gtk-doc
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk4)
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libportal - Flatpak portal library
==================================
libportal provides GIO-style async APIs for most Flatpak portals. You can find
the documentation [here](https://flatpak.github.io/libportal/).

%package data
Summary: data components for the libportal package.
Group: Data

%description data
data components for the libportal package.


%package dev
Summary: dev components for the libportal package.
Group: Development
Requires: libportal-lib = %{version}-%{release}
Requires: libportal-data = %{version}-%{release}
Provides: libportal-devel = %{version}-%{release}
Requires: libportal = %{version}-%{release}

%description dev
dev components for the libportal package.


%package extras
Summary: extras components for the libportal package.
Group: Default

%description extras
extras components for the libportal package.


%package lib
Summary: lib components for the libportal package.
Group: Libraries
Requires: libportal-data = %{version}-%{release}
Requires: libportal-license = %{version}-%{release}

%description lib
lib components for the libportal package.


%package license
Summary: license components for the libportal package.
Group: Default

%description license
license components for the libportal package.


%prep
%setup -q -n libportal-0.6
cd %{_builddir}/libportal-0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680015681
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocs=false \
-Dtests=false  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libportal
cp %{_builddir}/libportal-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libportal/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Xdp-1.0.typelib
/usr/lib64/girepository-1.0/XdpGtk3-1.0.typelib
/usr/lib64/girepository-1.0/XdpGtk4-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libportal-gtk3.deps
/usr/share/vala/vapi/libportal-gtk3.vapi
/usr/share/vala/vapi/libportal-gtk4.deps
/usr/share/vala/vapi/libportal-gtk4.vapi
/usr/share/vala/vapi/libportal.deps
/usr/share/vala/vapi/libportal.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libportal-gtk3/portal-gtk3.h
/usr/include/libportal-gtk4/portal-gtk4.h
/usr/include/libportal-qt5/portal-qt5.h
/usr/include/libportal/account.h
/usr/include/libportal/background.h
/usr/include/libportal/camera.h
/usr/include/libportal/dynamic-launcher.h
/usr/include/libportal/email.h
/usr/include/libportal/filechooser.h
/usr/include/libportal/inhibit.h
/usr/include/libportal/location.h
/usr/include/libportal/notification.h
/usr/include/libportal/openuri.h
/usr/include/libportal/parent.h
/usr/include/libportal/portal-enums.h
/usr/include/libportal/portal-helpers.h
/usr/include/libportal/portal.h
/usr/include/libportal/print.h
/usr/include/libportal/remote.h
/usr/include/libportal/screenshot.h
/usr/include/libportal/spawn.h
/usr/include/libportal/trash.h
/usr/include/libportal/types.h
/usr/include/libportal/updates.h
/usr/include/libportal/wallpaper.h
/usr/lib64/libportal-gtk3.so
/usr/lib64/libportal-gtk4.so
/usr/lib64/libportal-qt5.so
/usr/lib64/libportal.so
/usr/lib64/pkgconfig/libportal-gtk3.pc
/usr/lib64/pkgconfig/libportal-gtk4.pc
/usr/lib64/pkgconfig/libportal-qt5.pc
/usr/lib64/pkgconfig/libportal.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libportal-qt5.so.1
/usr/lib64/libportal-qt5.so.1.0.0

%files lib
%defattr(-,root,root,-)
/usr/lib64/libportal-gtk3.so.1
/usr/lib64/libportal-gtk3.so.1.0.0
/usr/lib64/libportal-gtk4.so.1
/usr/lib64/libportal-gtk4.so.1.0.0
/usr/lib64/libportal.so.1
/usr/lib64/libportal.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libportal/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
