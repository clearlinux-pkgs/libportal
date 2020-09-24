#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libportal
Version  : 0.3
Release  : 2
URL      : https://github.com/flatpak/libportal/releases/download/0.3/libportal-0.3.tar.xz
Source0  : https://github.com/flatpak/libportal/releases/download/0.3/libportal-0.3.tar.xz
Summary  : Portal API wrappers
Group    : Development/Tools
License  : LGPL-2.0
Requires: libportal-lib = %{version}-%{release}
Requires: libportal-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : pkgconfig(glib-2.0)

%description
libportal - Flatpak portal library
==================================
libportal provides GIO-style async APIs for most Flatpak portals.

%package dev
Summary: dev components for the libportal package.
Group: Development
Requires: libportal-lib = %{version}-%{release}
Provides: libportal-devel = %{version}-%{release}
Requires: libportal = %{version}-%{release}

%description dev
dev components for the libportal package.


%package doc
Summary: doc components for the libportal package.
Group: Documentation

%description doc
doc components for the libportal package.


%package lib
Summary: lib components for the libportal package.
Group: Libraries
Requires: libportal-license = %{version}-%{release}

%description lib
lib components for the libportal package.


%package license
Summary: license components for the libportal package.
Group: Default

%description license
license components for the libportal package.


%prep
%setup -q -n libportal-0.3
cd %{_builddir}/libportal-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579198320
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libportal
cp %{_builddir}/libportal-0.3/COPYING %{buildroot}/usr/share/package-licenses/libportal/ba8966e2473a9969bdcab3dc82274c817cfd98a1
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libportal/account.h
/usr/include/libportal/background.h
/usr/include/libportal/camera.h
/usr/include/libportal/email.h
/usr/include/libportal/filechooser.h
/usr/include/libportal/inhibit.h
/usr/include/libportal/location.h
/usr/include/libportal/notification.h
/usr/include/libportal/openuri.h
/usr/include/libportal/portal-enums.h
/usr/include/libportal/portal-gtk3.h
/usr/include/libportal/portal-gtk4.h
/usr/include/libportal/portal-helpers.h
/usr/include/libportal/portal.h
/usr/include/libportal/print.h
/usr/include/libportal/remote.h
/usr/include/libportal/screenshot.h
/usr/include/libportal/spawn.h
/usr/include/libportal/trash.h
/usr/include/libportal/updates.h
/usr/include/libportal/wallpaper.h
/usr/lib64/libportal.so
/usr/lib64/pkgconfig/libportal.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libportal/XdpPortal.html
/usr/share/gtk-doc/html/libportal/XdpSession.html
/usr/share/gtk-doc/html/libportal/aux.html
/usr/share/gtk-doc/html/libportal/home.png
/usr/share/gtk-doc/html/libportal/index.html
/usr/share/gtk-doc/html/libportal/left-insensitive.png
/usr/share/gtk-doc/html/libportal/left.png
/usr/share/gtk-doc/html/libportal/libportal-Accounts.html
/usr/share/gtk-doc/html/libportal/libportal-Background.html
/usr/share/gtk-doc/html/libportal/libportal-Camera.html
/usr/share/gtk-doc/html/libportal/libportal-Email.html
/usr/share/gtk-doc/html/libportal/libportal-File.html
/usr/share/gtk-doc/html/libportal/libportal-Location.html
/usr/share/gtk-doc/html/libportal/libportal-Notification.html
/usr/share/gtk-doc/html/libportal/libportal-Open.html
/usr/share/gtk-doc/html/libportal/libportal-Print.html
/usr/share/gtk-doc/html/libportal/libportal-Remote-desktop.html
/usr/share/gtk-doc/html/libportal/libportal-Screencast.html
/usr/share/gtk-doc/html/libportal/libportal-Screenshot.html
/usr/share/gtk-doc/html/libportal/libportal-Session.html
/usr/share/gtk-doc/html/libportal/libportal-Spawn.html
/usr/share/gtk-doc/html/libportal/libportal-Trash.html
/usr/share/gtk-doc/html/libportal/libportal-Updates.html
/usr/share/gtk-doc/html/libportal/libportal-Wallpaper.html
/usr/share/gtk-doc/html/libportal/libportal-XdpParent.html
/usr/share/gtk-doc/html/libportal/libportal.devhelp2
/usr/share/gtk-doc/html/libportal/libportal.html
/usr/share/gtk-doc/html/libportal/right-insensitive.png
/usr/share/gtk-doc/html/libportal/right.png
/usr/share/gtk-doc/html/libportal/style.css
/usr/share/gtk-doc/html/libportal/up-insensitive.png
/usr/share/gtk-doc/html/libportal/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libportal.so.0
/usr/lib64/libportal.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libportal/ba8966e2473a9969bdcab3dc82274c817cfd98a1
