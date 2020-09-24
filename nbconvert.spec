#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbconvert
Version  : 5.6.1
Release  : 34
URL      : https://files.pythonhosted.org/packages/04/f2/299fa4b15155ecbe2aefe7412249f0dd91f953b7a9b37c336317d564a1ca/nbconvert-5.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/f2/299fa4b15155ecbe2aefe7412249f0dd91f953b7a9b37c336317d564a1ca/nbconvert-5.6.1.tar.gz
Summary  : Converting Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: nbconvert-bin = %{version}-%{release}
Requires: nbconvert-license = %{version}-%{release}
Requires: nbconvert-python = %{version}-%{release}
Requires: nbconvert-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Pygments
Requires: bleach
Requires: defusedxml
Requires: entrypoints
Requires: jupyter_core
Requires: mistune
Requires: nbformat
Requires: pandocfilters
Requires: testpath
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : bleach
BuildRequires : buildreq-distutils3
BuildRequires : defusedxml
BuildRequires : entrypoints
BuildRequires : jupyter_core
BuildRequires : mistune
BuildRequires : nbformat
BuildRequires : pandocfilters
BuildRequires : testpath
BuildRequires : traitlets
BuildRequires : util-linux

%description
# nbconvert
### Jupyter Notebook Conversion
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/nbconvert.svg?branch=master)](https://travis-ci.org/jupyter/nbconvert)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=stable)](http://nbconvert.readthedocs.io/en/stable/?badge=stable)
[![codecov.io](https://codecov.io/github/jupyter/nbconvert/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbconvert?branch=master)
[![CircleCI Docs Status](https://circleci.com/gh/jupyter/nbconvert/tree/master.svg?style=svg)](https://circleci.com/gh/jupyter/nbconvert/tree/master)

%package bin
Summary: bin components for the nbconvert package.
Group: Binaries
Requires: nbconvert-license = %{version}-%{release}

%description bin
bin components for the nbconvert package.


%package license
Summary: license components for the nbconvert package.
Group: Default

%description license
license components for the nbconvert package.


%package python
Summary: python components for the nbconvert package.
Group: Default
Requires: nbconvert-python3 = %{version}-%{release}

%description python
python components for the nbconvert package.


%package python3
Summary: python3 components for the nbconvert package.
Group: Default
Requires: python3-core
Provides: pypi(nbconvert)

%description python3
python3 components for the nbconvert package.


%prep
%setup -q -n nbconvert-5.6.1
cd %{_builddir}/nbconvert-5.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583185514
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbconvert
cp %{_builddir}/nbconvert-5.6.1/LICENSE %{buildroot}/usr/share/package-licenses/nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-nbconvert

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
