class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        # FIRST PASS — conta frequência
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # bucket onde índice = frequência
        buckets = [[] for _ in range(len(nums) + 1)] #usamos convensao for _ in quando nao queremos passar nenhum valor na logica do for loop
        for num, count in freq.items():
            buckets[count].append(num)

        # SECOND PASS — coleta os k mais frequentes do maior bucket
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
