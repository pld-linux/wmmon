Summary:	WMMon monitors the realtime CPU load and system load
Summary(pl.UTF-8):	WMMon monitoruje obciążenie procesora i systemu
Summary(pt_BR.UTF-8):	Applet para monitorar o uso de CPU/Memória/Disco/Swap
Summary(es.UTF-8):	Applet para monitorar el uso de CPU/Memória/Disco/Swap
Name:		wmmon
Version:	1.0b2
Release:	7
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.xs4all.nl/~warp/files/%{name}-%{version}.tar.gz
# Source0-md5:	1b8c780b8c24a6958c69330fef4171df
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://www.xs4all.nl/~warp/files/
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

%description -l pl.UTF-8
WMMon monitoruje aktualne obciążenie procesora i zasobów systemowych,
wyświetla średnie wartości obciążenia, zawiera również wiele innych,
ciekawych opcji.

%description -l pt_BR.UTF-8
Wmmon é o canivete suíço da monitoração. Ele pode mostrar o uso de
CPU, memória, swap, disco e outras informações úteis para o
administrador do sistema. Wmmon é projetado para funcionar com o dock
do WindowMaker.

%description -l es.UTF-8
Wmmon es el cuchillo suizo de la monitoración. Puede visualizar el uso
de CPU, memoria, swap, disco y otras informaciones para los
administradores de sistema. Wmmon se diseña para trabajar con el dock
de WindowMaker.

%prep
%setup -q -n %{name}.app
%patch0 -p0

%build
%{__make} -C %{name} \
	CFLAGS="%{rpmcflags} -Wall" \
	CC="%{__cc}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HINTS CHANGES TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmmon.desktop
