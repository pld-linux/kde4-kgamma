%define		_state		stable
%define		qtver		4.7.4

Summary:	A monitor calibration tool
Summary(pl.UTF-8):	Narzędzie do kalibracji monitora
Name:		kgamma
Version:	4.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	810d933d7e7b637558a5333b52818db9
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdegraphics-kgamma < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A monitor calibration tool.

%description -l pl.UTF-8
Narzędzie do kalibracji monitora.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%attr(755,root,root) %{_libdir}/kde4/kcm_kgamma.so
%{_datadir}/apps/kgamma
%{_datadir}/kde4/services/kgamma.desktop
%{_kdedocdir}/en/kcontrol/kgamma
