Name:		texlive-metapost
Version:	73850
Release:	1
Summary:	A development of Metafont for creating graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/base
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-metapost.bin

%description
MetaPost uses a language based on that of Metafont to produce
precise technical illustrations. Its output is scalable
PostScript or SVG, rather than the bitmaps Metafont creates.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/metapost
%{_texmfdistdir}/fonts/enc/dvips/metapost
%{_texmfdistdir}/fonts/map/dvips/metapost
%{_texmfdistdir}/fonts/tfm/metapost
%{_texmfdistdir}/fonts/type1/metapost
%{_texmfdistdir}/metapost
%{_texmfdistdir}/tex/generic/metapost
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/metapost

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
