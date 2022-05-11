%bcond_without	luajit		# use lua interpreter

%ifnarch %{ix86} %{x8664} %{arm} aarch64 mips mips64 mipsel ppc
%undefine	with_luajit
%endif

Summary:	WebKitGTK+ based browser
Summary(hu.UTF-8):	WebKitGTK+ alapú böngésző
Summary(pl.UTF-8):	Przeglądarka oparta na WebKitGTK+
Name:		luakit
Version:	2.3
Release:	1
Epoch:		1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/luakit/luakit/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	056187ee95e0ac6eff84f7ff9fd2ed51
Patch0:		%{name}-shebang.patch
URL:		http://luakit.org/
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-webkit4-devel
%if %{with luajit}
BuildRequires:	luajit
BuildRequires:	luajit-devel
%else
BuildRequires:	lua51
BuildRequires:	lua51-devel
%endif
BuildRequires:	lua51-filesystem
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
luakit is a highly configurable, micro-browser framework based on the
WebKit web content engine and the GTK+ toolkit. It is very fast,
extensible by Lua.

%description -l hu.UTF-8
luakit egy magas szinten konfigurálható, micro-böngésző keretrendszer
WebKit motorral és GTK+ grafikus felületettel. Nagyon gyors, és Lua
nyelven bővíthető.

%description -l pl.UTF-8
luakit jest wysoko konfigurowalnym frameworkiem mikro-przeglądarki
opartym na silniku webowym WebKit oraz GTK+. Jest szybki i
rozszeezalny przez Lua.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}/luakit \
	MANPREFIX=%{_mandir} \
	PIXMAPDIR=%{_pixmapsdir} \
	APPDIR=%{_desktopdir} \
	%{?with_luajit:USE_LUAJIT=1 LUA_BIN_NAME="/usr/bin/luajit -O2"} \
	%{!?with_luajit:USE_LUAJIT=0 LUA_BIN_NAME="/usr/bin/lua5.1"}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/luakit

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
        LIBDIR=%{_libdir}/luakit \
        MANPREFIX=%{_mandir} \
        PIXMAPDIR=%{_pixmapsdir} \
        APPDIR=%{_desktopdir} \

if [ "%{_prefix}/lib" != "%{_libdir}" ]; then
	%{__mv} $RPM_BUILD_ROOT%{_prefix}/lib/luakit/luakit.so $RPM_BUILD_ROOT%{_libdir}/luakit
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md

%dir %{_sysconfdir}/xdg/luakit
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/luakit/*.lua
%attr(755,root,root) %{_bindir}/luakit
%dir %{_libdir}/luakit
%attr(755,root,root) %{_libdir}/luakit/luakit.so
%{_datadir}/luakit
%{_pixmapsdir}/luakit.png
%{_mandir}/man1/luakit.1*
%{_desktopdir}/luakit.desktop
