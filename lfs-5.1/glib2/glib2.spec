%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A library of functions used by GDK, GTK+, and many applications
Name            : glib2
Version         : 2.43.3
#Version         : 2.58.3
Release         : 1
License         : LGPL
Vendor          : ow
Packager        : mjs
Group           : System Environment/Libraries
Source          : glib-%{version}.tar.xz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
Requires        : libffi

%Description
%{summary}

%Prep
%setup -n glib-%{version}
#TODO# need to: wget https://gist.githubusercontent.com/bluesquall/4272351e021a5fce3c42/raw/faac3dc9ba61a9b35946cb96669437adf68d3a27/lpc3250-glib2.cache

%Build
#./configure --cache-file=lpc3250.cache \
# prevent configure from trying to compile and
# run test binaries for the target.
glib_cv_long_long_format=ll \
glib_cv_stack_grows=no \
glib_cv_sane_realloc=yes \
glib_cv_have_strlcpy=no \
glib_cv_va_val_copy=yes \
glib_cv_rtldglobal_broken=no \
glib_cv_uscore=no \
glib_cv_monotonic_clock=no \
ac_cv_func_nonposix_getpwuid_r=no \
ac_cv_func_posix_getpwuid_r=yes \
ac_cv_func_posix_getgrgid_r=yes \
glib_cv_use_pid_surrogate=yes \
ac_cv_func_printf_unix98=no \
ac_cv_func_vsnprintf_c99=yes \
LD_LIBRARY_PATH+="$PWD/gmodule/.libs/ $PWD/glib/gnulib/.libs/ $PWD/glib/libcharset/.libs/ " \
./configure \
  --disable-always-build-tests --disable-installed-tests \
  --disable-coverage --disable-fam \
  --disable-gtk-doc --disable-gtk-doc-html --disable-gtk-doc-pdf --disable-man \
  --disable-libtool-lock --disable-selinux \
  --host=$CFGHOST --prefix=%{_prefix} --build=%{_build}
make LDFLAGS="-Wl,-rpath,$PWD/gmodule/.libs:$PWDglib/glib/gnulib/.libs/:$PWD/glib/libcharset/.libs" -j1
# make LDFLAGS="-rpath $PWD/gmodule/.libs/ -rpath $PWD/glib/libgnu/.libs/" -j1

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*

