Summary: 	A time-out plugin for the Xfce panel
Name: 		xfce-time-out-plugin
Version: 	0.1.1
Release: 	%mkrel 1
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-time-out-plugin/xfce4-time-out-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A time-out plugin for the Xfce panel.

%prep
%setup -qn xfce4-time-out-plugin-%{version}

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-time-out-plugin

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-time-out-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-time-out-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*
