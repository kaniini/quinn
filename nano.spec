%define name	nano
%define version	2.4.1
%define release	1

Summary	: Pico editor clone with enhancements
Name		: %{name}
Version		: %{version}
Release		: %{release}
License		: GPLv3+
Group		: Applications/Editors
URL		: http://www.nano-editor.org/
Source		: http://www.nano-editor.org/dist/v2.3/%{name}-%{version}.tar.gz
BuildRoot	: %{_tmppath}/%{name}-%{version}-root
BuildRequires	: autoconf, automake, gettext-devel, ncurses-devel, texinfo

%description
GNU nano is a small and friendly text editor.  It aims to emulate the
Pico text editor while also offering a few enhancements.

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR="%{buildroot}" install
#ln -s nano %{buildroot}%{_bindir}/pico
rm -f %{buildroot}%{_infodir}/dir

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO doc/faq.html doc/nanorc.sample
%{_bindir}/*
%{_docdir}/nano/*
%{_mandir}/man*/*
%{_mandir}/fr/man*/*
%{_infodir}/nano.info*
%{_datadir}/locale/*/LC_MESSAGES/nano.mo
%{_datadir}/nano/*
