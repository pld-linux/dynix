Summary:	A dyn.ee client for *x operating systems
Name:		dynix
Version:	0.60
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/System
Source0:	http://www.dyn.ee/software/%{name}/%{name}%{version}.tgz
# Source0-md5:	2bdf63d7580143f6ccb431f954600afe
Patch0:		%{name}-dyn.ee.patch
URL:		http://www.dyn.ee/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynix was created to provide more comfortable and flexible ways to use dyn.ee
and dynserv ddns service. Version updates are released whenever some bigger
bugs are found and fixed or when dynserv introduces new features.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p0

%build
%{__cc} %{rpmcflags} -Wall %{name}.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dynix.readme
%attr(755,root,root) %{_sbindir}/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
