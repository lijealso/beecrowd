# https://www.beecrowd.com.br/judge/pt/problems/view/2344

# -*- coding: utf-8 -*-

nota = int(input())

if nota == 0:
    print("E")
elif nota >= 1 and nota <= 35:
    print("D")
elif nota >= 36 and nota <= 60:
    print("C")
elif nota >= 62 and nota <= 85:
    print("B")
else:
    print("A")

# https://www.beecrowd.com.br/judge/pt/runs/code/29447903