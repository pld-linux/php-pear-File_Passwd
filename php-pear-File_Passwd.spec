%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Passwd
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate password files
Summary(pl):	%{_pearname} - manipulacje na plikach z has³ami
Name:		php-pear-%{_pearname}
%define	_pre	b2
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_pre}.tgz
# Source0-md5:	44093594eb4330cd82a345624b60723a
URL:		http://pear.php.net/package/File_Passwd/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods to manipulate standard Unix, SMB server,
AuthUser (.htpasswd), AuthDigest (.htdigest) and CVS pserver password
files.

This class has in PEAR status: %{_status}.

%description -l pl
Dostarcza metody do manipulacji na standardowych UNIX-owych plikach
passwd, serwera SMB, AuthUser (.htpasswd), AuthDigest (.htdigest) oraz
na plikach passwd CVS pserver.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}%{_pre}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}%{_pre}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}%{_pre}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_pre}/tests
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
