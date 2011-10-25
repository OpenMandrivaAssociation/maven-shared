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

%global shared_components_version 15
%global file_management_version 1.2.2
%global ant_version 1.0

%global artifact_resolver_version 1.1

%global common_artifact_filters_version 1.3
%global dependency_analyzer_version 1.2
%global dependency_tree_version 1.3
%global downloader_version 1.2

# missing?
%global plugin_testing_harness_version 1.2

%global filtering_version 1.0

%global invoker_version 2.0.12
%global model_converter_version 2.3
%global osgi_version 0.3.0

#this model is not included in parent pom
%global reporting_api_version 3.0

%global reporting_impl_version 2.1
%global repository_builder_version 1.0

%global runtime_version 1.0

%global io_version 1.2
%global jar_version 1.1
%global monitor_version 1.0
### disabled by pom.xml default
#%global script_ant_version 2.1
#%global script_beanshell_version 2.1
#%global test_tools_version 1.0
#%global toolchain_version 1.0
%global verifier_version 1.3

Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           maven-shared
Version:        15
Release:        16
License:        ASL 2.0
Group:          Development/Java

# svn export \
# http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-components-15/
# tar czf maven-shared-components-14.tar.gz maven-shared-components-15
Source0:        maven-shared-components-%{version}.tar.gz
Source1:        %{name}-jpp-depmap.xml

Patch0:        %{name}-pom.patch
Patch1:        maven-ant-pom_xml.patch
Patch2:        maven-dependency-tree-pom.patch
Patch3:        maven-osgi-pom.patch
Patch4:        maven-repository-build-pom.patch
Patch5:        maven-runtime-pom.patch
Patch6:        maven-runtime-XMLMavenRuntimeVisitor.patch
Patch7:        maven-artifact-resolver-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-report-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia-tools
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-plugin-testing-tools
BuildRequires:  maven-test-tools
BuildRequires:  plexus-maven-plugin
BuildRequires:  plexus-component-api
BuildRequires:  maven-plugin-cobertura
BuildRequires:  junit
BuildRequires:  saxon
BuildRequires:  saxon-scripts
BuildRequires:  plexus-utils
BuildRequires:  plexus-digest
BuildRequires:  modello
BuildRequires:  easymock2
BuildRequires:  objectweb-asm
BuildRequires:  dom4j
BuildRequires: aqute-bndlib
BuildRequires:  maven-wagon

Requires:       ant
Requires:       ant-nodeps
Requires:       maven2 >= 0:2.0.4
Requires:       plexus-utils
Requires:       saxon
Requires:       saxon-scripts
Requires:       plexus-utils
Requires:       plexus-digest
Requires:       objectweb-asm
Requires:       dom4j
Requires:       aqute-bndlib
Requires:       maven-wagon

BuildArch:      noarch

Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description
Maven Shared Components

