---
layout: post
title: LintCode 进阶题解 之 Stirng

category: Learning
tags: [LintCode, 解题报告]
description: |
  LintCode 阶梯训练之String 解题报告
---
{% include JB/setup %}



##Two Strings Are Anagrams

Write a method anagram(s,t) to decide if two strings are anagrams or not.

Example
Given s="abcd", t="dcab", return true.

Challenge
O(n) time, O(1) extra space
{% highlight cpp %}
class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        // write your code here
        int m = s.size(), n = t.size();
        if(m != n)
            return false;
        int sum = 0;
        for(int i=0; i<m; i++){
            sum += s[i] - 'a';
            sum -= t[i] - 'a';
        }
        return sum == 0;
    }
};

{% endhighlight %}

##Compare Strings

26% Accepted
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD", B = "AABC", return false.
{% highlight cpp %}
class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true 
     *           else return false
     */
    bool compareStrings(string A, string B) {
        // write your code here
        int m = A.size(), n = B.size();
        
        if(0 == n)
            return true;
        
        if(m < n)
            return false;
            
        vector<int> numa(26,0);
        vector<int> numb(26, 0);
        for(int i=0; i<m; i++)
            numa[A[i] - 'A']++;
        for(int i=0; i<n; i++)
            numb[B[i] - 'A']++;
        
        for(int i=0; i<26; i++)
            if(numa[i] < numb[i])
                return false;
        
        return true;
    }
};


{% endhighlight %}
##strStr

18% Accepted
strstr (a.k.a find sub string), is a useful function in string operation. You task is to implement this function. 

For a given source string and a target string, you should output the "first" index(from 0) of target string in source string.

If target is not exist in source, just return -1.

Example
If source="source" and target="target", return -1.

If source="abcdabcdefg" and target="bcd", return 1.

Challenge
O(n) time.

Clarification
Do I need to implement KMP Algorithm in an interview?
- Not necessary. When this problem occurs in an interview, the interviewer just want to test your basic implementation ability.
{% highlight cpp %}
class Solution {
public:
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    int strStr(const char *source, const char *target) {
        // write your code here
        
        if(source == NULL or target == NULL)
            return -1;
        
        int m = strlen(source), n = strlen(target);
        if(m < n)
            return -1;
        if( m == 0 && n == 0)
            return 0;
        int result = -1;
        for(int i=0; i<m; i++){
            int k = i;
            int j;
            for(j=0; j<n && k < m; ++k, ++j){
                if(source[k] != target[j])
                    break;
            }
            
            if(j >=n ){
                result = i;
                break;
            }
        }
        return result;
    }
};


{% endhighlight %}

##Anagrams

24% Accepted
Given an array of strings, return all groups of strings that are anagrams.

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Note
All inputs will be in lower-case
{% highlight cpp %}
class Solution {
public:
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    vector<string> anagrams(vector<string> &strs) {
        // write your code here
        int m = strs.size();
        vector<string> newstr;
        for(int i=0; i<m; ++i){
            string tmp = strs[i];
            sort(tmp.begin(), tmp.end());
            //cout<<tmp<<endl;
            newstr.push_back(tmp);
        }

        map<string, int> hashstr;
        for(int i=0; i<m; ++i){
            if(hashstr.find(newstr[i]) == hashstr.end())
                hashstr[newstr[i]] = 0;
            hashstr[newstr[i]] += 1;
        }
        vector<string> result;
        for(int i=0; i<m; ++i){
            if(hashstr[newstr[i]] > 1)
                result.push_back(strs[i]);
        }
        return result;
    }
};


{% endhighlight %}
##Longest Common Substring

35% Accepted
Given two strings, find the longest common substring.

Return the length of it.

Example
Given A="ABCD", B="CBCE", return 2.

Note
The characters in substring should occur continuously in original string. This is different with subsequence.

{% highlight cpp %}
class Solution {
public:    
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        // write your code here
        int m = A.size(), n = B.size();
        vector<vector<int>> dp(m, vector<int>(n));
        int result = 0;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(0 == i or 0 == j){
                    dp[i][j] = A[i] == B[j] ? 1:0;
                }
                else{
                    if(A[i] == B[j])
                        dp[i][j] = dp[i-1][j-1] + 1;
                    else
                        dp[i][j] = 0;
                }
                result = max(result, dp[i][j]);
            }
        }
        return result;
    }
};


{% endhighlight %}

##Longest Common Prefix

31% Accepted
Given k strings, find the longest common prefix (LCP).

Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
{% highlight cpp %}
class Solution {
public:    
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    
    string LCP(string one, string two){
        int m = one.size(), n = two.size();
        string prefix = "";
        int len = min(m,n);
        for(int i=0; i<len; i++){
            if(one[i] == two[i])
                prefix += one[i];
            else
                break;
        }
        return prefix;
    }
    string longestCommonPrefix(vector<string> &strs) {
        // write your code here
        int m = strs.size();
        if(m == 0)
            return "";
        if(1 == m)
            return strs[0];
        string comstr = LCP(strs[0], strs[1]);
        for(int i=2; i<m; ++i){
            comstr = LCP(comstr, strs[i]);
        }
        return comstr;
    }
};

{% endhighlight %}

##String to Integer(atoi)

14% Accepted
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Example
"10" => 10

"-1" => -1

"123123123123123" => 2147483647

"1.0" => 1

{% highlight cpp %}
class Solution {
public:
    /**
     * @param str: A string
     * @return An integer
     */
    int atoi(string str) {
        // write your code here
        int result = 0;
        int m = str.size();
        int i = 0;
        while(str[i]== ' ') ++i;
        
        int sign = 1;
        if(str[i] == '-'){
            ++i;
            sign = -1;
        }
        else if(str[i] == '+'){
            ++i;
            sign = 1;
        }
        
        for(; i <m; ++i){
            if(str[i] < '0' || str[i] > '9')
                break;
            if((result > INT_MAX / 10) || 
                    (result == INT_MAX/10 
                    && str[i] - '0' > INT_MAX %10))
                return sign == -1 ? INT_MIN : INT_MAX;
            result = result*10 + str[i] - '0';
        }
        
        return sign == 1 ? result : -1*result;
    }
};

{% endhighlight %}

