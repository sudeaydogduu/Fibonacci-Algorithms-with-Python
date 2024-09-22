# Fibonacci Algorithms with Python
 Fibonacci Algorithms (Recursive, Recursive-Memo, Iterative) with Python
This Python program calculates Fibonacci numbers using three different methods: recursive, recursive memoization, and iterative. Each approach has its advantages and disadvantages; while the recursive method is simple and easy to understand, it can have poor performance due to redundant calculations. The memoization method significantly speeds up the computation by storing previously computed values, while the iterative method offers better memory efficiency.

Description
The program computes Fibonacci numbers using three different approaches:

Recursive Method:

The Fibonacci function is defined simply, where the nth Fibonacci number is computed as the sum of the (n-1)th and (n-2)th Fibonacci numbers. This method works well for small values of n but suffers from performance issues for larger n due to many overlapping subproblems.

Time Complexity : 𝑂(2^𝑛) 
Space Complexity : 𝑂(𝑛)


Recursive Memoization:
This approach uses a dictionary to store previously computed Fibonacci numbers. By caching results, it avoids redundant calculations of the same Fibonacci number multiple times, significantly improving performance.

Time Complexity :  𝑂(𝑛)
Space Complexity: 
𝑂(𝑛)


Iterative Method:
This method calculates Fibonacci numbers using a loop. It stores the last two Fibonacci numbers and computes the next one in each iteration. It is memory-efficient.

Time Complexity : 𝑂(𝑛)
Space Complexity : 𝑂(1)
