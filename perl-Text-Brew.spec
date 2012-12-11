%define upstream_name    Text-Brew
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An implementation of the Brew edit distance
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the Brew edit distance that is very close to the dynamic
programming technique used for the Wagner-Fischer (and so for the Levenshtein)
edit distance. Please look at the module references below. For more information
about the Brew edit distance see:
http://ling.ohio-state.edu/~cbrew/795M/string-distance.html

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/*/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 664904
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 405618
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-7mdv2009.0
+ Revision: 241987
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-5mdv2008.0
+ Revision: 86969
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-4mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-3mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdk 
- better url
- spec cleanup
- make test in %%check
- don't ship useless empty directories

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk 
- new release
- spec cleanup
- better url

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk
- fix buildrequires in a backward compatible way

* Thu Jun 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk 
- first mdk release

