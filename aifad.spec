Name:           aifad
Version:        1.0.28
Release:        %mkrel 1
Summary:        Machine learning system - Automated Induction of Functions over Algebraic Datatypes
License:        GPL
Group:          Development/Other
URL:            http://ocaml.info/home/ocaml_sources.html#aifad
Source0:        http://hg.ocaml.info/release/aifad/archive/aifad-release-%{version}.tar.lzma
# curl http://hg.ocaml.info/release/aifad/archive/release-${version}.tar.bz2 > aifad-release-${version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cfg
BuildRequires:  ocaml-res
BuildRequires:  ocaml-pcre

%description
AIFAD stands for "Automated Induction of Functions over Algebraic Datatypes"
and improves decision tree learning by supporting significantly more complex
kinds of data. This allows users to more conveniently describe the data they
want to have learnt, which can improve accuracy and complexity of resulting
models.

%prep
%setup -q -n aifad-release-%{version}

%build
make opt
(cd src/ ; make doc)

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}/
install -d %{buildroot}%{_datadir}/vim/syntax/
install -m 0755 ./src/aifad %{buildroot}%{_bindir}/
install -m 0644 ./aifad.vim %{buildroot}%{_datadir}/vim/syntax/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.txt INSTALL.txt Changes TODO
%doc examples
%{_bindir}/aifad
%{_datadir}/vim/syntax/aifad.vim

