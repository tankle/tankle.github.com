---
layout: post
title: "修改Red Hat自带的yum，使用CentOS版本"
category: Linux
tags: [linux，yum]
description: |
  由于，Red Hat自带的yum是要收费的，因此我们需要修改Red Hat自带的包管理系统，改成CentOS免费版。
---
{% include JB/setup %}

###1. 首先查看系统的版本信息:

{% highlight bash %}
[root@localhost ~]# lsb_release -a
LSB Version:    :core-3.1-ia32:core-3.1-noarch:graphics-3.1-ia32:graphics-3.1-noarch
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 5.5 (Tikanga)
Release:        5.5
Codename:       Tikanga

{% endhighlight %}

###2. 删除RedHat自带的yum源
{% highlight bash %}
[root@localhost ~]# rpm -aq|grep yum|xargs rpm -e --nodeps
{% endhighlight %}

###3. 下载新的相关软件包，这四个软件包可能会升级，如果不能下载的话可以自己去http://mirrors.163.com/centos/5/os/i386/CentOS下载最近的rpm包。
{% highlight bash %}
[root@localhost ~]# wget http://mirrors.163.com/centos/5/os/i386/CentOS/yum-fastestmirror-1.1.16-21.el5.centos.noarch.rpm

[root@localhost ~]# wget http://mirrors.163.com/centos/5/os/i386/CentOS/python-iniparse-0.2.3-6.el5.noarch.rpm

[root@localhost ~]# wget http://mirrors.163.com/centos/5/os/i386/CentOS/yum-metadata-parser-1.1.2-4.el5.i386.rpm

[root@localhost ~]# wget http://mirrors.163.com/centos/5/os/i386/CentOS/yum-3.2.22-40.el5.centos.noarch.rpm
{% endhighlight %}

###4. 安装rpm（一定要按照顺序来）

####4.1 安装python-iniparse-0.2.3-6.el5.noarch.rpm 
{% highlight bash %}
[root@localhost ~]# rpm -ivh python-iniparse-0.2.3-6.el5.noarch.rpm 
warning: python-iniparse-0.2.3-6.el5.noarch.rpm: Header V3 DSA signature: NOKEY, key ID e8562897
Preparing...                                                         ########################################### [100%]
file /usr/lib/python2.4/site-packages/iniparse/compat.py from install of python-iniparse-0.2.3-6.el5.noarch conflicts with file from package python-iniparse-0.2.3-4.el5.noarch
file /usr/lib/python2.4/site-packages/iniparse/compat.pyc from install of python-iniparse-0.2.3-6.el5.noarch conflicts with file from package python-iniparse-0.2.3-4.el5.noarch
file /usr/lib/python2.4/site-packages/iniparse/compat.pyo from install of python-iniparse-0.2.3-6.el5.noarch conflicts with file from package python-iniparse-0.2.3-4.el5.noarch
{% endhighlight %}

####4.2 安装yum-metadata-parser-1.1.2-4.el5.i386.rpm
{% highlight bash %}
[root@localhost ~]# rpm -ivh yum-metadata-parser-1.1.2-4.el5.i386.rpm 
warning: yum-metadata-parser-1.1.2-4.el5.i386.rpm: Header V3 DSA signature: NOKEY, key ID e8562897
Preparing...                                                         ########################################### [100%]
1:yum-metadata-parser                                             ########################################### [100%]
{% endhighlight %}

####4.3 安装yum-3.2.22-40.el5.centos.noarch.rpm yum-fastestmirror-1.1.16-21.el5.centos.noarch.rpm，而且这两个包一定要一起安装，要不然会报错的。
{% highlight bash %}
[root@localhost ~]# rpm -ivh yum-3.2.22-40.el5.centos.noarch.rpm yum-fastestmirror-1.1.16-21.el5.centos.noarch.rpm 
warning: yum-3.2.22-40.el5.centos.noarch.rpm: Header V3 DSA signature: NOKEY, key ID e8562897
Preparing...                                                         ########################################### [100%]
1:yum-fastestmirror                                               ########################################### [ 50%]
2:yum                                                             ########################################### [100%]
{% endhighlight %}

###5. 下载CentOS-Base.repo
{% highlight bash %}
[root@localhost yum.repos.d]# wget http://mirrors.163.com/.help/CentOS5-Base-163.repo
{% endhighlight %}

###5. 更改#vi CentOS-Base-163.repo 替换$releaserver 为5或者6[5/6为centos的版本] ， 不然在后面的更新的时候会出问题。


###6. 到这里就可以更新了。
{% highlight bash %}
$yum update -y //这里会更新很多软件，但如果是服务器，有些软件就不用安装
{% endhighlight %}

###7. 到这里就算是更新好了RedHat的yum了。以后安装软件就直接
{% highlight bash %}
$yum install  packagename 
{% endhighlight %}
就可以安装软件了，而且它会自动将依赖的包列出来，让你知道安装某个软件，还需要安装哪些依赖的软件。

