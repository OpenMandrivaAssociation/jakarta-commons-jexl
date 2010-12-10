%define oname commons-jexl

Summary:        Java Expression Language
Name:		jakarta-%{oname}
Version:	1.1
Release:	%mkrel 2
Group:		Development/Java
License:	Apache Software License
URL:		http://jakarta.apache.org/commons/jexl/
Source0:	http://www.apache.net.pl/commons/jexl/source/%{oname}-%{version}-src.tar.gz
BuildRequires:	jpackage-utils >= 0:1.5
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-junit >= 0:1.6
BuildRequires:	junit
BuildRequires:	jakarta-commons-logging
BuildRequires:	java-rpmbuild
Requires:	jakarta-commons-logging
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Jexl is an expression language engine designed for easy embedding in 
applications and frameworks. It implements an extended version of the 
Expression Language of the JSTL.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
%{summary}.


%prep
%setup -q -n %{oname}-%{version}-src

%build
export JAVA_HOME="%{java_home}"
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath jakarta-commons-logging-api jakarta-commons-logging )
CLASSPATH=target/classes:target/test-classes:$CLASSPATH
%ant -Dbuild.sysclasspath=only test dist


%install
rm -rf %{buildroot}
install -Dpm 644 dist/%{oname}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{oname}-%{version}.jar
ln -s %{oname}-%{version}.jar \
  %{buildroot}%{_javadir}/%{oname}.jar
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink


%clean
rm -rf %{buildroot}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(-,root,root)
%doc LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}
