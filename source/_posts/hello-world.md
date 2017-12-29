---
title: Hello World
---
Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).

## Quick Start

### Create a new post

``` bash
$ hexo new "My New Post"
```

More info: [Writing](https://hexo.io/docs/writing.html)

### Run server

``` bash
$ hexo server
```

More info: [Server](https://hexo.io/docs/server.html)

### Generate static files

``` bash
$ hexo generate
```

More info: [Generating](https://hexo.io/docs/generating.html)

### Deploy to remote sites

``` bash
$ hexo deploy
```

More info: [Deployment](https://hexo.io/docs/deployment.html)

### 具体安装过程

#### 初始化以及生成网站
```
$ npm install hexo-cli -g # 这步是安装hexo的命令行
$ hexo init blog
$ cd blog
$ npm install
$ hexo g # 或者hexo generate
$ hexo s # 或者hexo server，可以在http://localhost:4000/ 查看
```

#### 配置
repo 是Github的项目的链接地址
```
deploy:
  type: git
  repo: git@github.com:xxx.git
  branch: master
```

#### 部署
```
$ npm install hexo-deployer-git --save # 需要安装这个插件
$ hexo d # 即可
```

#### 安装插件

在_config.yml配置文件中添加插件信息

```
plugins:
  hexo-generator-feed #RSS订阅插件
  hexo-generator-sitemap  #sitemap插件
然后，安装插件，后面要加上--save，表示依赖项。

RSS订阅插件
hexo-generator-feed：生成rss订阅文件
npm install hexo-generator-feed --save
添加配置信息

# sitemap
sitemap:
  path: sitemap.xml
SiteMap插件
hexo-generator-sitemap：生成易于搜索引擎搜素的网站地图
npm install hexo-generator-sitemap --save
添加配置信息：

# feed
atom:
  type: atom
  path: atom.xml
  limit: 20
可以在主题配置文件中添加相关配置，可以在页面上显示。
比如，添加链接信息




links:
  Feed: /atom.xml
  SiteMap: /sitemap.xml

```
## 参考博客
https://www.jianshu.com/p/5973c05d7100