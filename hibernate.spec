%define name	hibernate
%define version 2.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Summary:	Software suspend 2 hibernate script
Group:		System/Base
URL:		http://www.tuxonice.net/
Source:		http://www.tuxonice.net/downloads/all/%{name}-script-%{version}.tar.gz
Patch0:		hibernate-extra_pages_allowance.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at http://www.tuxonice.net/,
which are also included in the kernel-tmb package.

After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%prep
%setup -q -n %{name}-script-%{version}

%patch0 -p1

%install
rm -rf %{buildroot}
export BASE_DIR=%{buildroot}
export PREFIX=%{_prefix}
export MAN_DIR=$BASE_DIR/%{_mandir}
sh install.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING README SCRIPTLET-API
%{_datadir}/%{name}
%{_mandir}/*/*
%{_sbindir}/hibernate
%config(noreplace) %{_sysconfdir}/%{name}

