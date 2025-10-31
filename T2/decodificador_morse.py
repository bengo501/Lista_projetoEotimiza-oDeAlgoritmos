codigos = {
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
#normaliza texto para o formato morse e faz return de string com os simbolos ., - e ∪
def normalizar(texto: str) -> str:
    s = texto.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    if "∪" not in s:  
        s = s.replace(" ", "∪")
    s = "".join(s.split()).replace("u", "∪").replace("U", "∪")
    while "∪∪" in s: 
        s = s.replace("∪∪", "∪") 
    return "".join(c for c in s if c in ".-∪") # return string com os simbolos ., - e ∪
    
#conta o n de formas diferentes que um bloco de morse pode ser decodificado
def contarModosBloco(bloco: str) -> int:
    por_comprimento = {}#dict q armazena codigos por comprimento
    for codigo in codigos.values(): #percorre os vals do dict codigos
        por_comprimento.setdefault(len(codigo), []).append(codigo)#add o codigo ao dict por comprimento
    n, memo = len(bloco), {}#n é o comprimento do bloco, memo é o dict que guarda os indices calculados
    def backtrack(i): 
        if i == n: 
            return 1
        if i in memo:#return o val armazenado se o indice foi calculado
            return memo[i] 
        total = 0
        for L in sorted(por_comprimento.keys()):#pecorre comprimentos dos possveis codigos 
            if L > n - i:   
                break
            for codigo in por_comprimento[L]:# percorre codigos possiveis do comprimento L do dict
                if bloco.startswith(codigo, i): #add 1 ao total se o bloco começa com o codigo do dict
                    total += backtrack(i + L)  
        memo[i] = total#add total ao dict memo se o indice i nao foi calculado
        return total  
    return backtrack(0)   #return total de modos que o bloco pode ser decodificado

#contar o n de mensagens diferentes que podem ser decodificadas
def contarMensagens(mensagem: str) -> int:
    s = normalizar(mensagem) 
    if not s: #return 0 se a mensagem n for valida
        return 0
    total = 1 
    for bloco in s.split("∪"):  #separa blocos por ∪
        if not bloco or not (total := total * contarModosBloco(bloco)):  
            return 0  #return 0 se o bloco for invalido
    return total # return total de mensagens diferentes que podem ser decodificadas

def main(): 
    mensagem = input().strip()  
    print(contarMensagens(mensagem) if mensagem else "Digite uma mensagem em morse!") 

if __name__ == "__main__":
    main()