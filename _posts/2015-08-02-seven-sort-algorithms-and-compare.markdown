---
layout: post
title: 7大排序算法及其比较

category:  Learning
tags: [数据结构]
description: |
  实现了常见的7大排序算法，并进行了性能的比较。
---


{% include JB/setup %}


##7大排序算法比较

插入排序，希尔排序，选择排序，归并排序，冒泡排序，快速排序，堆排序[^1][^2]

###插入排序
```C++
 /**
     * 插入排序
     * 基本思想：寻找到可以插入的位置
     */
    vector<int> InsertSort(vector<int> result){
        int tmp = 0;
        for(int i=1; i<result.size(); i++){
            int j= i-1;
            tmp = result[i];
            while(j >= 0 && tmp < result[j]){
                result[j+1]= result[j];
                j--;
            }
            result[j+1] = tmp;
        }
        return result;
    }
{% highlight cpp %}
###希尔排序
```C++
    /**
     * 希尔排序
     * 基本思想：
     *  算法先将要排序的一组数按某个增量d（n/2,n为要排序数的个数）分成若干组，
     * 每组中记录的下标相差d.对每组中全部元素进行直接插入排序，
     * 然后再用一个较小的增量（d/2）对它进行分组，在每组中再进行直接插入排序。
     * 当增量减到1时，进行直接插入排序后，排序完成。
     */
    vector<int> ShellSort(vector<int> result){

        int tmp = 0;
        double d1 = result.size();

        while(true){
            d1 = ceil(d1/2);
            int d = (int)d1;
            for(int i=0; i<d; i++){
                //增量为d的插入排序
                for(int j=i+d; j<result.size(); j+=d){
                    int k = j - d;
                    tmp = result[j];
                    while(k >= 0 && result[k] > tmp){
                        result[k+d] = result[k];
                        k = k - d;
                    }
                    result[k+d] = tmp;
                }
            }
            if(d == 1)
                break;
        }
        return result;
    }
{% endhighlight %}
###选择排序
```C++
    /**
     * 选择排序：
     * 基本思想：
     *      在要排序的一组数中，选出最小的一个数与第一个位置的数交换；
     * 然后在剩下的数当中再找最小的与第二个位置的数交换，如此循环到倒数第二个数和最后一个数比较为止。
     */
    vector<int> SelectSort(vector<int> result){
        for(int i=0; i<result.size()-1; i++){
            int k = i;
            for(int j=i+1; j<result.size(); j++){
                if(result[k] > result[j] )
                    k = j;
            }
            if( k != i){
                int tmp = result[k];
                result[k] = result[i];
                result[i] = tmp;
            }
        }
        return result;
    }
{% highlight cpp %}
###堆排序
```C++
    //*************************************************
    //堆排序
    /**
     * 重新构建堆，使之符合堆的规则
     */
    void __fixdwon(vector<int>& arr,int root, int lastIndex){
        int i = root;
        int tmp = arr[root];
        int j = 2*i + 1;
        while(j < lastIndex){

            if(j + 1 < lastIndex && arr[j+1] > arr[j])
                j++;
            //找到比根节点小的值
            if(arr[j] <= tmp)
                break;
            //移动到父节点
            arr[i] = arr[j];
            i = j;
            j = 2*i + 1;
        }
        arr[i] = tmp;
    }

    //建堆
    void  __buildMaxHeap(vector<int>& arr, int lastindex){
        for(int i=lastindex/2-1; i>=0; i--){
            this->__fixdwon(arr, i, lastindex);
        }
    }
    /**
     * 堆排序
     *
     */
    vector<int> HeapSort(vector<int> arr){
        this->__buildMaxHeap(arr, arr.size());
        for(int i=arr.size()-1; i>=0; i--){
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
            this->__fixdwon(arr, 0, i);
        }
        return arr;
    }
{% endhighlight %}
###冒泡排序
```C++
    /**
     *  冒泡排序
     *  相邻比较
     */
    vector<int> BubbleSort(vector<int> arr){
        for(int i=0; i<arr.size(); i++){
            for(int j=1; j<arr.size()-i; j++){
                if(arr[j] < arr[j-1]){
                    int tmp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = tmp;
                }
            }
        }
        return arr;
    }
{% highlight cpp %}
###冒泡排序优化
```C++
    /**
     * 冒泡排序算法的优化1
     *
     * 设置一个标志flag，当某一趟完全没有进行交换，就不需要进行下一轮的排序
     */
    vector<int> BubbleSort1(vector<int> arr){
        bool flag = true;
        int k = arr.size();
        while(flag && k >0 ) {
            flag = false;
            for (int i = 1; i < k; i++) {
                if (arr[i] < arr[i - 1]) {
                    swap(arr[i], arr[i - 1]);
                    flag = true;
                }
            }
            k--;
        }
        return arr;
    }

