---
layout: post
title: "leetcode two sum"
category: Learning
tags: [leetcode, 解题报告, two sum]
description: |
  leetcode two sum 解题报告
---
{% include JB/setup %}



大概将近两年没用c++写过代码了，连基本的写法都忘记了。为了重拾C++基本知识，打算用C++来敲一下leetcode上的题目。没想到碰到第一道题目就想了好久。:-(

leetcode的oj有个好处就是能够提供哪组测试数据出错了。这个很方便我们来调试我们得代码。

这是用hash来做的。


    vector<int> twoSum(vector<int> &numbers, int target) {
        map<int,int> pair;
        vector<int> res;
        for(int i=0; i<numbers.size(); i++){
            int tmp = target - numbers[i];
            if(pair.find(tmp) != pair.end() ){
                res.push_back(pair[tmp]+1);
                res.push_back(i+1);
                break;
            }
            else{
                pair[numbers[i]] = i;
            }
        }
        return res;
    }



