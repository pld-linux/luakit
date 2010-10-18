
%bcond_with	git		# fetch the newest version from git

%if %{with git}
%define git_url		%{?luakit_git_url}%{!?luakit_git_url:git://github.com/mason-larobina/luakit}
%define git_branch	%{?luakit_git_branch}%{!?luakit_git_branch:develop}
%endif

%define		rel	1
Summary:	WebKitGTK+ based browser
Summary(hu.UTF-8):	WebKitGTK+ alapú böngésző
Name:		luakit
Version:	2010.09.24
Release:	%{rel}%{?with_git:.git.%(date +%s)}
License:	GPL v3
Group:		Applications
Source0:	http://github.com/mason-larobina/luakit/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1cf30b806f4758a1def0eabe4c86c1e2
Patch0:		%{name}-make.patch
Patch1:		%{name}-shebang.patch
URL:		http://luakit.org/
%{?with_git:BuildRequires:	git-core}
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	help2man
BuildRequires:	libsoup-devel
BuildRequires:	lua51
BuildRequires:	lua51-devel
Requires:	dmenu
Requires:	wget
Suggests:	ca-certificates
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
%if %{without git}
%setup -qc
mv mason-larobina-%{name}-*/* .
%patch0 -p1
%patch1 -p1
%else
%setup -qcT
git clone -b %{git_branch} %{git_url} .
%{!?luakit_skip_patches:
%patch0 -p1
%patch1 -p1
}
%endif

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
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
