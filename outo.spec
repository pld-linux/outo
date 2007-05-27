Summary:	Simple unit tester for C/C++ on Linux
Summary(pl.UTF-8):	Prosty tester jednostkowy dla C/C++ na Linuksie
Name:		outo
Version:	0.1.2
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/outo/%{name}-%{version}.tar.gz
# Source0-md5:	75a53d333dca94925f05bee8293a0294
URL:		http://outo.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OUTO (Outo Unit Tester by Otso) is a simple unit tester for C (or C++
as well) on Linux.

%description -l pl.UTF-8
OUTO (Outo Unit Tester by Otso) to prosty tester jednostkowy dla C
(oraz C++) na Linuksie.

%prep
%setup -q

%build
%configure
%{__make} \
	AM_CFLAGS="%{rpmcflags} -ansi -Wall -pipe -Wmissing-prototypes"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HOWTO NEWS README THANKS
%attr(755,root,root) %{_bindir}/outo
%{_includedir}/outo.h
%{_pkgconfigdir}/outo.pc
%{_examplesdir}/%{name}-%{version}
