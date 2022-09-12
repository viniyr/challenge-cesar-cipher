posicao = int(input("Qual a chave?"))
frase = input("Diga uma frase para ser criptografada: ")
alfabeto = "abcdefghijklmnopqrstuvwxyz" #criei alfabeto em string
frase = frase.lower() #deixei a frase em letra minuscula
new_frase = "" #criei uma string para adicionar a nova frase
for letra in frase:
    if letra != ' ':
        posicao_caractere = alfabeto.index(letra) #acha a posição da letra no alfabeto
        if(posicao_caractere > (25-posicao)):
            posicao_caractere = (posicao-1)-(25-posicao_caractere) #substitui a posicao do caractere considerando a posição da letra em relação à chave
        else:
            posicao_caractere += posicao
        new_frase = new_frase + alfabeto[posicao_caractere] #adiciona a letra criptografada na string
    if letra == ' ':
        new_frase = new_frase + " " #adiciona os espaços
print("Frase Criptografada: ", new_frase)
