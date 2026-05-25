class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0                         # edge case: string vazia

        seen = {}                                  # char → último índice visto
        l = 0                                      # ponteiro esquerdo da janela
        best = 0                                   # maior comprimento encontrado

        for i, char in enumerate(s):               # i = índice, char = valor
            if char in seen and seen[char] >= l:   # repetição dentro da janela
                l = seen[char] + 1                 # move janela para depois da repetição
            seen[char] = i                         # atualiza último índice do char
            best = max(best, i - l + 1)            # i - l + 1 = tamanho da janela

        return best