%package file-management
Summary:        Maven Shared File Management API
Group:          Development/Java
Version:        %{file_management_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  %{name}-io >= 0:%{io_version}
Requires:  maven2
Requires:  plexus-container-default
Requires:  plexus-utils

%description file-management
API to collect files from a given directory using
several include/exclude rules.

%package osgi
Summary:        Maven OSGi
Group:          Development/Java
Version:        %{osgi_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  aqute-bndlib
Requires:  maven

%description osgi
Library for Maven-OSGi integration

%package ant
Summary:        Maven Ant
Group:          Development/Java
Version:        %{ant_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  ant
Requires:  maven
Requires:  plexus-containers-container-default

%description ant
Runs ant scripts embedded in the POM.

%package common-artifact-filters
Summary:        Maven Common Artifact Filters
Group:          Development/Java
Version:        %{common_artifact_filters_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  %{name}-test-tools >= 0:%{test_tools_version}-%{release}
Requires:  junit
Requires:  maven
Requires:  plexus-container-default

%description common-artifact-filters
%{summary}.

%package dependency-tree
Summary:        Maven Dependency Tree
Group:          Development/Java
Version:        %{dependency_tree_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  %{name}-plugin-testing-harness >= 0:%{plugin_testing_harness_version}-%{release}
Requires:  maven

%description dependency-tree
%{summary}.

%package downloader
Summary:        Maven Downloader
Group:          Development/Java
Version:        %{downloader_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  maven

%description downloader
Provide a super simple interface for downloading a
single artifact.

%package dependency-analyzer
Summary:        Maven Dependency Analyzer
Group:          Development/Java
Version:        %{dependency_analyzer_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  maven
Requires:  objectweb-asm

%description dependency-analyzer
%{summary}.

%package invoker
Summary:        Maven Process Invoker
Group:          Development/Java
Version:        %{invoker_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  %{name}-monitor >= 0:%{monitor_version}-%{release}
Requires:  maven
Requires:  plexus-utils

%description invoker
%{summary}.

%package model-converter
Summary:        Maven Model Converter
Group:          Development/Java
Version:        %{model_converter_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  dom4j
Requires:  maven
Requires:  plexus-container-default
Requires:  plexus-utils

%description model-converter
Converts between version 3.0.0 and version 4.0.0 models.

%package reporting-impl
Summary:        Maven Reporting Implementation
Group:          Development/Java
Version:        %{reporting_impl_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  jakarta-commons-validator
Requires:  jakarta-oro
Requires:  maven
Requires:  maven-doxia

%description reporting-impl
%{summary}.

%package repository-builder
Summary:        Maven Repository Builder
Group:          Development/Java
Version:        %{repository_builder_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  %{name}-common-artifact-filters = 0:%{common_artifact_filters_version}-%{release}
Requires:  maven

%description repository-builder
%{summary}.

%package io
Summary:        Maven Shared I/O API
Group:          Development/Java
Version:        %{io_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  maven
Requires:  maven-wagon
Requires:  plexus-utils
Requires:  plexus-container-default

%description io
%{summary}.

%package jar
Summary:        Maven Shared Jar
Group:          Development/Java
Version:        %{jar_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  maven

%description jar
Utilities that help identify the contents of a JAR,
including Java class analysis and Maven metadata
analysis.

%package monitor
Summary:        Maven Shared Monitor API
Group:          Development/Java
Version:        %{monitor_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  maven
Requires:  plexus-container-default

%description monitor
%{summary}.

%package verifier
Summary:        Maven Verifier Component
Group:          Development/Java
Version:        %{verifier_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  junit

%description verifier
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java 
Provides:       %{name}-file-management-javadoc = %{file_management_version}-%{release}
Obsoletes:      %{name}-file-management-javadoc < %{file_management_version}-%{release}
Provides:       %{name}-plugin-testing-harness-javadoc = %{plugin_testing_harness_version}-%{release}
Obsoletes:      %{name}-plugin-testing-harness-javadoc < %{plugin_testing_harness_version}-%{release}

%description javadoc
%{summary}.

%package artifact-resolver
Summary:        Maven Artifact Resolution API
Group:          Development/Java
Version:        %{artifact_resolver_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  ant
Requires:  maven

%description artifact-resolver
Provides a component for plugins to easily resolve project dependencies.

%package filtering
Summary:        Maven Filtering
Group:          Development/Java
Version:        %{filtering_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  ant
Requires:  maven

%description filtering
A component to assist in filtering of resource files with properties from a Maven project.

%package reporting-api
Summary:        Maven Reporting API
Group:          Development/Java
Version:        %{reporting_api_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  ant
Requires:  maven

%description reporting-api
Maven Reporting API.

%package runtime
Summary:        Maven Runtime
Group:          Development/Java
Version:        %{runtime_version}
Requires:  %{name} = 0:%{shared_components_version}-%{release}
Requires:  ant
Requires:  maven

%description runtime
Maven Runtime allows introspection of Maven project metadata at runtime.  Basic artifact information or full Maven
project metadata can be obtained for all projects within a given class loader, optionally sorted into dependency
order, and also for a given class within a project.

%prep
%setup -q -n %{name}-components-%{shared_components_version}
chmod -R go=u-w *
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5
%patch6 -p0 -b .sav6
%patch7 -p0 -b .sav7

# need namespace for new version modello
sed -i "s|<model>|<model xmlns=\"http://modello.codehaus.org/MODELLO/1.3.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://modello.codehaus.org/MODELLO/1.3.0 http://modello.codehaus.org/xsd/modello-1.3.0.xsd\" xml.namespace=\"..\" xml.schemaLocation=\"..\" xsd.namespace=\"..\" xsd.targetNamespace=\"..\">|" file-management/src/main/mdo/fileset.mdo
sed -i "s|<groupId>ant|<groupId>org.apache.ant|g" maven-ant/pom.xml

# Remove test that needs junit-addons until that makes it into Fedora
rm -f maven-reporting-impl/src/test/java/org/apache/maven/reporting/AbstractMavenReportRendererTest.java

# Remove tests that need jmock (for now)
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/InputStreamConstraint.java
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/ClassFileVisitorUtilsTest.java
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/AbstractFileTest.java

%build
mvn-rpmbuild \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate

%install

rm -rf $RPM_BUILD_ROOT
# main package infrastructure
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-shared
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

# poms and jars
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-components-parent.pom
%add_to_maven_depmap org.apache.maven.shared maven-shared-components %{shared_components_version} JPP/maven-shared components-parent

install -pm 644 maven-downloader/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-downloader.pom
%add_to_maven_depmap org.apache.maven.shared maven-downloader %{downloader_version} JPP/maven-shared downloader
install -p -m 0644 maven-downloader/target/maven-downloader-%{downloader_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/downloader.jar

install -pm 644 maven-dependency-analyzer/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-dependency-analyzer.pom
%add_to_maven_depmap org.apache.maven.shared maven-dependency-analyzer %{dependency_analyzer_version} JPP/maven-shared dependency-analyzer
install -p -m 0644 maven-dependency-analyzer/target/maven-dependency-analyzer-%{dependency_analyzer_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/dependency-analyzer.jar

install -pm 644 maven-dependency-tree/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-dependency-tree.pom
%add_to_maven_depmap org.apache.maven.shared maven-dependency-tree %{dependency_tree_version} JPP/maven-shared dependency-tree
install -p -m 0644 maven-dependency-tree/target/maven-dependency-tree-%{dependency_tree_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/dependency-tree.jar

install -pm 644 maven-verifier/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-verifier.pom
%add_to_maven_depmap org.apache.maven.shared maven-verifier %{verifier_version} JPP/maven-shared verifier
install -p -m 0644 maven-verifier/target/maven-verifier-%{verifier_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/verifier.jar

install -pm 644 maven-shared-monitor/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-monitor.pom
%add_to_maven_depmap org.apache.maven.shared maven-shared-monitor %{monitor_version} JPP/maven-shared monitor
install -p -m 0644 maven-shared-monitor/target/maven-shared-monitor-%{monitor_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/monitor.jar

install -pm 644 maven-shared-io/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-io.pom
%add_to_maven_depmap org.apache.maven.shared maven-shared-io %{io_version} JPP/maven-shared io
install -p -m 0644 maven-shared-io/target/maven-shared-io-%{io_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/io.jar

install -pm 644 maven-shared-jar/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-jar.pom
%add_to_maven_depmap org.apache.maven.shared maven-shared-jar %{jar_version} JPP/maven-shared jar
install -p -m 0644 maven-shared-jar/target/maven-shared-jar-%{jar_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/jar.jar

install -pm 644 maven-repository-builder/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-repository-builder.pom
%add_to_maven_depmap org.apache.maven.shared maven-repository-builder %{repository_builder_version} JPP/maven-shared repository-builder
install -p -m 0644 maven-repository-builder/target/maven-repository-builder-%{repository_builder_version}-alpha-3-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/repository-builder.jar

install -pm 644 maven-reporting-impl/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-reporting-impl.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting-impl %{reporting_impl_version} JPP/maven-shared reporting-impl
install -p -m 0644 maven-reporting-impl/target/maven-reporting-impl-%{reporting_impl_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/reporting-impl.jar

install -pm 644 maven-model-converter/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-model-converter.pom
%add_to_maven_depmap org.apache.maven.shared maven-model-converter %{model_converter_version} JPP/maven-shared model-converter
install -p -m 0644 maven-model-converter/target/maven-model-converter-%{model_converter_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/model-converter.jar

install -pm 644 maven-invoker/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-invoker.pom
%add_to_maven_depmap org.apache.maven.shared maven-invoker %{invoker_version} JPP/maven-shared invoker
install -p -m 0644 maven-invoker/target/maven-invoker-%{invoker_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/invoker.jar

install -pm 644 maven-common-artifact-filters/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-common-artifact-filters.pom
%add_to_maven_depmap org.apache.maven.shared maven-common-artifact-filters %{common_artifact_filters_version} JPP/maven-shared common-artifact-filters
install -p -m 0644 maven-common-artifact-filters/target/maven-common-artifact-filters-%{common_artifact_filters_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/common-artifact-filters.jar

install -pm 644 maven-ant/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-ant.pom
%add_to_maven_depmap org.apache.maven.shared maven-ant %{ant_version} JPP/maven-shared ant
install -p -m 0644 maven-ant/target/maven-ant-%{ant_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/ant.jar

install -pm 644 maven-osgi/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-osgi.pom
%add_to_maven_depmap org.apache.maven.shared maven-osgi %{osgi_version} JPP/maven-shared osgi
install -p -m 0644 maven-osgi/target/maven-osgi-%{osgi_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/osgi.jar

install -pm 644 file-management/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-file-management.pom
%add_to_maven_depmap org.apache.maven.shared file-management %{file_management_version} JPP/maven-shared file-management
install -p -m 0644 file-management/target/file-management-%{file_management_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/file-management.jar

install -pm 644 maven-artifact-resolver/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-artifact-resolver.pom
%add_to_maven_depmap org.apache.maven.shared maven-artifact-resolver %{artifact_resolver_version} JPP/maven-shared artifact-resolver
install -p -m 0644 maven-artifact-resolver/target/maven-artifact-resolver-%{artifact_resolver_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/artifact-resolver.jar

install -pm 644 maven-filtering/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-filtering.pom
%add_to_maven_depmap org.apache.maven.shared maven-filtering %{filtering_version} JPP/maven-shared filtering
install -p -m 0644 maven-filtering/target/maven-filtering-%{filtering_version}-beta-4-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/filtering.jar

install -pm 644 maven-reporting-api/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-reporting-api.pom
%add_to_maven_depmap org.apache.maven.shared maven-reporting-api %{reporting_api_version} JPP/maven-shared reporting-api
install -p -m 0644 maven-reporting-api/target/maven-reporting-api-%{reporting_api_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/reporting-api.jar

install -pm 644 maven-runtime/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-runtime.pom
%add_to_maven_depmap org.apache.maven.shared maven-runtime %{runtime_version} JPP/maven-shared runtime
install -p -m 0644 maven-runtime/target/maven-runtime-%{runtime_version}-alpha-3-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/runtime.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{shared_components_version}
cp -pr target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{shared_components_version}/

ln -s %{name}-%{shared_components_version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%dir %{_javadir}/maven-shared
%dir %{_mavenpomdir}
%{_mavenpomdir}/JPP.maven-shared-components-parent.pom
%{_mavendepmapfragdir}

%files file-management
%defattr(-,root,root,-)
%{_javadir}/maven-shared/file-management*.jar
%{_mavenpomdir}/JPP.maven-shared-file-management.pom

%files osgi
%defattr(-,root,root,-)
%{_javadir}/maven-shared/osgi*.jar
%{_mavenpomdir}/JPP.maven-shared-osgi.pom

%files ant
%defattr(-,root,root,-)
%{_javadir}/maven-shared/ant*.jar
%{_mavenpomdir}/JPP.maven-shared-ant.pom

%files common-artifact-filters
%defattr(-,root,root,-)
%{_javadir}/maven-shared/common-artifact-filters*.jar
%{_mavenpomdir}/JPP.maven-shared-common-artifact-filters.pom

%files dependency-analyzer
%defattr(-,root,root,-)
%{_javadir}/maven-shared/dependency-analyzer*.jar
%{_mavenpomdir}/JPP.maven-shared-dependency-analyzer.pom

%files dependency-tree
%defattr(-,root,root,-)
%{_javadir}/maven-shared/dependency-tree*.jar
%{_mavenpomdir}/JPP.maven-shared-dependency-tree.pom

%files downloader
%defattr(-,root,root,-)
%{_javadir}/maven-shared/downloader*.jar
%{_mavenpomdir}/JPP.maven-shared-downloader.pom

%files invoker
%defattr(-,root,root,-)
%{_javadir}/maven-shared/invoker*.jar
%{_mavenpomdir}/JPP.maven-shared-invoker.pom

%files model-converter
%defattr(-,root,root,-)
%{_javadir}/maven-shared/model-converter*.jar
%{_mavenpomdir}/JPP.maven-shared-model-converter.pom


%files reporting-impl
%defattr(-,root,root,-)
%{_javadir}/maven-shared/reporting-impl*.jar
%{_mavenpomdir}/JPP.maven-shared-reporting-impl.pom

%files repository-builder
%defattr(-,root,root,-)
%{_javadir}/maven-shared/repository-builder*.jar
%{_mavenpomdir}/JPP.maven-shared-repository-builder.pom

%files io
%defattr(-,root,root,-)
%{_javadir}/maven-shared/io*.jar
%{_mavenpomdir}/JPP.maven-shared-io.pom

%files jar
%defattr(-,root,root,-)
%{_javadir}/maven-shared/jar*.jar
%{_mavenpomdir}/JPP.maven-shared-jar.pom

%files monitor
%defattr(-,root,root,-)
%{_javadir}/maven-shared/monitor*.jar
%{_mavenpomdir}/JPP.maven-shared-monitor.pom

%files verifier
%defattr(-,root,root,-)
%{_javadir}/maven-shared/verifier*.jar
%{_mavenpomdir}/JPP.maven-shared-verifier.pom

%files artifact-resolver
%defattr(-,root,root,-)
%{_javadir}/maven-shared/artifact-resolver*.jar
%{_mavenpomdir}/JPP.maven-shared-artifact-resolver.pom

%files filtering
%defattr(-,root,root,-)
%{_javadir}/maven-shared/filtering*.jar
%{_mavenpomdir}/JPP.maven-shared-filtering.pom

%files reporting-api
%defattr(-,root,root,-)
%{_javadir}/maven-shared/reporting-api*.jar
%{_mavenpomdir}/JPP.maven-shared-reporting-api.pom

%files runtime
%defattr(-,root,root,-)
%{_javadir}/maven-shared/runtime*.jar
%{_mavenpomdir}/JPP.maven-shared-runtime.pom

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{shared_components_version}
%doc %{_javadocdir}/%{name}

