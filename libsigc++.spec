Summary:	The Typesafe Signal Framework for C++
Summary(pl):	¶rodowisko sygna≥Ûw z kontrol± typÛw dla C++
Name:		libsigc++
Version:	1.1.7
Release:	1
Epoch:		1
License:	LGPL
Vendor:		Karl E. Nelson <kenelson@ece.ucdavis.edu>
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Agerasˆfn
Group(it):	Librerie
Group(ja):	•È•§•÷•È•Í
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(sl):	Knjiænice
Group(sv):	Bibliotek
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/libsigc/%{name}-%{version}.tar.gz
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
Ta biblioteka jest implementacj± pe≥nego systemu callbackÛw do
uøywania w bibliotekach widgetÛw, interfejsach abstrakcyjnych i
ogÛlnym programowaniu. Oryginalnie by≥a to czÍ∂Ê zestawu widgetÛw
Gtk--, ale jest teraz oddzieln± bibliotek± ogÛlniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z moøliwo∂ci±
≥±czenia abstrakcyjnych callbackÛw z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterÛw do ≥±czenia rÛønych
callbackÛw.

%package devel
Summary:	Development tools for the Typesafe Signal Framework for C++
Summary(pl):	NarzÍdzia programistyczne do ∂rodowiska libsig++
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	m4
Requires:	%{name} = %{version}

%description devel
Development tools for the Typesafe Signal Framework for C++.

%description devel -l pl
NarzÍdzia programistyczne do ∂rodowiska libsigc++ - sygna≥Ûw z
kontrol± typÛw.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Summary(pl):	Statyczna biblioteka libsigc++
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static Typesafe Signal Framework for C++ libraries.

%description static -l pl
Statyczna biblioteka libsigc++ - ∂rodowiska sygna≥Ûw z kontrol± typÛw.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
rm -f scripts/missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS README IDEAS FEATURES NEWS ChangeLog TODO doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/sigc-config*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/sigc++-*
%{_libdir}/sigc++-*
%{_pkgconfigdir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
