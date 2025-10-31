cods = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", 
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", 
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", 
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", 
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", 
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.",  "=": "-...-", 
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}
#normaliza texto para o formato morse
def normalizar(texto: str) -> str:
    s = texto.strip().replace("−", "-").replace("–", "-").replace("—", "-") # s é a string normalizada
    if "∪" not in s:  
        s = s.replace(" ", "∪")
    s = "".join(s.split()).replace("u", "∪").replace("U", "∪")
    while "∪∪" in s: 
        s = s.replace("∪∪", "∪") 
    return "".join(c for c in s if c in ".-∪") # return string com os simbolos ., - e ∪

#conta o n de formas diferentes que um bloco de morse pode ser decodificado
def contModosBloco(bloco: str) -> int:
    por_comprimento = {}#dict q armazena cods por comprimento
    for cod in cods.values(): #percorre os vals do dict cods
        por_comprimento.setdefault(len(cod), []).append(cod)#add o cod ao dict por comprimento
    n, memo = len(bloco), {}#n é o comprimento do bloco e memo é o dict dos indices calculados
    def backtrack(i): 
        if i == n: 
            return 1
        if i in memo:#  return o val armazenado se  o indice foi calculado
            return memo[i] 
        total = 0
        for L in sorted(por_comprimento.keys()):#pecorre comprimentos dos possveis cods 
            if L > n - i:   
                break
            for cod in por_comprimento[L]:# percorre cods possiveis do comprimento L do dict 
                if bloco.startswith(cod, i): #add 1 ao total se o bloco começa com o cod do dict
                    total += backtrack(i + L)  
        memo[i] = total     #se o indice i nao foi calculado, add total ao dict mem
        return total  
    return backtrack(0)   #return total de modos que o bloco pode ser decodificado

#contar o n de mensagens diferentes que podem ser decodificadas
def contMensagens(mensagem: str) -> int:
    s = normalizar(mensagem)# normaliza a mensagem
    if not s:#return 0 se a mensagem n for valida
        return 0
    total = 1 
    for bloco in s.split("∪"):#separação por ∪
        if not bloco or not (total := total * contModosBloco(bloco)):#se o bloco é valido, total=total*contModosBloco(bloco)
            return 0 #return 0 se o  bloco for invalido
    return total # return total de mensagens diferentes que podem ser decodificadas
def main(): 
    mensagem = input().strip()  
    print(contMensagens(mensagem) if mensagem else "Digite uma mensagem em morse!") 

if __name__ == "__main__":
    main()