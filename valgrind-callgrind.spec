Summary:	Call-graph profiling
Summary(pl.UTF-8):   Profilowanie przy użyciu wykresów wywołań
Name:		valgrind-callgrind
Version:	0.10.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://kcachegrind.sourceforge.net/callgrind-%{version}.tar.bz2
# Source0-md5:	6d8acca6b58b0b72804339d04426d550
Patch0:		%{name}-pld-fuckup.patch
URL:		http://kcachegrind.sourceforge.net/cgi-bin/show.cgi/KcacheGrindDownload
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	valgrind >= 3.1.0
BuildRequires:	which
Requires:	valgrind
Obsoletes:	valgrind-calltree
ExclusiveArch:	%{ix86} %{x8664} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a skin (aka plugin) for Valgrind, a program instrumentation
system for x86-linux. It is based on the cachegrind skin, a cache
simulator from the valgrind core package. It adds call-graph
profiling.

%description -l pl.UTF-8
To jest wtyczka dla Valgrinda - systemu strojenia programów dla
Linuksa na platformie x86. Jest oparty na cachegrind - symulatorze
cache dołączonym do pakietu valgrind. calltree dodaje możliwość
profilowania przy użyciu wykresów wywołań.

%prep
%setup -q -n callgrind-%{version}
#%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/valgrind/*-linux/*
