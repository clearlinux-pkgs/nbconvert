#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbconvert
Version  : 6.3.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/5f/d1/522fa1c7fa5269c8dcd1e14e16e43dadfcb56e938869f17cc5f1c325aa8d/nbconvert-6.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/d1/522fa1c7fa5269c8dcd1e14e16e43dadfcb56e938869f17cc5f1c325aa8d/nbconvert-6.3.0.tar.gz
Summary  : Converting Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: nbconvert-bin = %{version}-%{release}
Requires: nbconvert-data = %{version}-%{release}
Requires: nbconvert-license = %{version}-%{release}
Requires: nbconvert-python = %{version}-%{release}
Requires: nbconvert-python3 = %{version}-%{release}
Requires: bleach
Requires: entrypoints
Requires: mistune
Requires: nbformat
Requires: pandocfilters
Requires: testpath
Requires: traitlets
BuildRequires : bleach
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bleach)
BuildRequires : pypi(defusedxml)
BuildRequires : pypi(entrypoints)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(jupyterlab_pygments)
BuildRequires : pypi(mistune)
BuildRequires : pypi(nbclient)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pandocfilters)
BuildRequires : pypi(pygments)
BuildRequires : pypi(testpath)
BuildRequires : pypi(traitlets)

%description
# nbconvert
### Jupyter Notebook Conversion
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/nbconvert.svg?branch=main)](https://travis-ci.org/jupyter/nbconvert)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=stable)](https://nbconvert.readthedocs.io/en/stable/?badge=stable)
[![codecov.io](https://codecov.io/github/jupyter/nbconvert/coverage.svg?branch=main)](https://codecov.io/github/jupyter/nbconvert?branch=main)
[![CircleCI Docs Status](https://circleci.com/gh/jupyter/nbconvert/tree/main.svg?style=svg)](https://circleci.com/gh/jupyter/nbconvert/tree/main)

%package bin
Summary: bin components for the nbconvert package.
Group: Binaries
Requires: nbconvert-data = %{version}-%{release}
Requires: nbconvert-license = %{version}-%{release}

%description bin
bin components for the nbconvert package.


%package data
Summary: data components for the nbconvert package.
Group: Data

%description data
data components for the nbconvert package.


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
Requires: pypi(bleach)
Requires: pypi(defusedxml)
Requires: pypi(entrypoints)
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(jupyterlab_pygments)
Requires: pypi(mistune)
Requires: pypi(nbclient)
Requires: pypi(nbformat)
Requires: pypi(pandocfilters)
Requires: pypi(pygments)
Requires: pypi(testpath)
Requires: pypi(traitlets)

%description python3
python3 components for the nbconvert package.


%prep
%setup -q -n nbconvert-6.3.0
cd %{_builddir}/nbconvert-6.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638703412
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . mistune
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbconvert
cp %{_builddir}/nbconvert-6.3.0/LICENSE %{buildroot}/usr/share/package-licenses/nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} mistune
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-dejavu
/usr/bin/jupyter-nbconvert

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbconvert/templates/asciidoc/conf.json
/usr/share/jupyter/nbconvert/templates/asciidoc/index.asciidoc.j2
/usr/share/jupyter/nbconvert/templates/base/celltags.j2
/usr/share/jupyter/nbconvert/templates/base/display_priority.j2
/usr/share/jupyter/nbconvert/templates/base/jupyter_widgets.html.j2
/usr/share/jupyter/nbconvert/templates/base/mathjax.html.j2
/usr/share/jupyter/nbconvert/templates/base/null.j2
/usr/share/jupyter/nbconvert/templates/basic/conf.json
/usr/share/jupyter/nbconvert/templates/basic/index.html.j2
/usr/share/jupyter/nbconvert/templates/classic/base.html.j2
/usr/share/jupyter/nbconvert/templates/classic/conf.json
/usr/share/jupyter/nbconvert/templates/classic/index.html.j2
/usr/share/jupyter/nbconvert/templates/classic/static/style.css
/usr/share/jupyter/nbconvert/templates/compatibility/display_priority.tpl
/usr/share/jupyter/nbconvert/templates/compatibility/full.tpl
/usr/share/jupyter/nbconvert/templates/lab/base.html.j2
/usr/share/jupyter/nbconvert/templates/lab/conf.json
/usr/share/jupyter/nbconvert/templates/lab/index.html.j2
/usr/share/jupyter/nbconvert/templates/lab/static/index.css
/usr/share/jupyter/nbconvert/templates/lab/static/theme-dark.css
/usr/share/jupyter/nbconvert/templates/lab/static/theme-light.css
/usr/share/jupyter/nbconvert/templates/latex/base.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/conf.json
/usr/share/jupyter/nbconvert/templates/latex/display_priority.j2
/usr/share/jupyter/nbconvert/templates/latex/document_contents.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/index.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/null.j2
/usr/share/jupyter/nbconvert/templates/latex/report.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_bw_ipython.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_bw_python.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_ipython.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_jupyter.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_python.tex.j2
/usr/share/jupyter/nbconvert/templates/markdown/conf.json
/usr/share/jupyter/nbconvert/templates/markdown/index.md.j2
/usr/share/jupyter/nbconvert/templates/python/conf.json
/usr/share/jupyter/nbconvert/templates/python/index.py.j2
/usr/share/jupyter/nbconvert/templates/reveal/base.html.j2
/usr/share/jupyter/nbconvert/templates/reveal/conf.json
/usr/share/jupyter/nbconvert/templates/reveal/index.html.j2
/usr/share/jupyter/nbconvert/templates/reveal/static/custom_reveal.css
/usr/share/jupyter/nbconvert/templates/rst/conf.json
/usr/share/jupyter/nbconvert/templates/rst/index.rst.j2
/usr/share/jupyter/nbconvert/templates/script/conf.json
/usr/share/jupyter/nbconvert/templates/script/script.j2
/usr/share/jupyter/nbconvert/templates/webpdf/conf.json
/usr/share/jupyter/nbconvert/templates/webpdf/index.pdf.j2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
