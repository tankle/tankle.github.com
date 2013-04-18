---
layout: post
title: "利用Jekyll搭建个人博客"
category: develop
tags: [jekyll]
description: |
  Jekyll是一个静态网站生成器，用ruby编写而成，结合了markdown、Liquid等技术，简化了静态网站的构建过程，配合disqus等技术，可以方便的生成具有简单动态功能的网站。
---
{% include JB/setup %}

##准备工作

  1. 安装[RubyInstaller](http://rubyinstaller.org/downloads/)
  2. 安装[DevKit](http://rubyinstaller.org/downloads/)
  3. 安装Jekyll：
{% highlight bash %}
$ gem install jekyll
{% endhighlight %}
  4. 安装Python（推荐Python 2.7.2）
  5. 安装Python [setuptools](http://pypi.python.org/pypi/setuptools)，找对应的exe文件下载安装。
  6. 添加 C:\Python27\Scripts（假设你的Python安装在C盘根目录下）到你的path
  7. 安装pygments:
{% highlight bash %}
$ easy_install pygments
{% endhighlight %}
  8. 安装windows下的Git——[msysGit](http://msysgit.github.com/)
  9. 在Github上创建一个账户。Github会引导你如何进行简单的设置，如果你没用过Git，没关系，只管照做。

## 3分钟搭建Jekyll Blog

<form action="#" id="generate_code" class="alert alert-block alert-warn form-inline" style="text-align:center; vertical-align:middle">
  <label>GitHub账号:</label> <input type="text" id="github_username"/> <button class="btn btn-success" onclick="Pc.init()">个性化代码</button>
</form>

### 1 - 创建一个新的个版本库

登陆你的[Github账户](https://github.com/)，创建一个新的版本库，命名为<strong id="repo_name">USERNAME.github.com</strong>

### 2 - 安装Jekyll引导程序（Jekyll-Bootstrap）
<h3 id="2__install_jekyllbootstrap" style="display:none">2 - Install Jekyll-Bootstrap</h3>
{% highlight bash %}
$ git clone https://github.com/plusjade/jekyll-bootstrap.git USERNAME.github.com
$ cd USERNAME.github.com
$ git remote set-url origin git@github.com:USERNAME/USERNAME.github.com.git
$ git push origin master
{% endhighlight %}

### 3 - enjoy

两分钟后你的Blog神奇的出现在 
<a href="http://USERNAME.github.com" id="blog_link">http://USERNAME.github.com</a>

### \*已经在GitHub上创建的Blog?

如果你安装了Jekyll，你可以在本地预览你的Blog:
{% highlight bash %}
$ git clone https://github.com/plusjade/jekyll-bootstrap.git
$ cd jekyll-bootstrap
$ jekyll --server
{% endhighlight %}

在浏览器预览[http://localhost:4000](http://localhost:4000).

[更多介绍](http://jekyllbootstrap.com/lessons/jekyll-introduction.html)

##快速开始

###本地运行Jekyll

假设你已经安装好了jekyll-bootstrap，以及其他一些基本运行环境和工具，首先启动你本地的WEBrick服务器（Ruby自带的）：
{% highlight bash %}
$ cd USERNAME.github.com 
$ jekyll --server
# 别忘了把USERNAME换成你的GitHub用户名。
{% endhighlight %}

你的Blog在这预览: [http://localhost:4000/](http://localhost:4000/)。

###创建第一篇博文
{% highlight bash %}
$ rake post title="Hello World"
{% endhighlight %}

默认情况下rake命令会在你的_posts目录下创建一个名为\[年-月-日-posttitle.md\]的文件，例如2012-05-04-Hello-World.md，名称中的空格会转换成“-”，时间为当前系统时间。当然这些都是可配置的。

rake命令默认不会覆盖掉相同名称的文件。

###创建第一个页面
{% highlight bash %}
# 根目录下创建页面
$ rake page name="about.md"

# 自定义目录下创建页面
$ rake page name="pages/about.md"

# 创建类似./pages/about/index.html目录结构的页面
$ rake page name="pages/about"
{% endhighlight %}

###发布

完成一篇博文或者做一些修改之后可以用简单的git命令提交到远程的Github版本库。同时Github可以将md文件解析成html文件，通过USERNAME.github.com就可以访问刚才提交的博文。
{% highlight bash %}
$ git add .
$ git commit -m "Add new content"
$ git push origin master
{% endhighlight %}

至此你就可以写自己的blog like a hacker。

当然你还可以运用一些预置的[主题](http://themes.jekyllbootstrap.com/)，做一些自定义的配置，以及自己定义主题增加模板配置文件、增加Blog挂件、加入[Google Analytics](http://www.google.com/analytics/)、[Disqus](http://disqus.com/)等等，同样可以将一个静态网站做的栩栩如生。

另外网站默认是托管在Github服务器（实际上是RackSpace的云服务器）上的，你还可以考虑免费的Heroku，至于GAE、EC2（免费一年），显然有些大材小用了。

## 遇到的问题

### 1. 本地post中出现中文不能正常编译

由于windows下的git控制台MinGW默认不支持中文编码，需要将其设置为UTF-8，有两种解决方案：

**临时**：控制台输入以下语句
{% highlight bash %}
$ export LC_ALL=en_US.UTF-8
$ export LANG=en_US.UTF-8
{% endhighlight %}
**永久**：添加两个用户自定义的环境变量，LC_ALL=en_US.UTF-8 和 LANG=en_US.UTF-8（你想的没错，就是修改windows环境变量）

另外Jekyll默认的Markdown引擎markup对中文的解析不是很好，建议换成rdiscount。在_config.yml文件中pygments: true上一行添加markdown: rdiscount。在此之前你必须首先安装Rdiscount。
{% highlight bash %}
$ gem install rdiscount
{% endhighlight %}

### 2. Liquid error: No such file or directory - pygmentize

没有安装Pygments的缘故，如果你安装了python，只需要easy install。
{% highlight bash %}
$ easy_install Pygments
{% endhighlight %}

### 3. Liquid error: bad file descriptor

我的电脑上同时装了python2.7和python3.2，我想是这个原因。需要给albino.rb文件打个补丁，假设你的Ruby安装在D:\Program\，并且你已经把[albino-windows-refactor.patch补丁文件](https://gist.github.com/2592525)copy到了下边的目录：
{% highlight bash %}
$ cd D:\Program\Ruby193\lib\ruby\gems\1.9.1\gems\albino-1.3.3\lib
$ patch < albino-windows-refactor.patch
{% endhighlight %}

### 4. 侧边栏二级目录的链接不起作用

这个问题花了不少时间，最终还是未能找到问题所在，无奈，只有自己动手丰衣足食，自己写js搞定。

首先看一下源码，在assets\app.js文件中的Toc中看可以看到：
{% highlight javascript %}
node.children.each(function(){
    cache += '<li class="sub"><a href="#'+ this.id + '">'+ $(this).text() + '</a></li>';
  })
{% endhighlight %}

显然他在这为链接设置了href，但是调用了h2对象（也就是侧边栏目录的二级菜单）的id属性，而用Firebug查看最终解析成的html文件，发现&lt;h2&gt;的id是不存在的，于是自然想到这在之前先为h2设置唯一的id属性。这个用jQuery很容易就能实现：
{% highlight javascript %}
$("h2").each(function(){$(this).attr("id","_"+$(this).text());});
{% endhighlight %}

### 5. 类似于could't parse YAML at line 6 column 6 \(Psych::SyntaxError\)的问题

YAM了貌似对空格比较敏感，需要一个空格的时候就不要敲多个空格，同时注意你的Tab缩进，_config.yml中的属性都是key: value形式的，别忘了：后边有个空格。

另外post文件头中的属性配置也要注意：
<pre><code>
---
layout: post
title : post_title
categories : category_name
description: |
  This is a decription.
---
</code></pre>
description第二行开头我敲了一个Tab（四个字符宽度）就出错了，一些细节，注意一下就好了。

##域名绑定##

Github会为你分配一个类似于USERNAME.github.com的二级域名，如果你自己有一个顶级域名，你可以将它与Github提供的一个共有IP(204.232.175.78)绑定，这个在[Github Pages](http://help.github.com/pages/)上有详细介绍，在你的网站根目录下增加一个CNAME文件，里边写你自己的域名，再给你的域名增加一条A记录，稍等片刻之后就可以用你的域名访问了。

当然域名是需要花钱的，如果你舍不得花银子，免费的午餐还是会有的，你可以免费申请一个（当然也可以是多个）.tk的域名。[DotTK](http://www.dot.tk/zh/index.html)提供yourname.tk的免费顶级域名。.tk是南太平洋岛国托克劳的国家域名，免费注册一个帐户可以任意申请.tk域名，支持域名转发（可隐藏原URL）、电邮转发、A记录解析、CNAME别名记录、MX邮件记录、设置DNS服务器等服务。当然免费的总是会有一些限制条件喽。

  - 如果你注册的域名在90天内访问量少于25个，你的域名将被删除！
  - 如果你开通的电邮转发在90天内收到的邮件少于10封，你的电邮转发服务将被停止！

另外很多看起来不错的域名不是免费的，要交费才能注册使用！比如说cn.tk。

注册流程很简单，有中文版的，几十秒钟你的免费顶级域名就到手了，是不是很happy！