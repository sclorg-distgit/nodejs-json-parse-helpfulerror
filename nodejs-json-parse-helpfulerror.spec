%{?scl:%scl_package nodejs-json-parse-helpfulerror}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-json-parse-helpfulerror

%global npm_name json-parse-helpfulerror
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-json-parse-helpfulerror
Version:	1.0.3
Release:	3%{?dist}
Summary:	A drop-in replacement for JSON.parse that uses `jju` to give helpful errors
Url:		https://github.com/smikes/json-parse-helpfulerror
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(code)
BuildRequires:	%{?scl_prefix}npm(jslint)
BuildRequires:	%{?scl_prefix}npm(lab)
%endif

BuildRequires:	%{?scl_prefix}npm(jju)

Requires:	%{?scl_prefix}npm(jju)

%description
A drop-in replacement for JSON.parse that uses `jju` to give helpful errors

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
jslint --edition=latest --terse *.js
lab -c
%endif

%files
%{nodejs_sitelib}/json-parse-helpfulerror

%doc README.md LICENSE

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-2
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-1
- Initial build
