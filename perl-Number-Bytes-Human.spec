#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Number-Bytes-Human
Version  : 0.11
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Number-Bytes-Human-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Number-Bytes-Human-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnumber-bytes-human-perl/libnumber-bytes-human-perl_0.11-1.debian.tar.xz
Summary  : 'Convert byte count to human readable format'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Number::Bytes::Human 0.11
* finish docs
* include memoizing
* write a benchmark: unmemoized vs. memoized vs. object
* add test cases for rounding

%package dev
Summary: dev components for the perl-Number-Bytes-Human package.
Group: Development
Provides: perl-Number-Bytes-Human-devel = %{version}-%{release}

%description dev
dev components for the perl-Number-Bytes-Human package.


%prep
%setup -q -n Number-Bytes-Human-0.11
cd ..
%setup -q -T -D -n Number-Bytes-Human-0.11 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Number-Bytes-Human-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Number/Bytes/Human.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::Bytes::Human.3
