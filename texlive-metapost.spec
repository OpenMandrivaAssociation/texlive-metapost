%global tl_name metapost
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A development of Metafont for creating graphics
Group:		Publishing
URL:		https://www.ctan.org/pkg/metapost
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(metapost.bin)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
MetaPost uses a language based on that of Metafont to produce precise
technical illustrations. Its output is scalable PostScript or SVG,
rather than the bitmaps Metafont creates.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from metapost:
Map troff-updmap.map
TL_DROPIN_EOF
