%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-file-manager-share

Name:		caja-share
Version:	1.6.0
Release:	2
Summary:	Easy sharing folder via Samba (CIFS protocol)
Group:		Networking/File transfer
License:	GPLv2+
URL:		https://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
Source1:	caja-share-setup-instructions
Source2:	caja-share-smb.conf.example

BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:	mate-common

Requires:	samba

%rename %{oname}

%description
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%prep
%setup -q -n %{oname}-%{version}
cp %{SOURCE1} SETUP


%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static

%make


%install
%makeinstall_std INSTALL='install -p'

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

%find_lang %{oname}


%files -f %{oname}.lang
%doc AUTHORS COPYING README
%{_libdir}/caja/extensions-2.0/*
%{_datadir}/mate-file-manager-share/
%config(noreplace) %{_sysconfdir}/samba/caja-share-smb.conf.example

