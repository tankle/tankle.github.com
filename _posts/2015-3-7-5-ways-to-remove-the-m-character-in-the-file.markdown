---
layout: post
title: "五种方法用来移除文件中的^M符号"
category: linux
tags: [vim]
description: |
  5 Ways To Remove The ^M Character At The End Of Text Files
---
{% include JB/setup %}

5 Ways To Remove The ^M Character At The End Of Text Files

the Windows text editors place ^M at the end of each line, which is the visual representation for 0x0D, while Unix based systems place 0x0A, in text files.

1. To remove the ^M character, in ViM, write the following in the command mode and press :w to save the changes:

:set fileformat=unix

2. Or, type this script in ViM, in the command mode and type :w to save the changes:

:1,$s/^V^M//g

3. With sed:

$ sed 's/^M//g' filename > newfilename

4. With Dos2Unix:

$ dos2unix filename newfilename

5. With col:

$ cat filename | col -b > newfilename




