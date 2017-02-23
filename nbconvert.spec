#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbconvert
Version  : 5.1.1
Release  : 2
URL      : https://pypi.python.org/packages/95/58/df1c91f1658ee5df19097f915a1e71c91fc824a708d82d2b2e35f8b80e9a/nbconvert-5.1.1.tar.gz
Source0  : https://pypi.python.org/packages/95/58/df1c91f1658ee5df19097f915a1e71c91fc824a708d82d2b2e35f8b80e9a/nbconvert-5.1.1.tar.gz
Summary  : Converting Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: nbconvert-bin
Requires: nbconvert-python
Requires: bleach
Requires: entrypoints
Requires: mistune
Requires: nbformat
Requires: pandocfilters
Requires: testpath
Requires: traitlets
BuildRequires : bleach
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# nbconvert
### Jupyter Notebook Conversion
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/nbconvert.svg?branch=master)](https://travis-ci.org/jupyter/nbconvert)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=stable)](http://nbconvert.readthedocs.io/en/stable/?badge=stable)
[![codecov.io](https://codecov.io/github/jupyter/nbconvert/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbconvert?branch=master)

%package bin
Summary: bin components for the nbconvert package.
Group: Binaries

%description bin
bin components for the nbconvert package.


%package python
Summary: python components for the nbconvert package.
Group: Default

%description python
python components for the nbconvert package.


%prep
%setup -q -n nbconvert-5.1.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487876323
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487876323
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-nbconvert

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*