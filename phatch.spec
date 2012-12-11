%define name 	phatch
%define version 0.2.7.1
%define release 1

Summary:		Photo Batch Processor
Name:		%{name}
Version:		%{version}
License:		GPLv3+
Group:		Graphics
Release:		%{release}
Source:		http://photobatch.stani.be/download/package/%{name}-%{version}.tar.gz
URL:		http://photobatch.stani.be/
BuildRequires:	python-devel >= 2.5
BuildRequires:	desktop-file-utils
BuildRequires:	python-sphinx
BuildRequires:	mlocate
Requires:	findutils
Requires:	python-imaging
Requires:	python-notify
Requires:	wxPythonGTK
Requires:	python-exiv2


%description
Phatch is a simple to use cross-platform GUI Photo Batch Processor
which handles all popular image formats and can duplicate (sub)folder
hierarchies. Phatch can batch resize, rotate, apply perspective,
shadows, rounded corners, ... and more in minutes instead of hours or
days if you do it manually. Phatch allows you to use EXIF and IPTC
tags for renaming and data stamping. Phatch also supports a console
version to batch photos on webservers.


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-inspector.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-inspector.png
%{_iconsdir}/hicolor/*/apps/*
%exclude %{py_puresitedir}/%{name}/lib/linux/nautilusExtension.py
%exclude /usr/share/phatch/doc/html


%package nautilus-bindings
Summary:	Nautilus binding for Photo Batch Processor
Group:		Graphics
Requires:	wxPythonGTK
Requires:	nautilus-python
Requires:	%{name} 
%description nautilus-bindings

This package provides nautilus binding for Photo Batch Processor.

%files nautilus-bindings
%doc AUTHORS COPYING README
%{py_puresitedir}/%{name}/lib/linux/nautilusExtension.py


%package doc
Summary:	Documentation for Photo Batch Processor
Group:		Graphics
Requires:	%{name}
%description doc

This package provides the html documentation for Photo Batch Processor.

%files doc
%{_datadir}/%{name}/doc/html

#-----------------------------------------------------------------------

%prep

%setup -q -n %{name}-0.2.7

%build

%install
python setup.py install --root=%{buildroot}

# Building documentation
cd docs
make html
%__mkdir -p %{buildroot}/%{_datadir}/%{name}/doc
cp -r build/html  %{buildroot}/%{_datadir}/%{name}/doc
cd ..
%find_lang %{name}



%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.2.7.1-1mdv2011.0
+ Revision: 598937
- update file list
- update file list

* Sat Mar 27 2010 John Balcaen <mikala@mandriva.org> 0.2.7.1-1mdv2010.1
+ Revision: 528227
- Fix missing buildrequires
- Update to 0.2.7.1
- fix Filelist
- add a doc subpackage
- add a require on python-exiv2
- minor others changes in spec file

* Sat Jan 02 2010 John Balcaen <mikala@mandriva.org> 0.1.6-2mdv2010.1
+ Revision: 484999
- Add missing requires for wxPythonGTK

* Tue Aug 11 2009 John Balcaen <mikala@mandriva.org> 0.1.6-1mdv2010.0
+ Revision: 414514
- BuildRequires fix
- Add suggest for pyexiv2
- Fixing some requires
- import phatch


* Sat Aug 01 2009 John Balcaen <mikala@mandriva.org>  0.1.6-1mdv2010.0
 - initial import

