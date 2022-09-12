posicao = int(input("Qual a chave?"))
frase = input("Diga uma frase para ser criptografada: ")
lista_frase = list(frase)
new_frase_lista = []
for letra in lista_frase:
    asc2 = ord(letra)
    if asc2 != 32:
        if(asc2 == 121):
            asc2 = 97
        elif(asc2 == 122):
           asc2 = 98
        else: 
            asc2 += posicao
    new_frase_lista.append(chr(asc2).upper())
new_frase = "".join(new_frase_lista)
print("Frase Criptografada: ", new_frase)