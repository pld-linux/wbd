Summary:	Shared Whiteboard
Summary(pl):	Sieciowa tablica rysunkowa
Name:		wbd
Version:	1.0ucl3
Release:	1
Group:		X11/Applications/Multimedia
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-COPYRIGHT
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-sys_time_h.patch
Patch2:		%{name}-htonl_arg.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/wbd/
License:	Custom
BuildRequires:	ucl-common-devel
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
WBD is a shared whiteboard, compatible with LBL whiteboard WB.

%description -l pl
WBD to sieciowa tablica rysunkowa, kompatybilna z tablic± LBL --- WB.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} OPTFLAGS="%{!?debug:%{rpmcflags}} %{?debug:-O1 -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install wbd $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} COPYRIGHT

gzip -9nf CHANGES COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* COPYRIGHT*
%attr(755,root,root) %{_bindir}/*
