---
layout: post
title:  LintCode 阶梯训练之 Integer Array

category: Learning
tags: [LintCode, 解题报告]
description: |
  LintCode 阶梯训练之Integer Array 解题报告
---
{% include JB/setup %}



##Remove Element

39% Accepted
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
{% highlight cpp %}
class Solution {
public:
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        int result = 0;
        int i=0;
        while(i < A.size()){
            if(A[i] == elem)
                A.erase(A.begin()+i);
            else{
                i++;
                result++;
            }
        }
        return result;
    }
};

{% endhighlight %}

##Subarray Sum

18% Accepted
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Note
There is at least one subarray that it's sum equals to zero.
{% highlight cpp %}
//O(n^2)解法
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        // write your code here
        vector<int> result;
        for(int i=0; i<nums.size(); ++i){
            int sum = nums[i];
            if(sum == 0){
                result.push_back(i);
                result.push_back(i);
                break;
            }
            for(int j=i+1; j<nums.size(); ++j){
                sum += nums[j];
                if(sum == 0){
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
    }
};

//O(nlogn)解法
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        vector<int> result;
        if(nums.empty())
            return result;
        vector<pair<int,int>> sum(nums.size()+1,make_pair(0,0));
        for(int i=0; i<nums.size(); i++){
            sum[i+1].first =  sum[i].first + nums[i];
            sum[i+1].second = i + 1;
        }

        sort(sum.begin(), sum.end());
        
        for(int i=1; i<sum.size(); i++){
            if(sum[i].first == sum[i-1].first){
                //需要注意这里的下标，因为上面是从1开始的
                result.push_back(sum[i-1].second );
                result.push_back(sum[i].second -1);
                return result;
            }
        }
        return result;
    }
};


{% endhighlight %}

##Remove Duplicates from Sorted Array

33% Accepted
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

{% highlight cpp %}
class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        // write your code here
        int i=1;
        while(i<nums.size()){
            if(nums[i] != nums[i-1])
                ++i;
            else
                nums.erase(nums.begin()+i);
        }
        return nums.size();
    }
};
{% endhighlight %}

##Merge Sorted Array

41% Accepted
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

Note
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

{% highlight cpp %}
class Solution {
public:
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    void mergeSortedArray(int A[], int m, int B[], int n) {
        // write your code here
        int i=m-1, j=n-1;
        int k=m+n-1;
        while(k >= 0){
            if(A[i] >= B[j]){
                A[k] = A[i];
                i--;
            }else{
                A[k] = B[j];
                j--;
            }
            k--;
        }
    }
};

{% endhighlight %}

##Product of Array Exclude Itself

25% Accepted
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A=[1, 2, 3], return [6, 3, 2].

{% highlight cpp %}
class Solution {
public:
    /**
     * @param A: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    vector<long long> productExcludeItself(vector<int> &nums) {
        // write your code here
        int m = nums.size();
        vector<long long> left(m);
        vector<long long> right(m);
        long long tmp = 1;
        for(int i=0; i< m; ++i){
            left[i] = tmp;
            tmp *= nums[i];
        }
        tmp = 1;
        for(int i = m-1; i >= 0; i--){
            right[i] = tmp;
            tmp *= nums[i];
        }
        vector<long long> result(m);
        for(int i=0; i< m; ++i){
            result[i] = left[i] * right[i];
        }
        return result;
    }
};

{% endhighlight %}

##First Missing Positive

23% Accepted
Given an unsorted integer array, find the first missing positive integer.

Example
Given [1,2,0] return 3, and [3,4,-1,1] return 2.

Challenge
Your algorithm should run in O(n) time and uses constant space.

{% highlight cpp %}
class Solution {
public:
    /**    
     * @param A: a vector of integers
     * @return: an integer
     */
    int firstMissingPositive(vector<int> A) {
        // write your code here
        //利用数组的下标作为hash，每个对应的下标对应相应的值
        //然后循环，找到最小的那个值和下标不对应的地方即为答案
        int m = A.size();
        int i = 0;
        while(i < m){
            if(A[i] > 0 && A[i] <= m && A[i] != i+1 && A[i] != A[A[i]-1])
                    swap(A[i], A[A[i]-1]);
            else
                i++;
        }
        for(i=0; i<m; i++){
            if(A[i] != i+1)
                return i+1;
        }
        return m+1;
    }
};

