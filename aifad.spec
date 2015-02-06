%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Automated Induction of Functions over Algebraic Datatypes
Name:		aifad
Version:	2.0.2
Release:	2
License:	GPLv3+
Group:		Development/Other
Url:		https://bitbucket.org/mmottl/aifad
Source0:	https://bitbucket.org/mmottl/aifad/downloads/aifad-%{version}.tar.gz
BuildRequires:	menhir
BuildRequires:	ocaml
BuildRequires:	ocaml-cfg-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-res-devel

%description
AIFAD stands for "Automated Induction of Functions over Algebraic Datatypes"
and improves decision tree learning by supporting significantly more complex
kinds of data. This allows users to more conveniently describe the data they
want to have learnt, which can improve accuracy and complexity of resulting
models.

%files
%doc README.md AUTHORS.txt COPYING.txt CHANGES.txt TODO.md
%doc examples/
%{_bindir}/aifad
%{_datadir}/vim/syntax/aifad.vim

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./configure \
	--bindir %{_bindir} \
	--destdir %{buildroot}

make

%install
%makeinstall_std

install -d %{buildroot}%{_datadir}/vim/syntax/
install -m 0644 ./vim/aifad.vim %{buildroot}%{_datadir}/vim/syntax/

