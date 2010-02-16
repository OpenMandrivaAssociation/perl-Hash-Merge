%define upstream_name    Hash-Merge
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Merges arbitrarily deep hashes into a single hash
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Clone)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Hash::Merge merges two arbitrarily deep hashes into a single hash. That is,
at any level, it will add non-conflicting key-value pairs from one hash to
the other, and follows a set of specific rules when there are key value
conflicts (as outlined below). The hash is followed recursively, so that
deeply nested hashes that are at the same level will be merged when the
parent hashes are merged. *Please note that self-referencing hashes, or
recursive references, are not handled well by this method.*

Values in hashes are considered to be either ARRAY references, HASH
references, or otherwise are treated as SCALARs. By default, the data
passed to the merge function will be cloned using the Clone module;
however, if necessary, this behavior can be changed to use as many of the
original values as possible. (See 'set_clone_behavior').

Because there are a number of possible ways that one may want to merge
values when keys are conflicting, Hash::Merge provides several preset
methods for your convenience, as well as a way to define you own. These are
(currently):

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


