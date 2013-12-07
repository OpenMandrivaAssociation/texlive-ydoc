# revision 26202
# category Package
# catalog-ctan /macros/latex/contrib/ydoc
# catalog-date 2012-02-24 11:32:36 +0100
# catalog-license lppl1.3
# catalog-version 0.6alpha
Name:		texlive-ydoc
Version:	0.6alpha
Release:	4
Summary:	Macros for documentation of LaTeX classes and packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ydoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros and environments to document LaTeX
packages and classes. It is an (as yet unfinished) alternative
to the ltxdoc class and the doc or xdoc packages. The aim is to
provide a different layout and more modern styles (using the
xcolor, hyperref packages, etc.) This is an alpha release, and
should probably not (yet) be used with other packages, since
the implementation might change. Nevertheless, the author uses
it to document his own packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ydoc/ydocincl.tex
%{_texmfdistdir}/tex/generic/ydoc/ydocstrip.tex
%{_texmfdistdir}/tex/latex/ydoc/ydoc-code.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-desc.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-doc.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-expl.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc.cfg
%{_texmfdistdir}/tex/latex/ydoc/ydoc.cls
%{_texmfdistdir}/tex/latex/ydoc/ydoc.sty
%doc %{_texmfdistdir}/doc/latex/ydoc/README
%doc %{_texmfdistdir}/doc/latex/ydoc/ydoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ydoc/ydoc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
