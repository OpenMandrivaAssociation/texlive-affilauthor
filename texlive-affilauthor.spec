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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides key-value style author and affiliation information
tagging in a structured format. Each field has a specific name similar
to the bib format. We can customize the styles as per preferences for
article.cls class layout. Instead of giving all the information (author
and affiliation) in a single tag, we can split the information in a
format of key-value style.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/affilauthor
%dir %{_datadir}/texmf-dist/tex/latex/affilauthor
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/affilauthor-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/affilauthor-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/affilauthor-image1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/affilauthor-image2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/affilauthor/affilauthor-image3.pdf
%{_datadir}/texmf-dist/tex/latex/affilauthor/affilauthor.sty
