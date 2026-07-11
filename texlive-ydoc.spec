%global tl_name ydoc
%global tl_revision 64887

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7alpha
Release:	%{tl_revision}.1
Summary:	Macros for documentation of LaTeX classes and packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ydoc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ydoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Requires:	texlive(float)
Requires:	texlive(hyperref)
Requires:	texlive(listings)
Requires:	texlive(needspace)
Requires:	texlive(newverbs)
Requires:	texlive(showexpl)
Requires:	texlive(tools)
Requires:	texlive(url)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros and environments to document LaTeX packages
and classes. It is an (as yet unfinished) alternative to the ltxdoc
class and the doc or xdoc packages. The aim is to provide a different
layout and more modern styles (using the xcolor, hyperref packages,
etc.) This is an alpha release, and should probably not (yet) be used
with other packages, since the implementation might change.
Nevertheless, the author uses it to document his own packages.

