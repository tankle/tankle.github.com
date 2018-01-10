---
title: 隐马尔科夫模型实战之拼音转汉字
date: 2018-01-09 18:34:55
tags:
- HMM
- 隐马尔科夫模型
categories:
- 技术
- 机器学习
mathjax: true
---

## 背景
中文输入法有许多不同种的方法，主要有三大类：拼音输入法、形码输入法(如：五笔)和音型码输入法(如：二笔)，而当今最流行的输入法非拼音输入法莫属了。
在拼音输入法中，用户首先将中文转换为拼音，然后输入法根据输入的拼音序列转换为对应的汉字，已完成中文的输入。

在云音乐搜索中，由于用户每输入一个字符就会触发一次搜索，因此在搜索日志当中能收到大量的拼音序列搜索词。比如：zhou jie lun（周杰伦），li rong hao（李荣浩）。如果能够准确识别这些拼音序列，并转换为对应的中文搜索词，能显著提高用户的搜索体验。

## 难点
拼音转汉字的一些难点：
1. 一个拼音对应多个汉字，如何确定一个拼音对应哪个汉字？
2. 拼音序列对应这多种可能的组合方式，如何选出最好的一种组合方式，比如：jie lun，有：杰伦、结论，该选择哪个转换结果呢？

## 方法
用户输入的拼音序列，是一个可以观察到的序列，而拼音对应的汉字则可以看做是一个不可见序列，通过观察变量求解隐藏变量，这是隐马尔科夫模型的强项啊！

### 隐马尔科夫模型简介
一些基本符号的说明：

* Q  是所有可能的隐藏状态的集合, 其中  N  是可能的状态数， 对应所有可能的拼音的状态数量；
* V  是所有可能的观测的集合, 其中  M  是可能的观测数，对应所有可能的汉字的状态数量；
$$Q={q_1,q_2,⋯,q_N},V={v_1,v_2,⋯,v_M}$$
* I  是长度为  T  的隐藏状态序列， 对应用户输入的拼音序列对应的汉字序列；
* O  是对应的观测序列， 对应用户输入的拼音序列；
$$I={i_1,i_2,⋯,i_T},O={o_1,o_2,⋯,o_T}$$

隐马尔科夫模型（HMM，Hidden Markov Models）可以使用一个三元组来刻画$λ=(π,A,B)$:

* $A$为隐藏状态转移概率分布，一般用一个矩阵表示：
$A=[a_{ij}]_{N*N}$, 其中,  $a_{ij}$  是在时刻  t  处于状态 $q_i$ 的条件下时刻  t+1  转移到状态  $q_j$  的概率；
在拼音转换过程中，对应汉字到汉字之间的转移概率；
* $B$为观测概率分布,一般也是用一个矩阵表示：
$B = [b_{ij}]_{M*N}$，其中,  $b_{ij}$  是在时刻  t 下的观察状态 $v_k$ 生成隐藏状态状态 $q_i$ 的概率:
对应拼音到汉字之间的转移概率；
* π  是初始状态概率向量:
$π=（π_i)_N×1  $

### HMM的三个基本问题
* 概率计算问题: 前向-后向算法——动态规划
给定模型$λ=(A,B,π)$和观测序列$O={o_1,o_2,⋯,o_T}$
计算模型 λ 下观测序列 O  出现的概率  $P(O∣λ)$

* 学习问题: Baum-Welch算法(状态未知)——EM
已知观测序列 $O={o_1,o_2,⋯,o_T}$
估计模型  $λ=(A,B,π)$的参数,使得在该模型下观测序列 $P(O∣λ)$  最大

* 预测问题: Viterbi算法——动态规划
已知模型  $λ=(A,B,π)$, 和观测序列  $O={o_1,o_2,⋯,o_T}$
求给定观测序列条件概率  $P(I∣O,λ)$  最大的状态序列  $I={i)1,i_2,⋯,i_T}$

