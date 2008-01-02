%define module  Text-Brew
%define name    perl-%{module}
%define version 0.02
%define release %mkrel 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        An implementation of the Brew edit distance
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module implements the Brew edit distance that is very close to the dynamic
programming technique used for the Wagner-Fischer (and so for the Levenshtein)
edit distance. Please look at the module references below. For more information
about the Brew edit distance see:
http://ling.ohio-state.edu/~cbrew/795M/string-distance.html

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/*/*

