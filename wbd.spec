Summary:	Shared Whiteboard
Summary(pl.UTF-8):	Sieciowa tablica rysunkowa
Name:		wbd
Version:	1.0ucl3
Release:	1
License:	custom
Group:		X11/Applications/Multimedia
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	019d97da5d36013386dcd008a43d886f
Source1:	%{name}-COPYRIGHT
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-sys_time_h.patch
Patch2:		%{name}-htonl_arg.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/wbd/
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRequires:	ucl-common-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

%description
WBD is a shared whiteboard, compatible with LBL whiteboard WB.

%description -l pl.UTF-8
WBD to sieciowa tablica rysunkowa, kompatybilna z tablicą LBL --- WB.

%prep
%setup -qn %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wbd $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* COPYRIGHT*
%attr(755,root,root) %{_bindir}/*
