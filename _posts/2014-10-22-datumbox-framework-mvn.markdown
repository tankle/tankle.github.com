---
layout: post
title: "mvn 编译 datumbox-framework 失败，缺少lpsolve包"
category: Linux
tags: [datumbox-framework, mvn, lpsolve]
description: |
  mvn 编译 datumbox-framework 失败，缺少lpsolve包。
---

{% include JB/setup %}

##失败原因
使用mvn 编译开源机器学习包datumbox-framework时，因缺少lpsolve包而造成编译失败
```bash
$mvn package #出现如下错误
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1:45.186s
[INFO] Finished at: Tue Oct 21 15:06:49 CST 2014
[INFO] Final Memory: 10M/173M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal on project datumbox-framework: Could not resolve dependencies for project com.datumbox:datumbox-framework:jar:0.5.0: Could not find artifact lpsolve:lpsolve:jar:5.5.2.0 in central (http://repo.maven.apache.org/maven2) -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/DependencyResolutionException
```

上面的原因是因为mvn 源里缺少lpsolve包

我向该作者提交issue，可以去这里看[Github](https://github.com/datumbox/datumbox-framework/issues/1),下面是他给我的解决办法。

>1. Download Java wrapper: http://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.0/
2. Install the binary files: http://lpsolve.sourceforge.net/5.5/Java/README.html
3. Install the jar on your local Maven repository.


##解决办法：

自行下载lpsolve包，并添加到mvn 本地源里


###1. 首先下载lpsolve
地址：http://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.0/

总共需要下载三个文件：
lp_solve_5.5.2.0_java.zip
lp_solve_5.5.2.0_exe_ux64.tar.gz
lp_solve_5.5.2.0_dev_ux64.tar.gz

可以根据自己的系统类型下载对应的包。我的系统是ubuntu 64位。

###2. 官方安装说明地址
http://lpsolve.sourceforge.net/5.5/Java/README.html
>Installation
1. Copy the lp_solve dynamic libraries from the archives lp_solve_5.5_dev.(zip or tar.gz) and lp_solve_5.5_exe.(zip or tar.gz) to a standard library directory for your target platform. On Windows, a typical place would be \WINDOWS or \WINDOWS\SYSTEM32. On Linux, a typical place would be the directory /usr/local/lib.
2. Unzip the Java wrapper distribution file to new directory of your choice.
On Windows, copy the wrapper stub library lpsolve55j.dll to the directory that already contains lpsolve55.dll.
3. On Linux, copy the wrapper stub library liblpsolve55j.so to the directory that already contains liblpsolve55.so. Run ldconfig to include the library in the shared libray cache.

1. 首先将lp_solve_5.5.2.0_exe_ux64.tar.gz，lp_solve_5.5.2.0_dev_ux64.tar.gz解压，然后将两个文件夹下的文件都拷贝到/usr/local/lib/lpsolve_5.5目录下（没有，则自己创建)
2. 然后将lp_solve_5.5.2.0_java.zip文件夹下的liblpsolve55j.so文件也拷贝到上各步骤相同文件夹下
3. 最后运行ldconfig
4. 我运行的范例
```bash 
$mkdir /usr/local/lib/lpsolve_5.5
$cp lp_solve_5.5.2.0_exe_ux64/* /usr/local/lib/lpsolve_5.5
$cp lp_solve_5.5.2.0_dev_ux64/* /usr/local/lib/lpsolve_5.5
$cp lp_solve_5.5.2.0_java/lib/ux64/liblpsolve55j.so /usr/local/lib/lpsolve_5.5
$sudo ldconfig

```

###3. 将lpsolve 安装到mvn 本地源中
使用mvn 安装jar命令
```bash
$mvn install:install-file -Dfile=jar包的位置 -DgroupId=包的groupId -DartifactId=包的artifactId -Dversion=包的version -Dpackaging=jar 
```
可以在datumbox-framework目录下pom.xml找到lpsolve包的信息
```
    <dependency>
        <groupId>lpsolve</groupId>
        <artifactId>lpsolve</artifactId>
        <version>5.5.2.0</version>
    </dependency>
```
下面我们运行下面的命令
```bash
$mvn install:install-file -Dfile=lp_solve_5.5_java/lib/lpsolve55j.jar -DgroupId=lpsolve -DartifactId=lpsolve -Dversion=5.5.2.0 -Dpackaging=jar
```
然后就会看到如下信息表示安装成功
```
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 42.056s
[INFO] Finished at: Wed Oct 22 11:20:17 CST 2014
[INFO] Final Memory: 6M/61M
[INFO] ------------------------------------------------------------------------

```

###4. 最后就可以编译啦
不过需要注意的是，java的版本要是1.8 的，也就是java8，不然会编译有问题
```bash
$mvn package
```



