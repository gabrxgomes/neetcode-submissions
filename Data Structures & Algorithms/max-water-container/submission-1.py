class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: return 0

        l, r = 0, len(heights) - 1   # ponteiros nas extremidades
        best = 0                      # melhor área encontrada

        while l < r:
            # altura limitada pela menor parede
            # largura = distância entre os ponteiros
            area = min(heights[l], heights[r]) * (r - l)
            best = max(best, area)    # atualiza se for maior

            if heights[l] <= heights[r]:
                l += 1                # parede esquerda menor → move para direita
            else:
                r -= 1                # parede direita menor → move para esquerda

        return best