---
layout: post
title: "Git简明手册"
category: tool
tags: [git, github, heroku]
description: |
  Git是一个由林纳斯·托瓦兹为了更好地管理linux内核开发而创立的分布式版本控制／软件配置管理软件。如今已经超越CVS、SVN称为主流的版本控制器。许多著名的开源项目都用Git管理。
---
{% include JB/setup %}

##概述

如果第一次启动Git（[Windows下的Git](http://msysgit.github.com/)），需要设置用户名和邮箱地址：
{% highlight bash %}
$ git config --global user.name "My Name"
$ git config --global user.email "user@email.com"
{% endhighlight %}

<span style="float:right"><a href="http://git-scm.org"><img src="/res/images/git.png" alt="Git" /></a></span>
###关于Git，GitHub和Heroku

- **Git**是一个自由开源的版本控制器，它被设计用来高效管理大大小小的项目。
- **GitHub**是一个用于使用Git版本控制系统的项目的基于互联网的存取服务，使用Ruby on Rails开发而成，是目前最流行的Git存取站点，许多优秀的开源项目都托管在[GitHub](https://github.com/)上。
- **Heroku**是一个基于PaaS的云服务平台，支持包括Java，Ruby，Node.js，和Clojure在内的多种语言开发的应用程序。

##Git基本的工作流程

- 初始化（init）一个新的版本库，然后将目录中的所有文件纳入管理，Git把这个过程称为stage，最后以快照的方式提交所有文件。
{% highlight bash %}
$ git init
$ git add .
$ git commit -m 'initial commit'
{% endhighlight %}

- 创建一个新的分支（branch），将它检出（checkout）为活动分支，然后就可以编辑、载入和提交新的快照。
{% highlight bash %}
$ git branch featureA
$ git checkout featureA
# (edit files)
$ git add (files)
$ git commit -m 'add feature A'
{% endhighlight %}

<code>git add (files)</code>中\(files\)可以使具体的文件名，匹配所有用<code>git add .</code>。

转换到master分支，恢复featureA分支中刚刚做的更改，然后编辑一些文件，并将这些更改提交到master分支。
{% highlight bash %}
$ git checkout master
$ (edit files)
$ git commit -a -m 'change files'
{% endhighlight %}

合并（merge）featureA分支到master分支，结合你的项目需要，可以删掉featureA分支。
{% highlight bash %}
$ git merge featureA
$ git branch -d featureA
{% endhighlight %}
![git操作](/res/images/local-remote.png "git本地-远程操作")

##启动&初始化

Git的配置、版本库初始化（init）和克隆（clone）。
<table border="1" style="width:90%">
	<tr><td>git config [key] [value]</td><td>配置版本库参数</td></tr>
	<tr><td>git config --global [key] [value]</td><td>为用户设置全局属性</td></tr>
	<tr><td>git init</td><td>将已经存在的一个目录初始化为Git版本库</td></tr>
	<tr><td>git clone [url]</td><td>从一个URL地址克隆（clone）一个Git版本库</td></tr>
	<tr><td>git help [command]</td><td>获取帮助</td></tr>
</table>

##暂存&快照

使用Git的快照（snapshots）和暂存区（staging area）。

<table border="1" style="width:90%;">
	<tr><td>git status</td><td>显示下次提交的暂存区的状态和工作目录的更改</td></tr>
	<tr><td>git add [file]</td><td>添加文件到暂存区</td></tr>
	<tr><td>git reset [file]</td><td>重置暂存区的一个文件使之前的更改不被暂存</td></tr>
	<tr><td>git diff</td><td>显示未暂存的更改（即比较暂存和未暂存的项）</td></tr>
	<tr><td>git diff --staged</td><td>显示未提交的更改（即比较暂存区和版本库）</td></tr>
	<tr><td>git commit</td><td>以一个新的快照提交暂存项</td></tr>
	<tr><td>git rm [file]</td><td>从工作目录和暂存区移除文件</td></tr>
	<tr><td>git gui</td><td>启动Git GUI图形界面</td></tr>
</table>

##分支&合并

使用Git的分支（branch）和临时存放（stash）。

<table border="1" style="width:90%;">
	<tr><td>git branch</td><td>列出当前的所有分支，前边加<code>*</code>号的为当前活动分支</td></tr>
	<tr><td>git branch [branch-name]</td><td>以当前的提交创建一个新的分支</td></tr>
	<tr><td>git checkout [branch]</td><td>切换到另一个分支，并检出到当前工作目录</td></tr>
	<tr><td>git checkout -b [branch]</td><td>创建一个新的分支并切换到该分支</td></tr>
	<tr><td>git merge [branch]</td><td>进另一个分支合并到当前活动分支，并将此次合并记录为一次提交</td></tr>
	<tr><td>git log</td><td>显示提交日志</td></tr>
	<tr><td>git stash</td><td>临时存储当前未提交的更改</td></tr>
	<tr><td>git stash apply</td><td>恢复最后一次的临时存储</td></tr>
</table>

##共享&更新

抓取（fetch）、合并（merge），以及从另一个版本库获取更新。

<table border="1" style="width:90%;">
	<tr><td>git remote add [alias] [url]</td><td>为一个URL地址添加别名</td></tr>
	<tr><td>git fetch [alias]</td><td>从远程版本库拉取所有分支</td></tr>
	<tr><td>git merge [alias]/[branch]</td><td>合并一个分支到当前活动分支，是当前活动分支更新到最新版本</td></tr>
	<tr><td>git push [alias] [branch]</td><td>推送本地分支到远程版本库，使远程版本库获得更新</td></tr>
	<tr><td>git pull</td><td>从当前分支跟踪的远程分支中合并数据到本地</td></tr>
</table>

##检查&比较

抓取（fetch）、合并（merge），以及从另一个版本库获取更新。

<table border="1" style="width:90%;">
	<tr><td>git log</td><td>显示当前分支的提交历史</td></tr>
	<tr><td>git log branchB..branchA</td><td>显示branchA有而branchB没有的提交</td></tr>
	<tr><td>git log --follow [file]</td><td>显示该文件的提交记录，包括重命名</td></tr>
	<tr><td>git diff branchB...branchA</td><td>显示在branchA中而不在branchB中的不同</td></tr>
	<tr><td>git show [SHA]</td><td>显示人可读格式的文件的</td></tr>
	<tr><td>gitx</td><td>在GUI中显示提交记录</td></tr>
</table>

##参与GitHub上的开源项目

先将托管在GitHub上的项目克隆（clone）到本地，做过更改之后推送回GitHub，然后发送一个pull请求，项目的维护者就会收到邮件通知。
在GitHub上fork（拷贝一份到你的版本库列表）项目：
{% highlight bash %}
$ git clone https://github.com/my-user/project
$ cd project
# (edit files)
$ git add (files)
$ git commit -m 'Explain what I changed'
$ git push origin master
{% endhighlight %}

然后到[GitHub](http://github.com)上点击<code>pull request</code>按钮。

##使用Git部署到Heroku

使用Heroku的命令行工具创建和管理远程应用：
{% highlight bash %}
$ heroku create
[Creating glowing-dusk-965... done, stack is bamboo-mri-1.9.2
http://glowing-dusk-965.heroku.com/ <http://glowing-dusk-965.
heroku.com/> | git@heroku.com:glowing-dusk-965.git <x-msg://536/
git@heroku.com:glowing-dusk-965.git> Git remote heroku added]
{% endhighlight %}

使用Git部署应用：
{% highlight bash %}
$ git push heroku master
{% endhighlight %}

创建一个额外的Heroku应用暂存，并将远程的暂存命名为“staging”：
{% highlight bash %}
$ heroku create my-staging-app --remote staging
{% endhighlight %}

用Git部署远程的暂存：
{% highlight bash %}
$ git push staging master
{% endhighlight %}

<table width="90%">
	<tr>
		<td><a href="http://github.com"><img src="/res/images/github.png" alt="GitHub" /></a></td>
		<td><a href="http://www.heroku.com"><img src="/res/images/heroku.png" alt="Heroku" /></a></td>
	</tr>
</table>