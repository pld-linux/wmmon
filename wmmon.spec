Summary: WMMon monitors the realtime CPU load and system load 
%define version 1.0b2
Name: wmmon
Version: %{version}
Release: 2
Copyright: GPL
Group: X Windows/Window Managers
URL: http://www.xs4all.nl/~warp/files
Source: http://www.xs4all.nl/~warp/files/wmmon-1.0b2.tar.gz
BuildRoot: /var/tmp/wmmon-root

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

%prep
%setup -q -n wmmon.app

%build
make -C wmmon

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m 755 wmmon/wmmon $RPM_BUILD_ROOT/usr/X11R6/bin

%files
%defattr(-,root,root)
/usr/X11R6/bin/wmmon
%doc README HINTS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri May 22 1998 Cristian Gafton <gafton@redhat.com>
- package built for PowerTools
