# -*- coding: utf-8 -*-
"""2501.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_z1paE3HYv_jOx7FbhXzrDOIYBl3rlc
"""

n, k = map(int, input().split())

# n의 약수 구하기
divisors = []
for i in range(1, n+1):
  if n % i == 0:
    divisors.append(i)

if len(divisors) < k:
  print(0)
else:
  print(divisors[k-1])

