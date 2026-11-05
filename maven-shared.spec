Summary:        Maven Shared Components
URL:            https://maven.apache.org/shared/
Name:           maven-shared
Version:        50
Release:        1
License:        ASL 2.0
Group:          Development/Java

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-components/%{version}/maven-shared-components-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	maven-parent
BuildSystem:	maven
BuildOption:	validate

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
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
