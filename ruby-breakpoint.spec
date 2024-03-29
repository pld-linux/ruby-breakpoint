Summary:	Module that lets you inspect and modify state at run time
Summary(pl.UTF-8):	Moduł pozwalający na sprawdzanie i zmianę stanu programu w czasie działania
Name:		ruby-breakpoint
Version:	0.5.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/3302/%{name}-%{version}.tgz
# Source0-md5:	c7ca9db1f1ae105c99ddd945d8c55c20
URL:		http://ruby-breakpoint.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-breakpoint lets you inspect and modify state at run time. This
allows you to diagnose bugs, patch applications and more all via IRB
by simply doing a method call at the place you want to investigate.

%description -l pl.UTF-8
ruby-breakpoint pozwala na sprawdzanie i zmianę stanu w czasie
działania programu. Umożliwia to diagnozowanie błędów, poprawianie
aplikacji i inne rzeczy, a wszystko to przez IRB, po prostu wywołując
metodę w miejscu, które chcemy śledzić.

%prep
%setup -q

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
#%{ruby_ridir}/*
