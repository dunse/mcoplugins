%define plugindir %{_libexecdir}/mcollective/mcollective
%define agent_name nodeinfo 
%define gitrev 26323ed 

Name:      mcollective-plugins-nodeinfo
Summary:   Mcollective plugin agent that lets you get information on nodes 
Version:   1.0
Release:   2%{?dist}
License:   GPLv3
Group:     Development/Libraries
#Source0:   %{name}-%{version}.tar.gz 
Source0:   thinkfr-mcoplugins-%{gitrev}.tar.gz 
Requires:  mcollective >= 1.1.0
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Packager:  Louis Coilliot

%description
The nodeinfo agent lets you get basic information like the agents,
some facts and puppet classes of a mcollective node 

%prep
%setup -n thinkfr-mcoplugins-%{gitrev} 

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{plugindir}
install -d -m 755 %{buildroot}%{plugindir}/agent
install %{agent_name}* %{buildroot}%{plugindir}/agent

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,-)
%{plugindir}/agent/%{agent_name}.rb
%{plugindir}/agent/%{agent_name}.ddl

%changelog
* Sat Aug 20 2011 Louis Coilliot
- improvements to the ddl
* Fri Aug 12 2011 Louis Coilliot
- inspired with a spec file from Dan Carley
(https://gist.github.com/957029)
- Initial build

