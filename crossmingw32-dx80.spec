Summary:	MinGW32 binary utility development utilities - DirectX 8.0 API
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne dla MinGW32 - API DirectX 8.0
Name:		crossmingw32-dx80
Version:	8.0
Release:	2
License:	Free (libs), (c) Microsoft Corporation (headers)
Group:		Development/Libraries
# headers are Copyright (C) 19xx Microsoft Corporation - what about license???
# (even if distributable, are they "Free"?!)
Source0:	http://alleg.sourceforge.net/files/dx80_mgw.zip
# Source0-md5:	56989db41e494786220ed4e4788af929
Source1:	http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz
# Source1-md5:	389a36e4d209c0a76bea7d7cb6315315
BuildRequires:	unzip
Requires:	crossmingw32-runtime
Provides:	crossmingw32-dx = 8.0
Obsoletes:	crossmingw32-dx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}

%define		__unzip		unzip -q -o
# strip fails on static COFF files
%define		no_install_post_strip 1

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains DirectX 8.0 API includes and libraries.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nagłówkowe i biblioteki API DirectX 8.0.

%prep
%setup -q -c
mkdir extras
cd extras
tar zxf %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

rm -rf include/src
rm -rf lib/src

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

cp extras/include/directx.h $RPM_BUILD_ROOT%{arch}/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/d3d*.h
%{arch}/include/d3d*.inl
%{arch}/include/ddraw*.h
%{arch}/include/ddstream.h
%{arch}/include/dinput*.h
%{arch}/include/directx.h
%{arch}/include/dls1.h
%{arch}/include/dls2.h
%{arch}/include/dmdls.h
%{arch}/include/dmerror.h
%{arch}/include/dmksctrl.h
%{arch}/include/dmo*.h
%{arch}/include/dmplugin.h
%{arch}/include/dmus*.h
%{arch}/include/dpaddr.h
%{arch}/include/dplay*.h
%{arch}/include/dplobby*.h
%{arch}/include/dsetup.h
%{arch}/include/dshow.h
%{arch}/include/dshowasf.h
%{arch}/include/dsound.h
%{arch}/include/dv.h
%{arch}/include/dvdevcod.h
%{arch}/include/dvdmedia.h
%{arch}/include/dvoice.h
%{arch}/include/dvp.h
%{arch}/include/dx7todx8.h
%{arch}/include/dxerr8.h
%{arch}/include/dxfile.h
%{arch}/include/dxsdk.inc
%{arch}/include/dxtrans.h
%{arch}/include/dxva.h
%{arch}/include/multimon.h
%{arch}/include/rmxfguid.h
%{arch}/include/rmxftmpl.h
%{arch}/lib/libd3d8.a
%{arch}/lib/libd3dx8d.a
%{arch}/lib/libd3dxof.a
%{arch}/lib/libddraw.a
%{arch}/lib/libdinput.a
%{arch}/lib/libdinput8.a
%{arch}/lib/libdplayx.a
%{arch}/lib/libdpnaddr.a
%{arch}/lib/libdpnet.a
%{arch}/lib/libdpnlobby.a
%{arch}/lib/libdpvoice.a
%{arch}/lib/libdsetup.a
%{arch}/lib/libdsound.a
%{arch}/lib/libdxguid.a