{% endhighlight %}

##2 Sum

26% Accepted
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example
numbers=[2, 7, 11, 15], target=9

return [1, 2]

Note
You may assume that each input would have exactly one solution

Challenge
Either of the following solutions are acceptable:

O(1) Space, O(nlogn) Time
O(n) Space, O(n) Time

{% highlight cpp %}
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        unordered_map<int ,int> res;
        vector<int> idx;
        for(int i=0; i<nums.size(); ++i){
            int left = target - nums[i];
            if(res.find(left) == res.end()){
                res[nums[i]] = i;
            }
            else{
                idx.push_back(res[left]+1);
                idx.push_back(i+1);
                break;
            }
        }
        return idx;
    }
};


{% endhighlight %}

##3 Sum

18% Accepted
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

{% highlight cpp %}
class Solution {
public:    
    void twoSum(vector<int> &nums,int begin, int target, vector<vector<int>>& result) {
        //使用set集合来添加元素，因为target是固定的，这样就不会有重复的结果
        //使用双指针，前后夹逼
        int start = begin;
        int end = nums.size()-1;
        set<pair<int,int>> two;
        while (start < end){
            if(nums[start] + nums[end] == target){
//                result.push_back({target, nums[start], nums[end]});
                two.insert(make_pair(nums[start], nums[end]));
                start++;
                end--;
            }
            else if(nums[start] + nums[end] > target)
                end--;
            else
                start++;
        }
        //这里注意target 需要变换一下
        for(auto it = two.begin(); it != two.end(); ++it){
            result.push_back({0 - target, (*it).first, (*it).second});
        }
    }
    
    //首先对结果进行排序，对于重复的target只需要计算一次，避免重复
    vector<vector<int> > threeSum(vector<int> &nums) {
        // write your code here
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int m = nums.size();
        for(int i=0; i<m; ++i){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int target = 0 - nums[i];
            twoSum(nums, i+1, target, res);
        }
        return res;
    }
};

{% endhighlight %}

##3 Sum Closest 

30% Accepted
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Example
For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Note
You may assume that each input would have exactly one solution.

Challenge
O(n^2) time, O(1) extra space
{% highlight cpp %}
class Solution {
public:    
     /**
     * 找到与target最接近的两个数之和
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    int twoSum(vector<int> &nums,int begin, int target) {
        int result = 0;
        int start = begin;
        int end = nums.size()-1;
        int min_gap = INT_MAX;
        while (start < end){
            int gap = abs(nums[start] + nums[end] - target);
            if(gap < min_gap){
                result = nums[start] + nums[end];
                min_gap = gap;
            }
            if(nums[start] + nums[end] - target > 0)
                end--;
            else
                start++;
        }
        return result;
    }

    /**
     * @param numbers: Give an array numbers of n integer
     * @param target: An integer
     * @return: return the sum of the three integers, the sum closest target.
     */
    int threeSumClosest(vector<int> nums, int target) {
        // write your code here
        //先排序
        sort(nums.begin(), nums.end());
        int m = nums.size();
        int min_gap = INT_MAX;
        int result;
        //记录最小间隔
        for(int i=0; i<m-2; ++i){
            int tmp = target - nums[i];
            int res = twoSum(nums, i+1, tmp);
            if(abs(tmp - res) < min_gap){
                min_gap = abs(tmp - res);
                result = res + nums[i];
            }
        }
        return result;
    }
};


{% endhighlight %}

##4 Sum

18% Accepted
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Example
For example, given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:

(-1, 0, 0, 1)

(-2, -1, 1, 2)

(-2, 0, 0, 2)

Note
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)

The solution set must not contain duplicate quadruplets.
{% highlight cpp %}
class Solution {
public:
    void twoSum(vector<int> &nums,int begin, int target, vector<vector<int>>& result) {
        int start = begin;
        int end = nums.size()-1;
        set<pair<int,int>> two;
        while (start < end){
            if(nums[start] + nums[end] == target){
//                result.push_back({target, nums[start], nums[end]});
                two.insert(make_pair(nums[start], nums[end]));
                start++;
                end--;
            }
            else if(nums[start] + nums[end] > target)
                end--;
            else
                start++;
        }
        //因为是从begin后开始循环的
        for(auto it = two.begin(); it != two.end(); ++it){
            result.push_back({nums[begin-1], (*it).first, (*it).second});
        }
    }

