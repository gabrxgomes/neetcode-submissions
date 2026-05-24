class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #a ideia principal é, qual a quantidade length de numeros que PODEM
        #formar uma ordem consecutiva n + 1 ou n - 1 dependendo da ideia.

        # edge case: array vazio — nenhuma sequência possível
        if not nums: return 0

        # converte para set — remove duplicatas e permite lookup O(1)
        # [2,20,4,10,3,4,5] → {2,3,4,5,10,20}
        num_set = set(nums)

        # guarda o maior length encontrado até agora
        best = 0

        # percorre cada número do set
        for n in num_set:

            # verifica se n é o INÍCIO de uma sequência
            # se n-1 existe no set, alguém já vai contar essa sequência
            # ex: n=3 → 2 existe → 3 não é início, pula
            # ex: n=2 → 1 não existe → 2 É o início, entra
            if n - 1 not in num_set:

                # começa a contar a partir do próprio n
                length = 1

                # enquanto o próximo número da sequência existir no set
                # n=2: verifica 2+1=3, 2+2=4, 2+3=5, 2+4=6(não existe) → para
                while n + length in num_set:
                    length += 1         # encontrou o próximo → incrementa

                # atualiza o melhor resultado se essa sequência for maior
                best = max(best, length)

        # retorna o comprimento da maior sequência encontrada
        return best