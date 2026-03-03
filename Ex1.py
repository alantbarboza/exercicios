'''
Two Sum:
Dada uma matriz de inteiros nums e um número inteiro target, retornar índices dos dois números de modo que somem target.

Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

Exemplo 1:
:type nums: List[int]
:type target: int
:rtype: List[int]

Entrada: nums = [2,7,11,15], alvo = 9
Saída: [0,1]
Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result
    
