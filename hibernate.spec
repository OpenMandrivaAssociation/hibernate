Name:		hibernate
Version:	2.0
Release:	6
License:	GPL
Summary:	Software suspend 2 hibernate script
Group:		System/Base
URL:		http://www.tuxonice.net/
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-3mdv2011.0
+ Revision: 619373
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.0-2mdv2010.0
+ Revision: 437866
- rebuild

* Sun Apr 05 2009 Thomas Backlund <tmb@mandriva.org> 2.0-1mdv2009.1
+ Revision: 364066
- update to 2.0 (for tuxonice-3.0 in kernel-tmb)

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.99-3mdv2009.1
+ Revision: 350615
- 2009.1 rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.99-2mdv2009.1
+ Revision: 350290
- 2009.1 rebuild

* Sat Aug 02 2008 Thomas Backlund <tmb@mandriva.org> 1.99-1mdv2009.0
+ Revision: 260797
- update urls
- update to 1.99

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.97-3mdv2009.0
+ Revision: 246859
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 16 2007 Jérôme Soyer <saispo@mandriva.org> 1.97-1mdv2008.1
+ Revision: 120582
- New realase 1.97

* Wed Sep 26 2007 Danny Tholen <dtholen@mandriva.org> 1.96-1mdv2008.0
+ Revision: 93032
- Update to 1.96 to fix support for the new tuxonice suspend in kernel-tmb
- Drop patch 2 & 3 which have been addressed upstream

* Thu Sep 20 2007 Thomas Backlund <tmb@mandriva.org> 1.93-3mdv2008.0
+ Revision: 91539
- add tuxonice support


* Tue Sep 12 2006 Danny Tholen <obiwan@mailmij.org> 1.93-2mdv2007.0
- Add small comment for people who use fglrx (patch0)
- Fix a bogus error on resume (patch1)
- Add commercial for kernel-multimedia in description

* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.93-1mdv2007.0
- New version 1.93

* Tue Jan 17 2006 Olivier Blin <oblin@mandriva.com> 1.12-3mdk
- revert hibernate2 naming, better fix klaptop not to call hibernate directly

* Tue Jan 10 2006 Olivier Blin <oblin@mandriva.com> 1.12-2mdk
- rename hibernate as hibernate2, since it's for suspend2,
  and that a default hibernate script will be provided in suspend-scripts

* Sun Nov 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- 1.12

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdk
- New release 1.10

* Sat Feb 19 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.05-1mdk 
- first mdk release, based on package from Bernard Blackham (<bernard@blackham.com.au>)

