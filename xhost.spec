#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xhost
Version  : 1.0.7
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/app/xhost-1.0.7.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/xhost-1.0.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xhost-bin
Requires: xhost-doc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xmuu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
xhost is used to manage the list of host names or user names
allowed to make connections to the X server.

%package bin
Summary: bin components for the xhost package.
Group: Binaries

%description bin
bin components for the xhost package.


%package doc
Summary: doc components for the xhost package.
Group: Documentation

%description doc
doc components for the xhost package.


%prep
cd ..
%setup -q -n xhost-1.0.7

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xhost

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
