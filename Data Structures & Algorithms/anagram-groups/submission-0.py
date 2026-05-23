class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        groups = {}                             # chave: string ordenada → valor: lista de anagramas

        for s in strs:
            key = "".join(sorted(s))            # "cat" → "act", "pots" → "opst"
            if key not in groups:
                groups[key] = []                # primeira vez — cria lista
            groups[key].append(s)               # adiciona palavra ao grupo

        return list(groups.values())            # retorna só os grupos