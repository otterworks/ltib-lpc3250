%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A Portable Foreign Function Interface Library
Name            : libffi
Version         : 3.2.1
Release         : 3
License         : https://github.com/libffi/libffi/blob/master/LICENSE
Vendor          : ow
Packager        : mjs
Group           : xxxx
URL             : https://sourceware.org/libffi/
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build

./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-static
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
