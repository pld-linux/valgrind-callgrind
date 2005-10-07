Summary:	Call-graph profiling
Summary(pl):	Profilowanie przy u¿yciu wykresów wywo³añ
Name:		valgrind-callgrind
Version:	0.10.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://kcachegrind.sourceforge.net/callgrind-%{version}.tar.gz
# Source0-md5:	3bd2afd50fde7db4bd5a59dcb412d5e7
Patch0:		%{name}-pld-fuckup.patch
URL:		http://kcachegrind.sourceforge.net/cgi-bin/show.cgi/KcacheGrindDownload
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	valgrind >= 3.0.1
BuildRequires:	which
Requires:	valgrind
Obsoletes:	valgrind-calltree
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a skin (aka plugin) for Valgrind, a program instrumentation
system for x86-linux. It is based on the cachegrind skin, a cache
simulator from the valgrind core package. It adds call-graph
profiling.

%description -l pl
To jest wtyczka dla Valgrinda - systemu strojenia programów dla
Linuksa na platformie x86. Jest oparty na cachegrind - symulatorze
cache do³±czonym do pakietu valgrind. calltree dodaje mo¿liwo¶æ
profilowania przy u¿yciu wykresów wywo³añ.

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
%{_libdir}/valgrind/*
