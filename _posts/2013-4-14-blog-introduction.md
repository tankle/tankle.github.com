---
layout: post
category : blog安装
tagline: "blog安装入门"
tags : [intro, beginner, jekyll, github, tutorial]
---

git

git是一个分布式版本控制工具(DVCS)，不需要服务端软件支持(即使在地铁里也可以正常commit)，Linux内核开发用的版本控制工具就是它。 常用的SVN属于集中式版本控制工具(CVCS)，需要在服务端开启SVN服务，然后客户端checkout,commit,update。

github

github 的标语是：”secure source code hosting and collaborative development”。

一个基于git的类似google code的代码仓库，付费版的用户可以创建私有仓库，支持多人开发。

很多项目都选择了github来保存代码，如”jQuery/reddit/RoR/CakePHP/Redis”等等。

github pages

blog是在pages的基础上搭建的，创建一个用户的页面很简单，假设你的Github用户名为foo

新建一个仓库(repository)，名称填”foo.github.com”
按照guide完成
\# 在本地新建一个文件夹foo.github.com

$ mkdir foo.github.com

# 进入文件夹根目录

$ cd foo.github.com

# 初始化

$ git init

$ touch README

$ git add README

# 在根目录下新建一个index.html页面，随便写点什么

# 把index.html加入到仓库中

$ git add .

# 提交修改

$ git commit -m ‘first commit’

# 添加github的分支

$ git remote add origin git@github.com:foo/foo.github.com.git

# 提交到github分支

$ git push origin master

过1分钟左右，浏览http://foo.github.com，就可以看到刚刚创建的index.html文件了。 除了创建用户页面，还可以针对每个项目单独创建项目的主页

创建blog

到这里其实已经可以写博客了，创建一个index.html页面，在里面列出写过的文章，点击标题进去后又是一个手动创建的html页。就是太麻烦了，一点都不酷。

github当然知道这个问题，所以他们创建了jekyll模板引擎 。简单来说，就是你可以用textile 或者markdown语法来写博客，提交到github后，会自动转换成html。

这里有很多网站/博客，都是基于github的jekyll模板开发的，如果觉得哪个不错，可以查看source。 先来看看这个仓库，里面有一些特殊的文件/文件夹：

config.yml

存储了一些设置，大部分的设置都可以通过命令行指定，但放到配置文件里更方便些

layouts

layouts文件夹存放的是模板文件，文章会被渲染到这些模板里，变量指代的是文章内容

posts

这里就是真正存放博客文章的地方了，文件命名要遵守这种格式:year-month-day-title.textile 或者 year-month-day-title.markdown

site

这个文件夹是程序生成的，如果本地没有安装jekyll的话，是不会有这个文件夹的，如果想要先本地预览一下，再提交到github，最好通过.gitignore把这个文件夹排除。

index.html

这个文件也有一个yaml前缀 ，可以指定使用哪个模板，标题等等，所有根文件夹下的.html/.htm/.textile/.markdown都会被解析。

other files/folders

上面没有列出的文件/文件夹都会被jekyll放到_site文件夹下，如css/image/script等等。

jekyll的安装

参考博文pJekyll 非你莫属](http://chxt6896.github.io/blog/2011/11/30/blog-jekyll-install.html)

绑定域名

很简单，新建一个CNAME文本文件，在里面输入域名，如”chxt6896.com”，然后在域名提供商里，指定该域名的CNAME为”chxt6896.github.com”，搞定

添加评论功能

参考博文Disqus 我的评论我做主

参考文章

后记

最后再次感谢github提供了这么好的服务.


Please take a look at [{{ site.categories.api.first.title }}]({{ BASE_PATH }}{{ site.categories.api.first.url }}) 
or jump right into [Usage]({{ BASE_PATH }}{{ site.categories.usage.first.url }}) if you'd like.
