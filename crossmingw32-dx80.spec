Summary:	Mingw32 GNU binary utility development utilities - DirectX 8.0 API
Summary(pl):	Skro�ne narz�dzia programistyczne GNU dla Mingw32 - API DirectX 8.0
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
URL:		http://www.mingw.org/
BuildRequires:	unzip
Requires:	crossmingw32-runtime
Provides:	crossmingw32-w32api-dx
Obsoletes:	crossmingw32-w32api-dx
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
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains DirectX 8.0 API includes and libraries.

%description -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro�nej,
pozwalaj�cym budowa� aplikacje MS Windows pod Linuksem u�ywaj�c
bibliotek mingw32. System sk�ada si� z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj�ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nag��wkowe i biblioteki API DirectX 8.0.

%prep
%setup -q -c
mkdir extras
cd extras
tar zxf %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

rm -rf lib/src

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

cp extras/include/directx.h $RPM_BUILD_ROOT%{arch}/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*
%{arch}/lib/*