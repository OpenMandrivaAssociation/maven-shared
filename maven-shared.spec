# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define _with_gcj_support 1
%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/

# svn export
#    http://svn.apache.org/repos/asf/maven/shared/tags/file-management-1.0/
# tar czf maven-shared-file-management-1.0.tar.gz file-management-1.0/
Source0:        maven-shared-file-management-1.0.tar.gz
Source1:        %{name}-mapdeps.xsl
Source2:        %{name}-addjunitdep.xml
Source3:        %{name}-pom.xml
# svn export 
#    http://svn.apache.org/repos/asf/maven/shared/tags/maven-plugin-testing-harness-1.0-beta-1/
# tar czf maven-plugin-testing-harness-1.0-beta-1.tar.gz 
#    maven-plugin-testing-harness-1.0-beta-1/
Source4:        maven-plugin-testing-harness-1.0-beta-1.tar.gz

Patch1:         maven-shared-plugin-testing-harness-pom.patch

Name:           maven-shared
Version:        1.0
Release:        %mkrel 4.2.3
Epoch:          0
License:        Apache Software License
Group:          Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  java-rpmbuild >= 0:1.7.2
BuildRequires:  maven2 >= 0:2.0.4-9jpp
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-surefire
BuildRequires:  junit
BuildRequires:  saxon
BuildRequires:  saxon-scripts
BuildRequires:  plexus-utils
BuildRequires:  modello-maven-plugin

Requires:       maven2 >= 0:2.0.4
Requires:       plexus-utils

%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif


Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description
Maven Shared Components

%package file-management
Summary:        Maven Shared File Management API
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       plexus-utils
Requires:       junit

%description file-management
%{summary}.

%package file-management-javadoc
Summary:        Javadoc for %{name}-file-management
Group:          Development/Java

%description file-management-javadoc
%{summary}.

%package plugin-testing-harness
Summary:        Maven Shared Plugin Testing Harness
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description plugin-testing-harness
%{summary}.

%package plugin-testing-harness-javadoc
Summary:        Javadoc for %{name}-plugin-testing-harness
Group:          Development/Java

%description plugin-testing-harness-javadoc
%{summary}.

%prep
%setup -q -c -n %{name}-%{version}
gzip -dc %{SOURCE4} | tar xf -
chmod -R go=u-w *
%patch1 -b .sav

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
export JAVA_HOME

cp -p file-management-1.0/pom.xml{,.withoutjunit}
saxon -o file-management-1.0/pom.xml file-management-1.0/pom.xml.withoutjunit \
  /usr/share/java-utils/xml/maven2jpp-mapdeps.xsl map=%{SOURCE2}

cp -p %{SOURCE3} pom.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
rm -rf $RPM_BUILD_ROOT

# main package infrastructure
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-shared
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/maven2/poms

# poms
install -pm 644 pom.xml \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.maven-shared-components-parent.pom
%add_to_maven_depmap org.apache.maven.shared shared-components-parent 1 JPP/maven-shared components-parent

install -pm 644 file-management-%{version}/pom.xml \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.maven-shared-file-management.pom
%add_to_maven_depmap org.apache.maven.shared file-management 1.0 JPP/maven-shared file-management

install -pm 644 maven-plugin-testing-harness-1.0-beta-1/pom.xml \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.maven-shared-plugin-testing-harness.pom
%add_to_maven_depmap org.apache.maven.shared maven-plugin-testing-harness 1.0-beta-1 JPP/maven-shared plugin-testing-harness

# subpackage jars
install -p -m 0644 \
      file-management-%{version}/target/file-management-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/maven-shared
pushd $RPM_BUILD_ROOT%{_javadir}/maven-shared
  ln -sf file-management-%{version}.jar file-management.jar
popd

install -p -m 0644 \
      maven-plugin-testing-harness-1.0-beta-1/target/maven-plugin-testing-harness-1.0-beta-1.jar \
      $RPM_BUILD_ROOT%{_javadir}/maven-shared/plugin-testing-harness-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}/maven-shared
  ln -sf plugin-testing-harness-%{version}.jar plugin-testing-harness.jar
popd

# javadoc
install -d -m 755 \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-file-management-%{version}
cp -pr file-management-%{version}/target/site/apidocs/* \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-file-management-%{version}
ln -s %{name}-file-management-%{version} \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-file-management
install -d -m 755 \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-plugin-testing-harness-%{version}
cp -pr maven-plugin-testing-harness-1.0-beta-1/target/site/apidocs/* \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-plugin-testing-harness-%{version}
ln -s %{name}-plugin-testing-harness-%{version} \
      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-plugin-testing-harness

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post file-management
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun file-management
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post plugin-testing-harness
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun plugin-testing-harness
%{clean_gcjdb}
%endif

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%dir %{_javadir}/maven-shared
%dir %{_datadir}/maven2/poms
%{_datadir}/maven2/poms/JPP.maven-shared-components-parent.pom
%{_mavendepmapfragdir}
%config(noreplace) /etc/maven/fragments/maven-shared

%files file-management
%defattr(-,root,root,-)
%{_javadir}/maven-shared/file-management*.jar
%{_datadir}/maven2/poms/JPP.maven-shared-file-management.pom
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/file-management*-%{version}.jar.*
%endif

%files plugin-testing-harness
%defattr(-,root,root,-)
%{_javadir}/maven-shared/plugin-testing-harness*.jar
%{_datadir}/maven2/poms/JPP.maven-shared-plugin-testing-harness.pom
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-testing-harness*-%{version}.jar.*
%endif

%files file-management-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-file-management*

%files plugin-testing-harness-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-plugin-testing-harness*
