%define		status		stable
%define		pearname	Horde_Util
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Utility Libraries
Name:		php-horde-Horde_Util
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	68d01146449106c56181d2b4e1e1f759
URL:		https://github.com/horde/horde/tree/master/framework/Util/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-dom
Requires:	php-horde-Horde_Url < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-ctype
Suggests:	php-filter
Suggests:	php-horde-Horde_Imap_Client
Suggests:	php-iconv
Suggests:	php-mbstring
Suggests:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Imap/Client.*)

%description
These classes provide functionality useful for all kind of
applications.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Array.php
%{php_pear_dir}/Horde/Array
%{php_pear_dir}/Horde/Domhtml.php
%{php_pear_dir}/Horde/String.php
%{php_pear_dir}/Horde/Util.php
%{php_pear_dir}/Horde/Variables.php
