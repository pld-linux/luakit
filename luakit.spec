Summary:	WebKitGTK+ based browser
Summary(hu.UTF-8):	WebKitGTK+ alapú böngésző
Name:		luakit
Version:	2010.08.30
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://github.com/mason-larobina/luakit/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fb3a489988d3d2bd47671f13ecf5a6d7
Patch0:		%{name}-make.patch
URL:		http://luakit.org
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	lua51-devel
Requires:	dmenu
Requires:	halp2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
luakit is a highly configurable, micro-browser framework based on the
WebKit web content engine and the GTK+ toolkit. It is very fast,
extensible by Lua.

%description  -l hu.UTF-8
luakit egy magas szinten konfigurálható, micro-böngésző keretrendszer
WebKit motorral és GTK+ grafikus felületettel. Nagyon gyors, és Lua
nyelven bővíthető.

%prep
%setup -qc
mv mason-larobina-%{name}-*/* .

%patch0 -p1

%build
CFLAGS='%{rpmcflags}' \
LDFLAGS='%{rpmldflags}' \
PREFIX=%{_prefix} \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
PREFIX=%{_prefix} \
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING PATCHES README.md

%dir %{_sysconfdir}/xdg/luakit
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/luakit/*.lua
%attr(755,root,root) %{_bindir}/luakit
%{_datadir}/luakit
%{_pixmapsdir}/luakit.png
%{_mandir}/man1/luakit.1*
%{_desktopdir}/luakit.desktop