{% endhighlight %}
###快速排序
```C++
    /**
     * 快速排序
     */
    /**
     * 切分函数，以第一个作为枢纽
     */
    int __partition(vector<int>& arr, int first, int last){
        int key = arr[first];
        while(first < last){
            while(first < last && arr[last] >= key){
                last--;
            }
            arr[first] = arr[last];
            while(first < last && arr[first] <= key){
                first++;
            }
            arr[last] = arr[first];

        }
        arr[first] = key;
        return first;
    }
    /**
     * 递归排序
     */
    void __quickSort(vector<int>& arr, int start, int end){
        if(start < end){
            int middle = this->__partition(arr, start, end);
            __quickSort(arr, start, middle-1);
            __quickSort(arr, middle+1, end);
        }
    }

    vector<int> QuickSort(vector<int> arr){
        __quickSort(arr,0, arr.size()-1);
        return arr;
    }
{% highlight cpp %}
###归并排序
```C++
/////////////////////////////////////////////////////////////////////
    /**
     * 归并排序
     */
    void __merge(vector<int>&arr, int start, int mid, int end){
        vector<int> tmp;
        int left = start;
        int right = mid + 1;
        while(left <= mid && right <= end){
            if(arr[left] < arr[right])
                tmp.push_back(arr[left++]);
            else
                tmp.push_back(arr[right++]);
        }
        while(left <= mid){
            tmp.push_back(arr[left++]);
        }
        while(right <= end){
            tmp.push_back(arr[right++]);
        }
        for(int i=start; i<=end; i++){
            arr[i] = tmp[i-start];
        }
    }
    void __sort(vector<int>& arr, int start, int end){
        if(start < end){
            int mid = (start + end)/2;
            __sort(arr, start, mid);
            __sort(arr, mid+1, end);
            __merge(arr, start, mid, end);
        }

    }
    vector<int> MergeSort(vector<int> arr){
        __sort(arr, 0, arr.size()-1);
        return arr;
    }


{% endhighlight %}
程序中有些地方写了this，是因为原始代码是写在一个类中，具体可以查看我的Github参考[代码实现](https://github.com/tankle/offer/tree/master/DataStructure/sort)，其中还有效率比较代码。

###效率比较

时间性能比较（毫秒）

|数组大小 |	10000	|100000|	1000000|
| --------   | -----:  | :----:  |
|InsertSort	|210	|20727|	2038491|
|ShellSort	|3	|46	|747|
|SelectSort	|372	|37885|	3742262
|HeapSort	|0	|31	|449|
|QuickSort	|15	|15	|265|
|BubbleSort	|854	|80354  |	7977907
|MergeSort	|15	|141	|1435|
|Sort（c++内置排序）	|0	|31	|265|

可以看到随着待排序数组的增大，快速排序等算法的优势就越明显。

###参考博客：
[^1]: http://blog.csdn.net/morewindows/article/details/7961256

[^2]: http://blog.csdn.net/qy1387/article/details/7752973





