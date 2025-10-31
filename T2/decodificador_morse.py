codigos = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}

def normalizar(texto: str) -> str:
    s = texto.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    if "∪" not in s:
        s = s.replace(" ", "∪")
    s = "".join(s.split()).replace("u", "∪").replace("U", "∪")
    while "∪∪" in s:
        s = s.replace("∪∪", "∪")
    return "".join(ch for ch in s if ch in ".-∪")

def contar_modos_bloco(bloco: str) -> int:
    por_comprimento = {}
    for codigo in codigos.values():
        por_comprimento.setdefault(len(codigo), []).append(codigo)
    comprimentos = sorted(por_comprimento.keys())
    n, memo = len(bloco), {}
    
    def backtrack(i):
        if i == n:
            return 1
        if i in memo:
            return memo[i]
        total = 0
        for L in comprimentos:
            if L > n - i:
                break
            for codigo in por_comprimento[L]:
                if bloco.startswith(codigo, i):
                    total += backtrack(i + L)
        memo[i] = total
        return total
    return backtrack(0)

def contar_mensagens(mensagem: str) -> int:
    s = normalizar(mensagem)
    if not s:
        return 0
    blocos = s.split("∪")
    total = 1
    for bloco in blocos:
        if not bloco or not (total := total * contar_modos_bloco(bloco)):
            return 0
    return total

def main():
    mensagem = input().strip()
    print(contar_mensagens(mensagem) if mensagem else "forneca a mensagem em morse")

if __name__ == "__main__":
    main()