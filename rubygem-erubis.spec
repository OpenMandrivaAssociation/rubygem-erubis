# Generated from erubis-2.7.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	erubis

Summary:	a fast and extensible eRuby implementation which supports multi-language
Name:		rubygem-%{rbname}

Version:	2.7.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://www.kuwata-lab.com/erubis/
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Erubis is an implementation of eRuby and has the following features:
* Very fast, almost three times faster than ERB and about 10% faster than
eruby.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript)
* Auto escaping support
* Auto trimming spaces around '<% %>'
* Embedded pattern changeable (default '<% %>')
* Enable to handle Processing Instructions (PI) as embedded pattern (ex. '<?rb
... ?>')
* Context object available and easy to combine eRuby template with YAML
datafile
* Print statement available
* Easy to extend and customize in subclass
* Ruby on Rails support

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/erubis
%{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.7.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.7.0-1
+ Revision: 766879
- imported package rubygem-erubis

