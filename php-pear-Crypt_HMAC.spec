%define		_class		Crypt
%define		_subclass	HMAC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - A class to calculate RFC 2104 compliant hashes
Summary(pl.UTF-8):	%{_pearname} - klasa licząca hasze zgodne z RFC 2104
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7c9781e32d23ff35754fd7261a3aad39
URL:		http://pear.php.net/package/Crypt_HMAC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Crypt_HMAC-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class to calculate RFC 2104 compliant hashes.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa licząca hasze zgodne z RFC 2104.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
