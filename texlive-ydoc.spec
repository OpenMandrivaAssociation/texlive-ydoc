# revision 23544
# category Package
# catalog-ctan /macros/latex/contrib/ydoc
# catalog-date 2011-03-21 08:49:58 +0100
# catalog-license lppl1.3
# catalog-version 0.5alpha
Name:		texlive-ydoc
Version:	0.5alpha
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides macros and environments to document LaTeX
packages and classes. It is an (as yet unfinished) alternative
to the ltxdoc class and the doc or xdoc packages. The aim is to
provide a different layout and more modern styles (using the
xcolor, hyperref packages, etc.) This is an alpha release, and
should probably not (yet) be used with other packages, since
the implementation might change. Nevertheless, the author uses
it to document his own packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ydoc/ydoc-code.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-desc.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-doc.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc-expl.sty
%{_texmfdistdir}/tex/latex/ydoc/ydoc.cfg
%{_texmfdistdir}/tex/latex/ydoc/ydoc.cls
%{_texmfdistdir}/tex/latex/ydoc/ydoc.sty
%{_texmfdistdir}/tex/latex/ydoc/ydocstrip.tex
%doc %{_texmfdistdir}/doc/latex/ydoc/README
%doc %{_texmfdistdir}/doc/latex/ydoc/ydoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ydoc/ydoc.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
