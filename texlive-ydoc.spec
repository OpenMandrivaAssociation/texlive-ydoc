Name:		texlive-ydoc
Version:	64887
Release:	2
Summary:	Macros for documentation of LaTeX classes and packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ydoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/ydoc
%{_texmfdistdir}/tex/latex/ydoc
%doc %{_texmfdistdir}/doc/latex/ydoc
#- source
%doc %{_texmfdistdir}/source/latex/ydoc

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
