from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random
import re

tags_metadata = [
    {
        "name": "getCifra",
        "description": "Will encrypt a message from Dogs API",
    },
    {
        "name": "resolveCifra",
        "description": "Decrypt a message by passing the key and the message.",
    },
]


app = FastAPI(openapi_tags=tags_metadata)


class payloadEsperadoParaDescriptografia(BaseModel):
    frase_criptografada: str
    chave_descriptografia: int


class responseModelForResolve(BaseModel):
    decripted_message: str


@app.get("/getCifra", tags=["getCifra"], response_model=payloadEsperadoParaDescriptografia)
def getCifra():

    posicao = random.randrange(1, 25)

    responseFromDogApi = getMessageFromDogApi()

    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # criei alfabeto em string
    # deixei a frase em letra minuscula
    frase = responseFromDogApi["facts"][0].lower().replace(',', '')

    validacaoSeTemNumero = re.findall(r'\d+', frase)
    if(len(validacaoSeTemNumero) > 0):
        return getCifra()

    new_frase = ""  # criei uma string para adicionar a nova frase

    for letra in frase:
        if letra in alfabeto:
            # acha a posição da letra no alfabeto
            posicao_caractere = alfabeto.index(letra)
            if(posicao_caractere > (25-posicao)):
                # substitui a posicao do caractere considerando a posição da letra em relação à chave
                posicao_caractere = (posicao-1)-(25-posicao_caractere)
            else:
                posicao_caractere += posicao
            # adiciona a letra criptografada na string
            new_frase = new_frase + alfabeto[posicao_caractere]
        if letra == ' ':
            new_frase = new_frase + " "  # adiciona os espaços

    payload = {
        "frase_criptografada": new_frase,
        "chave_descriptografia": posicao
    }

    return payload


@app.post('/resolveCifra',  tags=["resolveCifra"], response_model=responseModelForResolve)
def resolveCifra(payloadEsperado: payloadEsperadoParaDescriptografia):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    frase_criptografada = payloadEsperado.frase_criptografada
    chave = payloadEsperado.chave_descriptografia

    mensagem_decriptografada = ""

    for letra in frase_criptografada:

        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao - chave) % 26
            nova_letra = alfabeto[nova_posicao]
            mensagem_decriptografada += nova_letra
        else:
            mensagem_decriptografada += letra

    return {"decripted_message": mensagem_decriptografada}


def getMessageFromDogApi():

    urlDogApi = 'http://dog-api.kinduff.com'
    response = requests.get(f"{urlDogApi}/api/facts")

    return response.json()
