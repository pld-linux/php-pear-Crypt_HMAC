%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	HMAC
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - A class to calculate RFC 2104 compliant hashes
Summary(pl):	%{_pearname} - klasa licz±ca hashe zgodne z RFC 2104
Name:		php-pear-%{_pearname}
Version:	0.9
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
A class to calculate RFC 2104 compliant hashes.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa licz±ca hashe zgodne z RFC 2104.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/*.php
