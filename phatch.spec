%define name phatch
%define version 0.1.6
%define release %mkrel 1

Summary:	Photo Batch Processor
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Graphics
Release:	%{release}
Source:		http://sd-2469.dedibox.fr/photobatch/download/package/%{name}-%{version}.tar.gz
URL:		http://photobatch.stani.be/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:  python-devel >= 2.5
BuildRequires:  desktop-file-utils
Requires:	findutils
Requires:	python-imaging
Suggests:	python-exiv2


%description
Phatch is a simple to use cross-platform GUI Photo Batch Processor
which handles all popular image formats and can duplicate (sub)folder
hierarchies. Phatch can batch resize, rotate, apply perspective,
shadows, rounded corners, ... and more in minutes instead of hours or
days if you do it manually. Phatch allows you to use EXIF and IPTC
tags for renaming and data stamping. Phatch also supports a console
version to batch photos on webservers.


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1.lzma
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%package nautilus-bindings
Summary:	Nautilus binding for Photo Batch Processor
Group:		Graphics
Requires:	wxPythonGTK
Requires:	nautilus-python
Requires:	%{name}
%description nautilus-bindings

This package provides nautilus binding for Photo Batch Processor.

%files nautilus-bindings
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/nautilus/extension-2.0/python/phatch_image_inspector.py
%{_libdir}/nautilus/extension-2.0/python/phatch_recent.py

%prep

%setup -q

%build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

# Creating directory for nautilus bindings and moving files

%__mkdir -p %{buildroot}/%{_libdir}/nautilus/extension-2.0/python
%__mv %{buildroot}/%{_prefix}/phatch_*.py %{buildroot}/%{_libdir}/nautilus/extension-2.0/python

%find_lang %{name}


%clean
%__rm -rf %{buildroot}

%changelog
* Sat Aug 01 2009 John Balcaen <mikala@mandriva.org>  0.1.6-1mdv2010.0
 - initial import

