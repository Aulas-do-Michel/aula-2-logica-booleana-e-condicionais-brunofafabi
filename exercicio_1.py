"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
  print('O número {} é PAR'.format(número))
else:
  print('O número {} é ÍMPAR'.format(número))
