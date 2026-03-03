'''
Palindrome Number:
Dado um número inteiro x, retornar true se x é um palíndromo, e false de outra forma.

Exemplo 1:

Entrada: x = 121
Saída: verdadeiro
Explicação: 121 é lido como 121 da esquerda para a direita e da direita para a esquerda.
Exemplo 2:

Entrada: x = -121
Saída: falso
Explicação: Da esquerda para a direita, lê-se -121. Da direita para a esquerda, passa a ser 121-. Portanto não é um palíndromo.
Exemplo 3:

Entrada: x = 10
Saída: falso
Explicação: Lê 01 da direita para a esquerda. Portanto não é um palíndromo.
'''

class Solution(object):
    def isPalindrome(self, x):
        str_num = str(x)
        return str_num == str_num[::-1]