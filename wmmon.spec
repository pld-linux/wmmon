Summary:	WMMon monitors the realtime CPU load and system load
Summary(pl):	WMMon monitoruje obci±¿enie procesora i systemu
Summary(pt_BR):	Applet para monitorar o uso de CPU/Memória/Disco/Swap
Summary(es):	Applet para monitorar el uso de CPU/Memória/Disco/Swap
Name:		wmmon
Version:	1.0b2
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.xs4all.nl/~warp/files/%{name}-%{version}.tar.gz
# Source0-md5:	1b8c780b8c24a6958c69330fef4171df
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://www.xs4all.nl/~warp/files
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMMon monitors the realtime CPU load as well the average system load
and gives you some nice additional features too...

WMMon currently provides:

- Realtime CPU 'stress' meter;
- Average systemload, like xload & wmavgload;
- Average systemload graphic is autoscaling;
- Realtime Disk I/O 'stress' meter;
- Average Disk I/O load grapic (autoscaling);
- Realtime total Mem & Swap usage meters;
- System uptime display;
- Realtime cycling through all monitor modes;
- Can lauch 3 user definable commands through ~/.wmmonrc;
- Can be started multiple times;
- Commandline options for help (-h), version (-v), start mode (-i &
  -s) and display (-d);

%description -l pl
WMMon monitoruje aktualne obci±¿enie procesora i zasobów systemowych,
wy¶wietla ¶rednie warto¶ci obci±¿enia, zawiera równie¿ wiele innych,
ciekawych opcji.

%description -l pt_BR
Wmmon é o canivete suíço da monitoração. Ele pode mostrar o uso de
CPU, memória, swap, disco e outras informações úteis para o
administrador do sistema. Wmmon é projetado para funcionar com o dock
do WindowMaker.

%description -l es
Wmmon es el cuchillo suizo de la monitoración. Puede visualizar el uso
de CPU, memoria, swap, disco y otras informaciones para los
administradores de sistema. Wmmon se diseña para trabajar con el dock
de WindowMaker.

%prep
%setup -q -n %{name}.app
%patch -p0

%build
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HINTS CHANGES TODO
%attr(755,root,root) %{_bindir}/%{name}

#%%{_applnkdir}/DockApplets/wmmon.desktop
