# LeetCode_Alogrithms 

#  Introduction
***
#### Definition :
```markdown
企業除了用履歷鑑定外，也時常參考面試者的開發能力及作品

而Leetcode便是以蒐集各項面試題目製成的題庫供求職者練習

其類型分別有 : 

● Algorithm 

● Database

● Shell

● Concurrency

而本篇以Alogrithms(演算法)題型為主,紀錄作答Leetcode之程式碼。 


```
#### Content : 
```markdown

● Algorithm : 演算法,用程式去描述其操作或是科學計算邏輯的過程。

可用許多種語言編寫(Java , Python , C++ ...)


```

#  Problems_Alogrithms 
***
#  01.Running Sum Of 1d Array
```markdown

# 1480.
# With Python
# Difficuly : Eazy


Input: nums = [1,2,3,4]

Output: [1,3,6,10]

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]

Output: [1,2,3,4,5]

Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]

Output: [3,4,6,16,17]

---------------------------------------------------------------------------------------

My Solution On underline↓


```

My Solution : [01.RunningSumOf1dArray](https://github.com/Wiwi-Creator/LeetCode_Algorithms/blob/main/RunningSumOf1dArray.py)

#  02. Jewels and Stones
```markdown

# 771.
# With Python
# Difficuly : Eazy

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

● 1 <= jewels.length, stones.length <= 50
● jewels and stones consist of only English letters.
● All the characters of jewels are unique.

---------------------------------------------------------------------------------------

My Solution On underline↓


```

My Solution : [02.JewelsAndStones](https://github.com/Wiwi-Creator/LeetCode_Algorithms/blob/main/JewelsAndStones.py)

#  03. Maximum Ice Cream Bars
```markdown

# 1883.
# With Python
# Difficuly : Medium

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n,
where costs[i] is the price of the ith ice cream bar in coins. 
The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

 

Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

---------------------------------------------------------------------------------------

My Solution On underline↓


```

My Solution :[03.MaximumIceCreamBars](https://github.com/Wiwi-Creator/LeetCode_Algorithms/blob/main/MaximumIceCreamBars.py)

#  04. Maximum 69 Number
```markdown

# 1323.
# With Python
# Difficuly : Eazy

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

---------------------------------------------------------------------------------------

My Solution On underline↓


```

My Solution :[04.Maximum69Number]()

#  05. Palondrome Number
```markdown

# 9.
# With Python
# Difficuly : Eazy

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

---------------------------------------------------------------------------------------

My Solution On underline↓


```

My Solution :[04.PalindromeNumber]()


Get more problems from it : https://leetcode.com/problemset/all/


