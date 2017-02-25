#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : doc8
Version  : 0.7.0
Release  : 17
URL      : https://pypi.python.org/packages/source/d/doc8/doc8-0.7.0.tar.gz
Source0  : https://pypi.python.org/packages/source/d/doc8/doc8-0.7.0.tar.gz
Summary  : Style checker for Sphinx (or other) RST documentation
Group    : Development/Tools
License  : Apache-2.0
Requires: doc8-bin
Requires: doc8-python
Requires: chardet
Requires: docutils
Requires: restructuredtext_lint
Requires: six
Requires: stevedore
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : Sphinx-python
BuildRequires : chardet-python
BuildRequires : configparser-python
BuildRequires : docutils-python
BuildRequires : enum34-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : nose-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : restructuredtext_lint-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
Patch1: test.patch

%description
====
Doc8
====
Doc8 is an *opinionated* style checker for `rst`_ (with basic support for
plain text) styles of documentation.

%package bin
Summary: bin components for the doc8 package.
Group: Binaries

%description bin
bin components for the doc8 package.


%package python
Summary: python components for the doc8 package.
Group: Default

%description python
python components for the doc8 package.


%prep
%setup -q -n doc8-0.7.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488046585
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1488046585
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doc8

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
