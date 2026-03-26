"""
Longest Common Prefix:
Escreva uma função para encontrar a string de prefixo comum mais longa entre uma matriz de strings.
Se não houver um prefixo comum, retorne uma string vazia "".

Exemplo:

Entrada: lista = ["flower","flow","flight"]
Saída: "fl"
"""
class Solution(object):
    def longestCommonPrefix(self, lista):
        retorno = ""

        for c in range(len(lista[0])):
            for s in range(1, len(lista)):
                if c >= len(lista[s]) or lista[0][c] != lista[s][c]:
                    return retorno
            
            retorno += lista[0][c]
        
        return retorno
