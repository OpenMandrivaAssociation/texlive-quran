%global tl_name quran
%global tl_revision 78362

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.42
Release:	%{tl_revision}.1
Summary:	An easy way to typeset any part of The Holy Quran
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/quran
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers the user an easy way to typeset The Holy Quran. It
has been inspired by the lipsum and ptext packages and provides several
macros for typesetting the whole or any part of the Quran based on its
popular division, including surah, ayah, juz, hizb, quarter, and page.
Besides the Arabic original, translations to English, German, French,
and Persian are provided, as well as an English transliteration.

