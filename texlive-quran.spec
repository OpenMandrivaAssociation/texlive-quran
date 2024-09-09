Name:		texlive-quran
Version:	72223
Release:	1
Summary:	An easy way to typeset any part of The Holy Quran
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quran
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers the user an easy way to typeset The Holy
Quran. It has been inspired by the lipsum and ptext packages
and provides several macros for typesetting the whole or any
part of the Quran based on its popular division, including
surah, ayah, juz, hizb, quarter, and page. Besides the Arabic
original, translations to English, German, French, and Persian
are provided, as well as an English transliteration.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quran
%doc %{_texmfdistdir}/doc/latex/quran

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
