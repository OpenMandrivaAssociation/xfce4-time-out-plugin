%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A time-out plugin for the Xfce panel
Name:		xfce4-time-out-plugin
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.0
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-time-out-plugin

%description
A time-out plugin for the Xfce panel.

%prep
%setup -q

%build

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-time-out-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*
