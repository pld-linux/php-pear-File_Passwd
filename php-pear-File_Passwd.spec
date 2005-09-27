%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Passwd
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate password files
Summary(pl):	%{_pearname} - manipulacje na plikach z has³ami
Name:		php-pear-%{_pearname}
Version:	1.1.5
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2821181aa1c1eaeba80c22378ea4c76c
URL:		http://pear.php.net/package/File_Passwd/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Crypt/CHAP.*)'

%description
Provides methods to manipulate standard Unix, SMB server,
AuthUser (.htpasswd), AuthDigest (.htdigest) and CVS pserver password
files.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza metody do manipulacji na standardowych UNIX-owych plikach
passwd, serwera SMB, AuthUser (.htpasswd), AuthDigest (.htdigest) oraz
na plikach passwd CVS pserver.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{name}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
