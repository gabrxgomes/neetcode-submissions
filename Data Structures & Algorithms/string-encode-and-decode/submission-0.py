class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            # para cada string, guarda o tamanho + "#" + a string
            # ex: "cat" → "3#cat", "dog" → "3#dog"
            # o "#" é o delimitador entre o tamanho e o conteúdo
            res += str(len(s)) + "#" + s

        # resultado final: "3#cat3#dog" — uma única string codificada
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                          # i aponta para o início do próximo token

        while i < len(s):
            j = i

            # avança j até encontrar o "#"
            # extrai o número que representa o tamanho da próxima string
            while s[j] != '#':
                j += 1

            # s[i:j] é o número antes do "#" — converte para int
            # ex: s = "3#cat", i=0, j=1 → s[0:1] = "3" → length = 3
            length = int(s[i:j])

            # pula o "#" — agora i aponta para o primeiro char da string
            i = j + 1

            # j aponta para o fim da string usando o tamanho extraído
            j = i + length

            # extrai a string original e adiciona ao resultado
            res.append(s[i:j])

            # move i para o início do próximo token
            i = j

        return res