# -*- coding: utf-8 -*-
"""5014.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15vsEUP0-FuKAXQVgrCO1jHd0COFPsHgD
"""

# 5014
# https://www.acmicpc.net/problem/5014

from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs():
  queue = deque()
  queue.append(S)
  cnt[S]= 1 # 방문처리 꼭 해주기

  while queue:
    now = queue.popleft()
    
    if now == G:
      print(cnt[now] - 1)
      return

    for nx in (now+U, now-D):
      if 0 < nx <= F and cnt[nx] == 0:
        cnt[nx] = cnt[now] + 1
        queue.append(nx)
  print("use the stairs")

cnt = [0] * (F+1)


bfs()