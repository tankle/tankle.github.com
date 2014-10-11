---
layout: post
title: "在RedHat中安装mysql php apahce phpmyadmin"
category: linux
tags: [linux] [RedHat] [mysql] [php] [apache]
description: |
    在RedHat中安装mysql，php，apache等服务。
---
{% include JB/setup %}

###1.安装php，需要安装mysql扩展，
{% highlight bash%}
$yum install php php-mysql php-gd
{% endhighlight %}

###2. 安装mysql server 和mysql
{% highlight bash%}
$yum install mysql-server mysql
{% endhighlight %}

###3. 安装apache
{% highlight bash%}
$yum install httpd
{% endhighlight %}

###4. 安装phpmyadmin,由于centos源中不包含phpmyadmin，因此使用fedora版本。
{% highlight bash%}
$cd /tmp
$wget http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
$rpm -ivh epel-release-5-4.noarch.rpm
$yum install phpmyadmin
{% endhighlight %}
安装好之后，还需要配置写phpmyadmin才能让外网可以访问。

修改这个文件/etc/httpd/conf.d/phpMyAdmin.conf
{% highlight bash%}
<Directory /usr/share/phpMyAdmin/>
   order deny,allow
   allow from all
</Directory>
{% endhighlight %}

这个只是粗暴的修改，可以设定只有某些ip可以访问，比如localhost