---
layout: post
title: "语言检测工具language detector"
category: Develop
tags: [NLP]
description: |
  使用朴素贝叶斯实现的语言检测工具 language detector
---

{% include JB/setup %}



该工具是一个使用java实现的语言检测工具，使用的是朴素贝叶斯方法，对噪声少的语言句子，准确率能达到99%，目前已经能够支持53种语言。


[官网](https://code.google.com/p/language-detection/)

以下是一个简单的java示例：

{% highlight java %}  
import java.util.ArrayList;
 import com.cybozu.labs.langdetect.Detector;
 import com.cybozu.labs.langdetect.DetectorFactory;
 import com.cybozu.labs.langdetect.Language;
 
 class LangDetectSample {
    //初始化DetectorFactory
     public void init(String profileDirectory) throws LangDetectException {
         DetectorFactory.loadProfile(profileDirectory);
     }
     //调用此方法来检测句子
     public String detect(String text) throws LangDetectException {
         Detector detector = DetectorFactory.create();
         detector.append(text);
         return detector.detect();
     }
     //检测句子被分成对应语言的概率
     public ArrayList detectLangs(String text) throws LangDetectException {
         Detector detector = DetectorFactory.create();
         detector.append(text);
         return detector.getProbabilities();
     }
     
 }
{% endhighlight %}

对于使用python来调用java的人，可以使用jpype，这个非常方便来调用java程序，既可以是java标准程序，也可以是第三方包。

下面是用python来检测语言的示例：

{% highlight python %}  
import jpype
import os.path
jarpath = os.path.join(os.path.abspath('.'), r"D:\sourcecode\langdetect\lib")
jpype.startJVM(jpype.getDefaultJVMPath(),"-Djava.ext.dirs=%s" % jarpath)
defac = jpype.JClass("com.cybozu.labs.langdetect.DetectorFactory")
defac.loadProfile("D:\sourcecode\langdetect\profiles")
detect = jpype.JClass("com.cybozu.labs.langdetect.Detector")
detect = defac.create()
detect.append("""hello world""")
jpype.java.lang.System.out.println(detect.detect())
jpype.java.lang.System.out.println(detect.getProbabilities())

jpype.shutdownJVM()
{% endhighlight %}


该工具虽然说号称准确率能达到99%， 但这也只是针对句子较长（抽取的ngram特征多），句子正规,比较少出现口语化，最近在做一个社区问答，使用该工具来检测回答是否非英语，但由于社区问答中，口语化叫严重，造成准确率较低。



