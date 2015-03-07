---
layout: post
title: "机器学习技法课之Aggregation模型"
category: learning
tags: [机器学习]
description: |
  Courses上台湾大学林轩田老师的机器学习技法课之Aggregation 模型学习笔记。
---

{% include JB/setup %}



##混合（blending）
本笔记是Course上台湾大学林轩田老师的《机器学习技法课》的学习笔记，用于学习之后的一些总结。

首先，对于Aggregation模型，其基本思想就是使用不同的$g_t$来合成最后的预测模型$G_t$。
对于合成的方式主要有四种：
<table>
    <tr><td>方法</td><td>数学描述</td></tr>
    <tr><td>1. 选择。选择最值得可信的$g_t$来当做最终的模型，而这个$g_t$可以使用validation set 来进行选择</td><td>$G(x)=argmin_{t\in\{1,2...T\}}E_{val} (g_t)$</td></tr>
    </tr><td>2. 均一式(uniform)混合(blending)。使用每个$g_t$一票的方式来决定最终的$G_t$</td><td>$G(x)=sign(\sum_{t=1}^T 1\cdot g_t(x))$</td></tr>
    </tr><td>3. 非均一式(non-uniform)混合。对于不同的$g_t$给予不同的权重。该方法包含了上述两种方法，a. 当$\alpha_t=1$时，是uniform混合，b. $E_{val}(g(t))$最小的$g_t$的$\alpha_t$为1，其他都是0，这就是选择方法</td><td>$G(x)=sign(\sum_{t=1}^T \alpha_t g_t(x)),\alpha_t \ge 0$</td></tr>
    </tr><td>4. 条件是混合。在不同的条件下选择不同的$g_t$,该方法包含了non-uniform方法，当$q_t(x)=\alpha_t$时</td><td>$G(x)=sign(\sum_{t=1}^T q_t(x)\cdot g_t(x)),q_t(x) \ge 0$</td></tr>
</table>


###选择
该方法的
优点：简单，流行
缺点：依赖一个很强的假设

在该方法中，$g_t$是使用validation set来进行选择的，选择的标准是$g_t$在验证集上的错误率$E_{val}(g_t)$最低，但如果使用$E_{in}(g_t)$来代替$E_{val}(g_t)$，则需要一个很强的假设来保证会有一个很小的$E_{val}(g_t)$以及$E_{out}(g_t)$

###均一式混合(uniform blending)
此方法最好是能够有不同的$g_t$,这样能从多方面的刻画数据，使得结果更加符合明主的方式，让小数服从多数。

该方法不仅适用于2分类，也适用于多分类，还适合回归问题。
对于回归问题：$G(x) =\frac1T \sum_{t=1}^T g_t(x) $

uniform blending还有一个优点是，使用blending的方式产生的结果，比将每个单独的$g_t$的结果加起来再取平均的结果还好。

下面是理论分析：
![blending](/res/images/blending-01.png)

上述理论表明，使用投票的方法产生的误差要比使用单独的$g_t$的结果之和再平均产生的误差要小。

###非均一式混合(non-uniform blending) 或者 线性混合（linear blending)
![linearblending](/res/images/linearblending.png)

其中对于$\alpha_t $的限制是可以不需要的，因为当$\alpha \lt 0$时，相当于对$g_t$ 进行取反而已。

###条件式混合
![anyblending](/res/images/anyblending.png)


##learning（学习）
在Aggregation模型中，除了blending（混合）之外，还有一种思想，就是在混合的过程中，同时进行$g_t$的生成，这种思想就是learning。混合的思想是，所有的$g_t$都是已知的，重点在于每个$g_t$的参数以及$g_t$是怎么产生的。

在learning的模型中，最关键也在$g_t$的多样性，多样性可以从以下几个方面来获得：

1. 使用不同的模型来产生$g_t$，比如SVM，NB等
2. 同一个模型，使用不同的参数
3. 有些算法本身就具有随机性，比如PLA使用不同的随机种子
4. 使用不同的训练数据来获得模型，可以对数据进行采样获得多份不同的数据

