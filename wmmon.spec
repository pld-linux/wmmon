Summary: 	WMMon monitors the realtime CPU load and system load 
Summary(pl):	WMMon monitoruje obci±¿enie procesora i systemu
Name: 		wmmon
Version: 	1.0b2
Release: 	3
Copyright: 	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
URL: 		http://www.xs4all.nl/~warp/files
Source: 	http://www.xs4all.nl/~warp/files/wmmon-1.0b2.tar.gz
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
WMMon monitors the realtime CPU load as well the average
system load and gives you some nice additional features too...

WMMon currently provides:

* Realtime CPU 'stress' meter;
* Average systemload, like xload & wmavgload;
* Average systemload graphic is autoscaling;
* Realtime Disk I/O 'stress' meter;
* Average Disk I/O load grapic (autoscaling);
* Realtime total Mem & Swap usage meters;
* System uptime display;
* Realtime cycling through all monitor modes;
* Can lauch 3 user definable commands through ~/.wmmonrc;
* Can be started multiple times;
* Commandline options for help (-h), version (-v),
  start mode (-i & -s) and display (-d);

%description -l pl
WMMon monitoruje aktualne obci±¿enie procesora i zasobów 
systemowych, wy¶wietla ¶rednie warto¶ci obci±¿enia, zawiera
równie¿ wiele innych, ciekawych opcji.

%prep
%setup -q -n %{name}.app

%build
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README HINTS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HINTS,CHANGES}.gz
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.0b2-3]
- modified a bit spec file for PLD use,
- package is FHS 2.0 compliant.

* Fri May 22 1998 Cristian Gafton <gafton@redhat.com>
- package built for PowerTools
