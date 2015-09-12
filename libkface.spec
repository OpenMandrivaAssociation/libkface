%define major 3
%define libname %mklibname kface %{major}
%define devname %mklibname kface -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: libkface
Version: 15.08.0
Release: 2
# Sadly, have to carry this over from when libkface was a part of digikam
Epoch: 4
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: Qt wrapper around the libface face recognition and detection library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: qt4-devel
BuildRequires: pkgconfig(opencv)
BuildRequires: kdelibs4-devel
Requires: %{libname} = %{EVRD}

%description
Qt wrapper around the libface face recognition and detection library

%package -n %{libname}
Summary: Qt wrapper around the libface face recognition and detection library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt wrapper around the libface face recognition and detection library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_datadir}/apps/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Kface-*
