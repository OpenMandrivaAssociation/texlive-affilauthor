%global tl_name affilauthor
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Tag author and affiliation information in a key-value style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/affilauthor
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/affilauthor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/affilauthor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides key-value style author and affiliation information
tagging in a structured format. Each field has a specific name similar
to the bib format. We can customize the styles as per preferences for
article.cls class layout. Instead of giving all the information (author
and affiliation) in a single tag, we can split the information in a
format of key-value style.

