%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       Passwd
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - manipulate password files
Summary(pl):	%{_pearname} - manipulacje na plikach z has³ami
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods to manipulate standard UNIX passwd, .htpasswd and CVS
pserver passwd files.

%description -l pl
Dostarcza metody do manipulacji na standardowych UNIX-owych plikach
passwd, .htpasswd oraz na plikach passwd CVS pserver.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
