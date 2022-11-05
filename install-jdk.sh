#!/bin/bash

#Login as root
sudo su

#create jdk directory
mkdir /opt/jdk

#uncompress, change to your file name
tar -zxf jdk-8u5-linux-x64.tar.gz -C /opt/jdk

#check if files are there
#ls /opt/jdk

#update alternatives so the command java point to the new jdk 
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_05/bin/java 100


#update alternatives so the command javac point to the new jdk 
update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_05/bin/javac 100

#check if java command is pointing to " link currently points to /opt/jdk/jdk1.8.0_05/bin/java"
update-alternatives --display java

#check if java command is pointing to " link currently points to /opt/jdk/jdk1.8.0_05/bin/javac"
update-alternatives --display javac

#check if java is running
java -version

# choose alternative to new java
update-alternatives --config java

# choose alternative to new javac
update-alternatives --config javac
