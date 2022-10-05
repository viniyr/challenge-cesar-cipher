# Cifra de Cesar - Atividade de estágio

Essa API foi disponibilizada para a criptografia de fatos de cachorros utilizando uma api pública (https://kinduff.github.io/dog-api/). <br>
E para associação foi utilizada a : https://thedogapi.com/

Como subir o banco de dados: <br>
   - Necessário ter DOCKER instalado em sua máquina
   - Primeiro crie dois volumes e uma rede para o mySQL com os seguinte comandos: 
         ```
                docker volume create mysql 
         ```
         ```
                docker volume create mysql_config
         ```
         ```
                docker network create mysqlnet
         ```
   - Em seguida rode o container do mySQL com o seguinte comando: <br>
         ```
         docker run --rm -d -v mysql:/var/lib/mysql \
         -v mysql_config:/etc/mysql -p 3306:3306 \
          --network mysqlnet \
         --name mysqldb \
         -e MYSQL_ROOT_PASSWORD= (SUA SENHA AQUI) \
         mysql 
         ```<br>
   - Caso precise acessar o banco do terminal: 
         ```docker exec -ti mysqldb mysql -u root -p ```

Como rodar: <br>
   - Será necessário um arquivo .env contendo todas informações confidenciais com a seguinte estrutura: <br>
            DB_HOST=str <br>
            DB_USER=str <br>
            DB_PASSWORD=str <br>
            DB_DATABASE=str <br>
   
   
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
<br>
  /saveFact -> Irá salvar um fato sobre cachorro da api kinduff e realizará a persistência desse dado no banco de dados local. Após isso a aplicação irá identificar se o fato em questão menciona alguma raça de cachorro se mencionar ela irá associar com a raça disponibilizada pela the dog api
                  
     
