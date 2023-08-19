%global milestone M5c

%undefine _enable_debug_packages

Name:           unison
Version:        %{milestone}
Release:        2%{?dist}
Summary:        Unison language

License:        MIT
URL:            https://www.unison-lang.org/
Source0:        https://github.com/unisonweb/unison/archive/refs/tags/release/%{milestone}.tar.gz#/unison-release-%{milestone}.tar.gz
Patch0:         unison-version.patch

BuildRequires:  stack
BuildRequires:  ghc9.2
BuildRequires:  zlib-devel

%description
Unison programming language.


%prep
%setup -q -n unison-release-%{milestone}
sed s/@MILESTONE@/%{milestone}/ %{PATCH0} | patch -p1


%build


%install
LANG=C.utf8 stack --system-ghc install

mkdir -p %{buildroot}%{_bindir}
cp -p ~/.local/bin/unison %{buildroot}%{_bindir}


%files
%license LICENSE
%doc CONTRIBUTORS.markdown CREDITS.md README.md
%{_bindir}/unison


%changelog
* Sat Aug 19 2023 Jens Petersen <petersen@redhat.com> - M5c-1
- initial package
