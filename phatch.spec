%define name phatch
%define version 0.2.7.1
%define release %mkrel 1

Summary:	Photo Batch Processor
Name:		%{name}
Version:	%{version}
License:	GPLv3+
Group:		Graphics
Release:	%{release}
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
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-inspector.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1.lzma
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-inspector.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg 


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
%{py_puresitedir}/%{name}/lib/linux/nautilusExtension.py


%package doc
Summary:	Documentation for Photo Batch Processor
Group:		Graphics
Requires:	%{name}
%description doc

This package provides the html documentation for Photo Batch Processor.

%files doc
%defattr(-,root,root,-)
%{_datadir}/%{name}/doc/html

#-----------------------------------------------------------------------

%prep

%setup -q -n %{name}-0.2.7

%build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

# Building documentation
cd docs
make html
%__mkdir -p %{buildroot}/%{_datadir}/%{name}/doc
%__mv build/html  %{buildroot}/%{_datadir}/%{name}/doc
cd ..
%find_lang %{name}


%clean
%__rm -rf %{buildroot}
