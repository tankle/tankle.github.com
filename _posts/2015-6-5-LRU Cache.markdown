---
layout: post
title:  LeetCode 之 LRU Cache

category: Learning
tags: [LeetCode, 解题报告]
description: |
  LeetCode 之 LRU Cache解题报告。
---
{% include JB/setup %}

##题目
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

##解题方法
首先构建一个cache的数据结构

对于所有的cacheNodes使用一个双向链表来链接，以便删除和插入

再构建一个hash表，key为cache的key，value为cacheNode保存的地址，快速定位cacheNode所在位置

{% highlight cpp %}
class LRUCache{
private:

    struct CacheNode{
      int key;
      int value;
      CacheNode(int k, int v) :key(k), value(v){};
    }; 
    
    int capacity;
    list<CacheNode> cachelist;
    unordered_map<int, list<CacheNode>::iterator> cacheMap;
public:

    LRUCache(int capacity) {
        this->capacity = capacity;        
    }
    
    int get(int key) {
        //如果该key存在，就放入list头，并返回该值，否则返回-1
        if(cacheMap.find(key) == cacheMap.end()) return -1;
        
        //将cacheMap[key]插入到头部 http://www.cplusplus.com/reference/list/list/splice/
        cachelist.splice(cachelist.begin(), cachelist, cacheMap[key]);
        cacheMap[key] = cachelist.begin();
        return cacheMap[key]->value;
    }
    
    void set(int key, int value) {
        //首先得判断是否存在，存在，则放入头部,并更新值
        //不存在，且列表大小超过了capacity，则删除最后一个，再在头部插入
        //没有就插入到头部
        if(cacheMap.find(key) == cacheMap.end()){
            if(cachelist.size() == this->capacity){
                cacheMap.erase(cachelist.back().key);
                cachelist.pop_back();
            }
            cachelist.push_front(CacheNode(key,value));
            cacheMap[key] = cachelist.begin();
        }else{
            cachelist.splice(cachelist.begin(), cachelist, cacheMap[key]);
            cacheMap[key] = cachelist.begin();
            cacheMap[key]->value = value;
        }
    }
};
{% endhighlight %}
