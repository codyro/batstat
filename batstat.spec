%global commit      d65abb7f96a7174a9bde270cb96c0254b8ebd8c9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           batstat
Version:        0~^1.%{shortcommit}
Release:        %autorelease
Summary:        CLI battery status for Linux

License:        GPLv3
URL:            https://github.com/Juve45/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc-c++
BuildRequires: ncurses-devel

%description
%{summary}


%prep
%autosetup -n %{name}-%{commit}


%build
%make_build CCFLAGS="%{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}


%files
%{_bindir}/%{name}
%doc README.md


%changelog
%autochangelog