    vector<vector<int> > threeSum(vector<int> &nums, int begin, int target) {
        // write your code here
        vector<vector<int>> res;
        int m = nums.size();
        for(int i=begin; i<m; ++i){
            if(i > begin && nums[i] == nums[i-1]) continue;
            int tmp = target - nums[i];
            twoSum(nums, i+1, tmp, res);
        }
        return res;
    }
    //调用3Sum程序
    vector<vector<int> > fourSum(vector<int> &nums, int target) {
        // write your code here
        int m = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i=0; i<m-3; i++){
            //避免重复
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int targ = target - nums[i];
            vector<vector<int>> res = threeSum(nums, i+1, targ);
            for(int j=0; j<res.size(); j++){
                res[j].insert(res[j].begin(), nums[i]);
                result.push_back(res[j]);
            }
        }
        return result;
    }
};
{% endhighlight %}

##Partition Array

24% Accepted
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
If nums=[3,2,2,1] and k=2, a valid answer is 1.

Note
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Challenge
Can you partition the array in-place and in O(n)?

{% highlight cpp %}
class Solution {
public:
    int partitionArray(vector<int> &nums, int k) {
    // write your code here
        if(nums.size() == 0)
            return 0;
        int start = 0;
        int end = nums.size()-1;
        while(start < end) {
            //寻找左边
            while(start < nums.size() && nums[start] < k)
                start++;
            while(end >=0 && nums[end] >= k)
                end--;
            //退出条件
            if(start >= end) break;
            else {
                int tmp = nums[start];
                nums[start] = nums[end];
                nums[end] = tmp;
                start++;
                end--;
            }
        }
        return start;
    }
};

{% endhighlight %}
##Remove Duplicates from Sorted Array II

29% Accepted
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
{% highlight cpp %}
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
          // write your code here
        if(nums.size() == 0)
            return 0;
        //设置一个重复次数的变量
        int idx = 0;
        int occur = 1;
        for(int i=1; i<nums.size(); i++){
            if(nums[i] == nums[idx]){
                //两次就继续，不需要添加
                if(occur == 2)
                    continue;
                occur++;
            }
            else{
                occur = 1;
            }
            nums[++idx] = nums[i];
        }
        //需要对数组大小进行变换
        nums.resize(idx+1);
        return nums.size();
    }
};
{% endhighlight %}

##Merge Sorted Array II 

32% Accepted
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
{% highlight cpp %}
class Solution {
public:
    /**
    * 对于Challenge问题没有进行优化，思路可以是对大的数组进行二分查找，找到插入的位置
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        // write your code here
        int m = A.size();
        int n = B.size();
        int l = m + n;
        vector<int> C(l);
        int i = 0, j = 0;
        int k = 0;
        while(i < m && j < n){
            if(A[i] <= B[j])
                C[k++] = A[i++];
            else
                C[k++] = B[j++];
        }
        while(i<m)
            C[k++] = A[i++];
        while(j<n)
            C[k++] = B[j++];
        return C;
    }
};

{% endhighlight %}

##Subarray Sum Closest

16% Accepted
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]

Challenge
O(nlogn) time
{% highlight cpp %}
//考察数组前缀和
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    vector<int> subarraySumClosest(vector<int> nums){
        vector<int> result;
        if(nums.empty())
            return result;
        vector<pair<int,int>> sum(nums.size()+1,make_pair(0,0));
        for(int i=0; i<nums.size(); i++){
            sum[i+1].first =  sum[i].first + nums[i];
            sum[i+1].second = i + 1;
        }

        sort(sum.begin(), sum.end());

        int min_gap = INT_MAX;
        int closed_idx = 1;
        for(int i=1; i < sum.size(); i++){
            int gap = sum[i].first - sum[i-1].first;
            if(min_gap > gap){
                min_gap = gap;
                closed_idx = i;
            }
        }
        //用来确保左值必须小于右值
        int left = min(sum[closed_idx].second, sum[closed_idx-1].second);
        int right = -1 + max(sum[closed_idx].second, sum[closed_idx-1].second);
        result.push_back(left);
        result.push_back(right);
        return result;
        
    }
};


{% endhighlight %}
