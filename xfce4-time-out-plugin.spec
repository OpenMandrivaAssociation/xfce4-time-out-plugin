%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A time-out plugin for the Xfce panel
Name: 		xfce4-time-out-plugin
Version: 	1.0.1
Release: 	2
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	perl(XML::Parser)

%description
A time-out plugin for the Xfce panel.

%prep
%setup -q

%build

%configure2_5x
%make

%install
%makeinstall_std 

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/xfce4-time-out-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-3mdv2012.0
+ Revision: 791567
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.0-2
+ Revision: 790059
- Rebuild for xfce 4.10

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 632785
- update to new version 1.0.0
- update url for Source0
- drop old scriplets

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-10mdv2011.0
+ Revision: 615631
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-9mdv2010.1
+ Revision: 543440
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-8mdv2010.0
+ Revision: 446138
- rebuild

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-7mdv2009.1
+ Revision: 349481
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-6mdv2009.1
+ Revision: 295030
- rebuild for new Xfce4.6 beta1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-4mdv2009.0
+ Revision: 256982
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-2mdv2008.1
+ Revision: 110140
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- use upstream name

* Wed Jul 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 51340
- new version

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-1mdv2008.0
+ Revision: 31060
- Import xfce-time-out-plugin

