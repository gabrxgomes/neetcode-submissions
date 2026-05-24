class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # FIRST PASS — prefix: produto acumulado da esquerda
        prefix = 1
        for i in range(n):
            output[i] = prefix        # guarda produto de tudo à esquerda
            prefix *= nums[i]         # atualiza para próxima posição

        # SECOND PASS — suffix: multiplica pelo produto acumulado da direita
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix       # multiplica pelo produto de tudo à direita
            suffix *= nums[i]         # atualiza para próxima posição

        return output