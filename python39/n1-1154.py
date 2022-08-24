# https://www.beecrowd.com.br/judge/pt/problems/view/1154

# -*- coding: utf-8 -*-

lista =[]
soma = 0

while True:
    nota = int(input())
    if nota < 0:
        break
    else:
        lista.append(nota)

for number in lista:
    soma += number

media = (soma / len(lista))

output = "{:.2f}".format(media)

print(output)

# https://www.beecrowd.com.br/judge/pt/runs/code/29448528