Summary:	WMMon monitors the realtime CPU load and system load 
Summary(pl):	WMMon monitoruje obci±¿enie procesora i systemu
Name:		wmmon
Version:	1.0b2
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.xs4all.nl/~warp/files/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://www.xs4all.nl/~warp/files
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

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
%patch -p0

%build
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README HINTS CHANGES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/wmmon.desktop
