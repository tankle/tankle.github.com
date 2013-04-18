---
layout: splash
title: "技术文档 &amp; 学习笔记"
---
{% include JB/setup %}

## 1 - 学习Jekyll

<ul class="thumbnails">
  {% assign pages_icons = site.tags.jekyll %}
  {% include custom/pages_reversed %}
</ul>

##2 - 学习笔记

<ul class="thumbnails">
  {% assign pages_icons = site.categories.learning %}
  {% include custom/pages_reversed %}
</ul>

##3 - 开发辅助

<ul class="thumbnails">
  {% assign pages_icons = site.categories.tool %}
  {% include custom/pages_reversed %}
</ul>