%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname icapclient3

Name:           python-%{srcname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        Python3 module for creating ICAP clients
License:        GPL-3.0-only
URL:            https://github.com/fim/icapclient3

Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/fim/icapclient3/master/LICENSE

BuildRequires:  c-icap-devel >= 0.5
BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
A Python3 module for creating ICAP clients. The module API is somewhat inspired
by the httplib python module.

This module is written in pure C, and uses the C-ICAP library to handle the ICAP
protocol.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A Python3 module for creating ICAP clients. The module API is somewhat inspired
by the httplib python module.

This module is written in pure C, and uses the C-ICAP library to handle the ICAP
protocol.

%prep
%autosetup -p1 -n %{srcname}-%{version}
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%py3_build

%install
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/icapclient.cpython-%{python3_version_nodots}-%{_arch}-linux-gnu.so

%changelog
* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 1.2.1-1
- First build.
