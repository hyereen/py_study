# -*- coding: utf-8 -*-
"""9093.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LDd1JRXMROHP5RAy35ilMkjnKPjP3IQq
"""

# 테스트 개수
t = int(input())
# 각 문장을 뒤집은 이중리스트를 저장하는 리스트
result = []
for tt in range(0, t):
  n = [] # 문장 별 리스트 
  temp = list(input().split())
  for i in temp: # 문장을 단어별로 쪼개서 뒤집어서 저장
    r = reversed(i)
    n.append(list(r))
  result.append(n)

for k in result: # 문장 여러개 중 
  for i in k: # 한 문장을 뽑아서  
    for j in i: # 한 단어를 뽑아서 
      print(j, end='') # 단어를 출력
    print(' ', end='') # 단어 사이에 띄어쓰기
  print() # 문장 사이에 엔터

