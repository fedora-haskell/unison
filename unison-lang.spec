%define debug_package %{nil}

%global ghc_major 9.6
%global ghc_name ghc%{?ghc_major}

%if %{defined el9}
%global stackage lts-22.43
%else
%global stackage lts-22.44
%endif

Name:           unison-lang
Version:        0.5.45
Release:        1%{?dist}
Summary:        Unison language

License:        MIT
URL:            https://www.unison-lang.org/
Source0:        https://github.com/unisonweb/unison/archive/refs/tags/release/%{version}.tar.gz#/unison-release-%{version}.tar.gz
Patch0:         unison-version.patch
Patch1:         stack-gnu17.patch

BuildRequires:  stack
BuildRequires:  ghc%{?ghc_major}
BuildRequires:  ghc-rpm-macros
BuildRequires:  zlib-devel
Recommends:     fzf
Obsoletes:      unison < 0.5.31-2
# unison file sync tool reappeared in Fedora
Conflicts:      unison > 2.53

%description
Unison programming language.


%prep
%setup -q -n unison-release-%{version}
%patch -P0 -p1 -b .orig
%patch -P1 -p1 -b .orig

sed -i s/@VERSION@/%{version}/ unison-cli-main/unison/Version.hs


%build


%install
stack-symlink-distro-ghc %{ghc_version}
if [ -d "$HOME/.stack/programs/ppc64le-linux" ]; then
mv $HOME/.stack/programs/{ppc64le,ppc64}-linux
fi
stack update
LANG=C.utf8 stack --resolver %{stackage} --no-install-ghc install

mkdir -p %{buildroot}%{_bindir}
cp -p ~/.local/bin/unison %{buildroot}%{_bindir}
ln -s unison %{buildroot}%{_bindir}/ucm


%files
%license LICENSE
%doc CONTRIBUTORS.markdown CREDITS.md README.md
%{_bindir}/unison
%{_bindir}/ucm


%changelog
* Thu Aug 21 2025 Jens Petersen <petersen@redhat.com> - 0.5.45-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.45

* Thu Jul 31 2025 Jens Petersen <petersen@redhat.com> - 0.5.44-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.44

* Mon Jun 30 2025 Jens Petersen <petersen@redhat.com> - 0.5.42-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.42

* Fri May 09 2025 Eduardo Hernacki <eh@runlevel0.me> - 0.5.40-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.40

* Thu May 08 2025 Jens Petersen <petersen@redhat.com> - 0.5.39-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.39

* Thu May 08 2025 Jens Petersen <petersen@redhat.com> - 0.5.38-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.38

* Fri Nov 15 2024 Jens Petersen <petersen@redhat.com> - 0.5.28-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.28
- renamed to unison-lang and obsoletes unison-0.5.*
  (unison file sync tool was added back to Fedora last year)

* Thu Aug  1 2024 Jens Petersen <petersen@redhat.com> - 0.5.25-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.25
- build with ghc9.6

* Mon May 27 2024 Jens Petersen <petersen@redhat.com> - 0.5.20-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.19
- https://github.com/unisonweb/unison/releases/tag/release/0.5.20

* Thu Feb 29 2024 Jens Petersen <petersen@redhat.com> - 0.5.18-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.18

* Tue Feb 20 2024 Jens Petersen <petersen@redhat.com> - 0.5.17-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.17

* Wed Feb 14 2024 Jens Petersen <petersen@redhat.com> - 0.5.16-1
- https://github.com/unisonweb/unison/releases/tag/release/0.5.16

* Fri Dec 15 2023 Jens Petersen <petersen@redhat.com> - 0.5.11-2
- add ucm symlink

* Fri Dec 15 2023 Jens Petersen <petersen@redhat.com> - 0.5.11-1
- update to 0.5.11 (new upstream version format instead of M5k)
- https://github.com/unisonweb/unison/releases/tag/release/0.5.11

* Sun Nov 19 2023 Jens Petersen <petersen@redhat.com> - M5h-1
- update to M5h

* Sat Aug 19 2023 Jens Petersen <petersen@redhat.com> - M5c-1
- initial package
