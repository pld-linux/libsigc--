Summary:	The Typesafe Signal Framework for C++
Summary(pl):	¦rodowisko sygna³ów z kontrol± typów dla C++
Name:		libsigc++
Version:	1.2.1
Release:	1
Epoch:		1
License:	LGPL
Vendor:		Karl E. Nelson <kenelson@ece.ucdavis.edu>
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/libsigc/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4.patch
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsigc++-examples
Conflicts:	%{name} < 1.1.0

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, %{name} is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

%description -l pl
Ta biblioteka jest implementacj± pe³nego systemu callbacków do
u¿ywania w bibliotekach widgetów, interfejsach abstrakcyjnych i
ogólnym programowaniu. Oryginalnie by³a to czê¶æ zestawu widgetów
Gtk--, ale jest teraz oddzieln± bibliotek± ogólniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z mo¿liwo¶ci±
³±czenia abstrakcyjnych callbacków z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterów do ³±czenia ró¿nych
callbacków.

%package devel
Summary:	Development tools for the Typesafe Signal Framework for C++
Summary(pl):	Narzêdzia programistyczne do ¶rodowiska libsig++
Group:		Development/Libraries
Requires:	m4
Requires:	%{name} = %{version}

%description devel
Development tools for the Typesafe Signal Framework for C++.

%description devel -l pl
Narzêdzia programistyczne do ¶rodowiska libsigc++ - sygna³ów z
kontrol± typów.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Summary(pl):	Statyczna biblioteka libsigc++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Typesafe Signal Framework for C++ libraries.

%description static -l pl
Statyczna biblioteka libsigc++ - ¶rodowiska sygna³ów z kontrol± typów.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
rm -f scripts/missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS README IDEAS FEATURES NEWS ChangeLog TODO doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sigc++-*
%{_libdir}/sigc++-*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
