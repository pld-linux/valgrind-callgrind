Summary:	Call-graph profiling
Summary(pl):	Profilowanie przy u¿yciu wykresów wywo³añ
Name:		valgrind-callgrind
Version:	0.9.10
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://kcachegrind.sourceforge.net/callgrind-%{version}.tar.gz
# Source0-md5:	ddfd883491f7d564dca15a2e9336854f
Patch0:		%{name}-pld-fuckup.patch
URL:		http://kcachegrind.sourceforge.net/cgi-bin/show.cgi/KcacheGrindDownload
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	valgrind >= 2.1.2
Requires:	valgrind
Obsoletes:	valgrind-calltree
ExclusiveArch:	%{ix86}
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
%patch0 -p1

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

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO docs/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_includedir}/*
%{_libdir}/valgrind/*
