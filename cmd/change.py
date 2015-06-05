# -*- coding: utf-8 -*-
import sys
import codecs

head = '''---
layout: post
title: %s
category: 
tags: []
description: |
  
---
{%% include JB/setup %%}
'''

inname = sys.argv[1]
print("Reading..."+inname)
f = codecs.open(inname, "r","utf-8")
lines = f.readlines()
f.close()

content = head % (lines[0][1:])
#print(content)
idx = 0
flag = False
for line in lines:
	if flag is False:
		if line.strip() == "---":
			flag = True
			
	else:
		if line.strip() == "```":
			if idx == 0:
				idx = 1
				content += "{% highlight cpp %}\n"
			else:
				idx = 0
				content += "{% endhighlight %}\n"
		else:
			content += line

import os

## if file exists, delete it ##
if os.path.isfile(inname):
        os.remove(inname)
else:    ## Show an error ##
        print("Error: %s file not found" % inname)
		
		
print("writing...")
outf = codecs.open("../_posts/"+inname, "w","utf-8")
outf.write(content)
outf.close()
		