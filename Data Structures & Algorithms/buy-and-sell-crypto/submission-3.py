class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        l = 0           # ponteiro de compra — sempre o menor preço visto
        best = 0        # melhor lucro

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:           # dá lucro — calcula
                best = max(best, prices[r] - prices[l])
            else:                               # preço caiu — move compra
                l = r

        return best