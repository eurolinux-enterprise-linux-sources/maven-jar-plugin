Name:           maven-jar-plugin
Version:        2.4
Release:        7%{?dist}
Summary:        Maven JAR Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-jar-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Some classes from maven-artifact come in maven-core, added a dep in pom.xml
Patch0:         %{name}-maven-core-dep.patch

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: javapackages-tools >= 0.7.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-archiver
BuildRequires: plexus-archiver
BuildRequires: apache-commons-lang
BuildRequires: plexus-utils
BuildRequires: junit

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

#let plexus-container-default be retrieved as a dependency
sed -i -e "s|plexus-container-default|plexus-container|g" pom.xml

%build
# Test class MockArtifact doesn't override method getMetadata
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-7
- Migrate away from mvn-rpmbuild (#997439)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Nov 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-3
- Install license files
- Use generated maven file lists

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 2.4-1
- Update to 2.4.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Tomas Radej <tradej@redhat.com> - 2.3.2-1
- Updated to 2.3.2

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- Update to 2.3.1.
- Keep plexus-container-default on the dependency tree.
- Drop depmap - not needed now.

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-3
- Add depmap.

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-2
- Requires maven-shared-archiver.

* Thu May 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Initial package