```python
# -*- coding: utf-8 -*-
#
# @author hztancong
#

import numpy as np

# 隐藏状态转移矩阵
trans_prob = {"周杰":0.9,
              "周姐":0.1,
              "周洁":0.3,
              "杰伦":0.8,
              "结论":0.7
              }

# 隐藏状态初始状态
pi = {
    "周":0.5,
    "粥":0.3,
    "杰":0.5,
    "姐":0.4,
    "节":0.2,
    "结":0.3,
    "轮":0.1,
    "伦":0.5,
    "论":0.5,
}

# 观察状态到隐藏状态的转移矩阵
emit_probs = {
    "zhou周":0.5,
    "zhou粥":0.1,
    "jie姐":0.1,
    "jie节":0.1,
    "jie结":0.2,
    "jie杰":0.2,
    "lun轮":0.1,
    "lun伦":0.3,
    "lun论":0.1,
}

def viterbi(word_list, pinyin_list, n, id2word):
    """
    维特比算法求解最大路径问题
    :param word_list:   每个拼音对应的隐藏状态矩阵
    :param n:   可能观察到的状态数， 对应为汉字数量
    :param id2word:    id到汉字的映射
    :return:
    """
    T = len(word_list)  # 观察状态的长度

    delta = np.zeros((T, n))
    # 保存转移下标值
    psi = np.zeros((T, n), dtype=int)

    # 初始化第一个字符的转移概率， 设置为每个词在词典中的单独出现的概率
    words = word_list[0]
    for w in words:
        delta[0][w] = pi[id2word[w]]

    # 动态规划计算
    for idx in range(1, T):
        words = word_list[idx]
        for i in range(len(words)):
            max_value = 0
            pre_words = word_list[idx-1]
            index = 1
            for j in range(len(pre_words)):
                tmp_key = id2word[pre_words[j]] + id2word[words[i]]
                # 获得转移概率，如果不存在，转移概率则为0
                if tmp_key in trans_prob:
                    prob = trans_prob[tmp_key]
                else:
                    prob = 0
                tmp_value = delta[idx-1][pre_words[j]] * prob
                if max_value < tmp_value:
                    max_value = tmp_value
                    index = j

            # 计算观察状态到隐藏状态的概率
            tmp_key = pinyin_list[idx] + id2word[words[i]]
            emit_prob = emit_probs[tmp_key] * max_value

            delta[idx][words[i]] = emit_prob
            psi[idx][words[i]] = pre_words[index]

    # print delta
    # 终止

    prob = 0
    path = np.zeros(T, dtype=int)
    path[T - 1] = 1
    # 获取最大的转移值
    for i in range(n):
        if prob < delta[T - 1][i]:
            prob = delta[T - 1][i]
            path[T - 1] = i


    # 最优路径回溯
    for t in range(T - 2, -1, -1):
        path[t] = psi[t+1][path[t+1]]

    # 生成解析结果
    final_word = ""
    for i in range(T):
        final_word += id2word[path[i]]

    print final_word

if __name__ == "__main__":
    pinyin_list = ["zhou", "jie", "lun"]
    word_list = [["周", "粥"], ["杰", "姐", "节", "结"], ["轮", "伦", "论"]]
    words = set()
    for wl in word_list:
        for w in wl:
            words.add(w)

    word2idx = dict()
    id2word = dict()
    idx = 0
    for w in words:
        word2idx[w] = idx
        id2word[idx] = w
        idx += 1

    # 将各个汉字转换为id表示
    word_id_list = [None] * len(word_list)
    for i, wl in enumerate(word_list):
        word_id_list[i] = [None] * len(wl)
        for j, w in enumerate(wl):
            word_id_list[i][j] = (word2idx[w])

    viterbi(word_id_list, pinyin_list, len(words), id2word, )

```

## 参考
* [Github 代码](https://github.com/tankle/NLPAlgorithm/blob/master/SpellCorrect/src/main/io/github/tankle/algorithm/DTSpellCorrectFactory.java)
*[HMM学习最佳范例四：隐马尔科夫模型] (http://www.52nlp.cn/hmm-learn-best-practices-four-hidden-markov-models)
