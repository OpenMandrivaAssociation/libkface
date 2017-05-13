%define major 5
%define libname %mklibname KF5KFace %{major}
%define devname %mklibname KF5KFace -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Qt wrapper around the libface face recognition and detection library
Name:		libkface
Version:	17.04.0
Release:	2
# Sadly, have to carry this over from when libkface was a part of digikam
Epoch:		4
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
URL:		http://kde.org/
License:	GPL
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Gui)
Requires:	%{libname} = %{EVRD}

%description
Qt wrapper around the libface face recognition and detection library

%package -n %{libname}
Summary:	Qt wrapper around the libface face recognition and detection library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname kface 3} < 4:15.12.0

%description -n %{libname}
Qt wrapper around the libface face recognition and detection library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{mklibname kface -d} < 4:15.12.0

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5 -DENABLE_OPENCV3=1

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/libKF5KFace.so.%{major}*
%{_libdir}/libKF5KFace.so.10*

%files -n %{devname}
%{_includedir}/KF5/KFace
%{_includedir}/KF5/libkface_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5KFace
