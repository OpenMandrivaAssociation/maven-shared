%{?_javapackages_macros:%_javapackages_macros}
Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           maven-shared
Version:        22
Release:        1
License:        ASL 2.0
Group:          Development/Java

Source0:        https://github.com/apache/maven-shared/archive/maven-shared-components-%{version}.tar.gz

BuildRequires:  java-devel
BuildRequires:  maven-local

BuildArch:      noarch

# Obsoleting retired subpackages. The packages with hardcoded versions and
# releases had their versions manually set in maven-shared-15 to something else
# than {version}. To make the change effective, the release below is one
# greater than the last release of maven-shared-15 in rawhide.
Obsoletes:      maven-shared-ant < 1.0-32
Obsoletes:      maven-shared-model-converter < 2.3-32
Obsoletes:      maven-shared-runtime < 1.0-32
Obsoletes:      maven-shared-monitor < 1.0-32
Obsoletes:      maven-shared-javadoc < %{version}-%{release}

%description
Maven Shared Components

%prep
%setup -q -n %{name}-%{name}-components-%{version}
chmod -R go=u-w *

# Maven-scm-publish-plugin is not in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
