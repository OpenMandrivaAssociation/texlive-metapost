# revision 31860
# category Package
# catalog-ctan /graphics/metapost/base
# catalog-date 2013-06-20 18:08:19 +0200
# catalog-license lgpl
# catalog-version 1.803
Name:		texlive-metapost
Version:	1.803
Release:	2
Summary:	A development of Metafont for creating graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/base
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/metapost/freeeuro.afm
%{_texmfdistdir}/fonts/afm/metapost/psyrgo.afm
%{_texmfdistdir}/fonts/afm/metapost/zpzdr-reversed.afm
%{_texmfdistdir}/fonts/enc/dvips/metapost/groff.enc
%{_texmfdistdir}/fonts/map/dvips/metapost/troff-updmap.map
%{_texmfdistdir}/fonts/map/dvips/metapost/troff.map
%{_texmfdistdir}/fonts/tfm/metapost/freeeuro.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pagd8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pagdo8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pagk8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pagko8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pbkd8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pbkdi8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pbkl8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pbkli8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pcrb8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pcrbo8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pcrr8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pcrro8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvb8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvb8gn.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvbo8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvbo8gn.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvr8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvr8gn.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvro8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/phvro8gn.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pncb8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pncbi8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pncr8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pncri8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pplb8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pplbi8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pplr8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pplri8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/psyrgo.tfm
%{_texmfdistdir}/fonts/tfm/metapost/ptmb8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/ptmbi8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/ptmr8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/ptmri8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/pzcmi8g.tfm
%{_texmfdistdir}/fonts/tfm/metapost/zpzdr-reversed.tfm
%{_texmfdistdir}/fonts/type1/metapost/freeeuro.pfa
%{_texmfdistdir}/metapost/base/TEX.mp
%{_texmfdistdir}/metapost/base/boxes.mp
%{_texmfdistdir}/metapost/base/format.mp
%{_texmfdistdir}/metapost/base/graph.mp
%{_texmfdistdir}/metapost/base/marith.mp
%{_texmfdistdir}/metapost/base/mfplain.mp
%{_texmfdistdir}/metapost/base/mpost.mp
%{_texmfdistdir}/metapost/base/plain.mp
%{_texmfdistdir}/metapost/base/rboxes.mp
%{_texmfdistdir}/metapost/base/sarith.mp
%{_texmfdistdir}/metapost/base/string.mp
%{_texmfdistdir}/metapost/base/texnum.mp
%{_texmfdistdir}/metapost/base/troffnum.mp
%{_texmfdistdir}/metapost/config/mfplain.ini
%{_texmfdistdir}/metapost/misc/null.mp
%{_texmfdistdir}/metapost/support/charlib/12
%{_texmfdistdir}/metapost/support/charlib/14
%{_texmfdistdir}/metapost/support/charlib/34
%{_texmfdistdir}/metapost/support/charlib/Ao
%{_texmfdistdir}/metapost/support/charlib/Fi
%{_texmfdistdir}/metapost/support/charlib/Fl
%{_texmfdistdir}/metapost/support/charlib/L1
%{_texmfdistdir}/metapost/support/charlib/LH
%{_texmfdistdir}/metapost/support/charlib/Lb
%{_texmfdistdir}/metapost/support/charlib/Sl
%{_texmfdistdir}/metapost/support/charlib/ao.x
%{_texmfdistdir}/metapost/support/charlib/bx
%{_texmfdistdir}/metapost/support/charlib/ci
%{_texmfdistdir}/metapost/support/charlib/ff
%{_texmfdistdir}/metapost/support/charlib/lh.x
%{_texmfdistdir}/metapost/support/charlib/ob
%{_texmfdistdir}/metapost/support/charlib/rh
%{_texmfdistdir}/metapost/support/charlib/sq
%{_texmfdistdir}/metapost/support/charlib/twiddle
%{_texmfdistdir}/metapost/support/trchars.adj
%{_texmfdistdir}/metapost/support/trfonts.map
%{_texmfdistdir}/tex/generic/metapost/mproof.tex
%{_texmfdistdir}/tex/generic/metapost/mpsproof.tex
%doc %{_mandir}/man1/dvitomp.1*
%doc %{_texmfdistdir}/doc/man/man1/dvitomp.man1.pdf
%doc %{_mandir}/man1/mpost.1*
%doc %{_texmfdistdir}/doc/man/man1/mpost.man1.pdf
%doc %{_texmfdistdir}/doc/metapost/base/grdemo-doc.pdf
%doc %{_texmfdistdir}/doc/metapost/base/grdemo.pdf
%doc %{_texmfdistdir}/doc/metapost/base/index.html
%doc %{_texmfdistdir}/doc/metapost/base/mpboxes.pdf
%doc %{_texmfdistdir}/doc/metapost/base/mpgraph.pdf
%doc %{_texmfdistdir}/doc/metapost/base/mpintro.pdf
%doc %{_texmfdistdir}/doc/metapost/base/mplibapi.pdf
%doc %{_texmfdistdir}/doc/metapost/base/mpman.pdf
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/Makefile
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/README
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/TODO
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/agepop91.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/agepopm.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/charts.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/cm2lm.map
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/countries.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/ctabbing.sty
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/demo.ms
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/energy.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/figs.1
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/figs.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/grdemo-doc.ms
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/grdemo-doc.ps
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/grdemo.eps
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/grdemo.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/grdemo.ms
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/lead.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/matmul.d
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpboxes.bib
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpboxes.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpboxes.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpgraph.bib
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpgraph.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpgraph.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mplibapi.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman-app-legacy.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman-app-optab.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman-app-refman.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman-charts.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman.bib
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman.ist
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/mpman.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-manual/timepop.d
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/Makefile
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/abstract.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/annulus.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/arrows.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/biblio.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/circles.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/commands.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/compilation.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/conclusion.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/data.d
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/data.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/data.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/draw.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/draw.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/fill.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/fill.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/graph.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/inclusion.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/intro.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/label.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/label.tex
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/mpintro.bib
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/mpintro.ltx
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/paperclip.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/parabola.mp
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/previewer.eps
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/previewer.pdf
%doc %{_texmfdistdir}/doc/metapost/base/source-tutorial/previewer.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
