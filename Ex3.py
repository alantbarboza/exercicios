"""
    Os algarismos romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M
    Símbolo       total
    I               1
    V               5
    X               10
    L               50
    C               100
    D               500
    M               1000
    
    Por exemplo, 2 é escrito como II em algarismo romano, apenas dois somados. 
    12 é escrito como XII, que é simplesmente X + II. 
    O número 27 é escrito como XXVII, que é XX + V + II
    Os algarismos romanos geralmente são escritos do maior para o menor, da esquerda para a direita. No entanto, o numeral para quatro não é IIII. 
    Em vez disso, o número quatro é escrito como IV. Como um está antes do cinco, subtraímos, resultando em quatro. 
    O mesmo princípio se aplica ao número nove, que é escrito como IX. Existem seis casos em que a subtração é usada
    
    I pode ser colocado antes V (5) e X (10) para fazer 4 e 9. 
    X pode ser colocado antes L (50) e C (100) para fazer 40 e 90. 
    C pode ser colocado antes D (500) e M (1000) para fazer 400 e 900.

    Dado um numeral romano, converta-o em um número inteiro
    Exemplo 1:
    Entrada: s = "III"
    Saída: 3
    Explicação: III = 3

    Exemplo 2:
    Entrada: s = "LVIII"
    Saída: 58
    Explicação: L = 50, V = 5, III = 3.
    
    Exemplo 3:
    Entrada: s = "MCMXCIV"
    Saída: 1994
    Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.
"""
class Solution(object):
    def romanToInt(self, input_romano):
        romano_para_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0

        for idx in range(len(input_romano)):
            if idx < len(input_romano) - 1 and romano_para_decimal[input_romano[idx]] < romano_para_decimal[input_romano[idx + 1]]:
                total -= romano_para_decimal[input_romano[idx]]
            else:
                total += romano_para_decimal[input_romano[idx]]
            
        return total