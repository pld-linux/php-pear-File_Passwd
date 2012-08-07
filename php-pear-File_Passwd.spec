%define		_class		File
%define		_subclass	Passwd
%define		_status		stable
%define		_pearname	File_Passwd
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - manipulate password files
Summary(pl.UTF-8):	%{_pearname} - manipulacje na plikach z hasłami
Name:		php-pear-%{_pearname}
Version:	1.1.7
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b11d5dac02ddd93fdfdd4756a0868afe
URL:		http://pear.php.net/package/File_Passwd/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.0.6
Requires:	php-pear
Requires:	php-pear-PEAR-core
Suggests:	php-pear-Crypt_CHAP
Obsoletes:	php-pear-File_Passwd-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Crypt/CHAP.*)'

%description
Provides methods to manipulate standard Unix, SMB server, AuthUser
(.htpasswd), AuthDigest (.htdigest) and CVS pserver password files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza metody do manipulacji na standardowych Uniksowych plikach
passwd, serwera SMB, AuthUser (.htpasswd), AuthDigest (.htdigest) oraz
na plikach passwd CVS pserver.

Ta klasa ma w PEAR status: %{_status}.

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
%dir %{php_pear_dir}/File/Passwd
%{php_pear_dir}/File/*.php
%{php_pear_dir}/File/Passwd/*.php
