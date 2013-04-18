---
layout: post
title: "使用Liquid模板语言"
category: develop
tags: [jekyll]
description: |
  Liquid是一模板引擎语言，从电子商务系统Shopify提取而来。Ruby库渲染的安全模板，不影响服务器上的安全性。
---
{% include JB/setup %}

## 介绍

Jekyll使用了标准的Liquid模板语言包，并且加入了一些实用的扩展。Jekyll-bootstrap不支持插件扩展，因为我们自己就是终端用户，这是Jekyll-bootstrap作者给出的解释，好像不是很有道理。但是作为一个简单的静态网站生成工具，Liquid提供的逻辑运算和过滤、循环等功能显然已经足够了。毕竟我们不会依靠他来编写复杂的运算程式。 

## Liquid速成

下边的链接包含了对Liquid语法全面的介绍，虽然是英语的，但是对于饱受英语折磨数十年之久的Chinese student（哪怕以前是）应该都是能看懂的，就不用我翻译了。

<http://github.com/Shopify/liquid/wiki/Liquid-for-Designers>

## Jekyll提供的扩展

Jekyll自己提供的一些扩展还是有点用的，不妨看一看:

<http://github.com/mojombo/jekyll/wiki/Liquid-Extensions>


[![Build Status](https://secure.travis-ci.org/Shopify/liquid.png)](http://travis-ci.org/Shopify/liquid)