混合和学习三种不同集成方式下的对照表
<table>
    <tr>
        <td>集成方式</td>
        <td>blending（混合）</td>
        <td>learning（学习）</td>
    </tr>
    <tr>
        <td>均一方式（uniform）</td>
        <td>voting（投票）/averaging</td>
        <td>Bagging</td>
    </tr>
        <tr>
        <td>非均一方式（non-uniform）</td>
        <td>linear blending</td>
        <td>AdaBoost</td>
    </tr>
        <tr>
        <td>条件式(conditional)</td>
        <td>Stacking(Any blending)</td>
        <td>Decision Tree</td>
    </tr>
</table>


###Bagging
![bagging](/res/images/bagging.png)

由上面可知，当bagging模型中的基本算法对数据的随机性敏感的话，该算法会比较有效。

###AdaBoost
AdaBoost的基本思想是对每个样本赋予不同的权重，来产生一个$g_t$,整个算法会有T轮迭代，每一轮迭代产生的$g_t$是根据上一轮的$g_{t-1}$来获得的。在迭代过程中，会增大分类错误样本的权重，降低分类正确的样本的权重。

算法流程：
![AdaBoost](/res/images/adaboost.png)

具体过程可以参考这篇博文：[AdaBoost算法的原理与推导](http://blog.csdn.net/v_july_v/article/details/40718799)

###Decision Tree
决策树的优缺点：
![decisionTree](/res/images/decisiontree-01.png)

决策树的基本流程：
![DecisionTreeAlgorithm](/res/images/decisiontree-02.png)

其中有四个关键点。
1. 分支的个数（C）
2. 产生分支的条件
3. 算法终止条件
4. 基本假设

对于上述4个关键点，CART（Classification and Regression Tree）使用了独特参数。
1. C = 2， 产生的树是一个二叉树
2. 对于产生分支的条件，使用了数据的纯洁度来进行度量
![CART](/res/images/decisiontree-03.png)
3. 算法的终止条件是：
    a. 所有 $y_n$是一样的: $ impurity = 0 \Rightarrow   g_t(x) = y_n$
    b. 所有的 $x_n$ 是一样的: 没有决策桩，既无法产生决策点
4. 基本假设是：
$g_t (x) = E_{in} - optimal constant$
    a. binary/multiclass classification (0/1 error): majority of {$y_n$}
    b. regression (squared error): average of {$y_n$}

算法基本流程：
![CARTAlgorithm](/res/images/cart-01.png)

按照上述算法生成的是一颗满二叉树，这样的结果是会造成overfit，因此需要进行剪枝。


CART的优点是：
1. 适用于类别标签数据
2. 对一些有缺失的数据也能够起作用
3. 是具有可解释性的
4. 支持多标签数据
5. 分类的过程非常高效

上面这些优点也是其他算法很难同时具备的，除了其他的一些决策树算法。

##Aggregation of Aggregation
将上述各个算法进行进一步融合，便得到了更加复杂的算法。

比如：Random Forest, Gradient Boosted Decision Tree

###Random Forest

基本算法流程：
![randomforest](/res/images/randomforest.png)

在这讲中还讲到了几个概念：
1. OOB，就是在boost的过程中，需要对数据进行采样，这样就会造成有些数据一直没有被采样过。
2. Feature Selection（特征选择），在RF中，使用的是一种叫排列测试来进行特征选择

上述两点都是RF的优点，在训练过程中不需要额外的validation set，使用OOB既可以进行自我检验；在训练过程中还可以进行特征选择，能选出那些重要的特征。

###Gradient Boosted Decision Tree

这一节还没怎么听懂。

先贴一个算法流程：
![GBDT](/res/images/gbdt.png)


对于整个Aggregation Models的总结
![summary-01](/res/images/summary-01.png)
![summary-02](/res/images/summary-02.png)
![summary-03](/res/images/summary-03.png)