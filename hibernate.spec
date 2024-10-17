Name:		hibernate
Version:	2.0
Release:	10
License:	GPL
Summary:	Software suspend 2 hibernate script
Group:		System/Base
URL:		https://www.tuxonice.net/
Source:		http://www.tuxonice.net/downloads/all/%{name}-script-%{version}.tar.gz
Patch0:		hibernate-extra_pages_allowance.patch
BuildArch:	noarch

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

%build

%install
export BASE_DIR=%{buildroot}
export PREFIX=%{_prefix}
export MAN_DIR=$BASE_DIR/%{_mandir}
sh install.sh

%files
%doc CHANGELOG COPYING README SCRIPTLET-API
%{_datadir}/%{name}
%{_mandir}/*/*
%{_sbindir}/hibernate
%config(noreplace) %{_sysconfdir}/%{name}
