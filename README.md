# Cifra de Cesar - Atividade de estágio

Essa API foi disponibilizada para a criptografia de fatos de cachorros utilizando uma api pública (https://kinduff.github.io/dog-api/). 

Como rodar: <br>
   - Após clonar o projeto em seu computador abra o terminal e digite: uvicorn cifra:app --reload<br>
   - Toda documentação será disponiblizada em localhost:8000/docs<br>


## Endpoints:<br> 
  /getCifra -> Irá retornar uma frase encriptografada com o fato de um cachorro e a chave utilizada para a criptografia, que poderá ser usada para descriptografar<br><br>
  /resolveCifra -> Vai descriptografar sua mensagem após você fornecer no corpo da requisição a mensagem e a chave: <br>
        ex. do corpo da requisição: 
        
                  {
                    frase_criptografada: string,
                    chave: number
                  }
