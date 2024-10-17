Name:		texlive-wordcount
Version:	46165
Release:	2
Summary:	Estimate the number of words in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wordcount
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordcount.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a relatively easy way of estimating the
number of words in a LaTeX document that does not require
dvitty or other DVI converters. It does however require
something like Unix grep -c that can search a file for a
particular string and report the number of matching lines. An
accompanying shell script wordcount.sh contains more
information in its comments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/wordcount
%{_texmfdistdir}/texmf-dist/scripts/wordcount
%doc %{_texmfdistdir}/texmf-dist/doc/latex/wordcount

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
