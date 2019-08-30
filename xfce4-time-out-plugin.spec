%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary: 	A time-out plugin for the Xfce panel
Name: 		xfce4-time-out-plugin
Version: 	1.0.3
Release: 	1
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)

%description
A time-out plugin for the Xfce panel.

%prep
%setup -q

%build

%configure
%make_build

%install
%make_install

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/xfce4-time-out-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*
