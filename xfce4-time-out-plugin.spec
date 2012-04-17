%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A time-out plugin for the Xfce panel
Name: 		xfce4-time-out-plugin
Version: 	1.0.0
Release: 	%mkrel 3
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	libxfcegui4-devel >= 4.8.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-time-out-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A time-out plugin for the Xfce panel.

%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-time-out-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*
