[1402. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/)

A chef has collected data on the `satisfaction` level of his `n` dishes. Chef can cook any dish in 1 unit of time.

**Like-time coefficient** of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. `time[i] * satisfaction[i]`.

Return the maximum sum of **like-time coefficient** that the chef can obtain after dishes preparation.

Dishes can be prepared in **any** order and the chef can discard some dishes to get this maximum value.

**Example 1:**

<pre><code><b>Input:</b> satisfaction = [-1,-8,0,5,-9]
<b>Output:</b> 14
<b>Explanation:</b> After Removing the second and last dish, the maximum total <b>like-time coefficient</b> will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.
</code></pre>

**Example 2:**

<pre><code><b>Input:</b> satisfaction = [4,3,2]
<b>Output:</b> 20
<b>Explanation:</b> Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
</code></pre>

**Example 3:**

<pre><code><b>Input:</b> satisfaction = [-1,-4,-5]
<b>Output:</b> 0
<b>Explanation:</b> People do not like the dishes. No dish is prepared.
</code></pre>

**Constraints:**

- `n == satisfaction.length`
- `1 <= n <= 500`
- `-1000 <= satisfaction[i] <= 1000`
