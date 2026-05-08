# VoltEye API

API em FastAPI para receber medições de consumo elétrico enviadas por dispositivos IoT e gravar no Supabase.

## Estrutura

```txt
.
|-- main.py
|-- schemas.py
`-- src
    |-- bd
    |   `-- connect.py
    |-- controllers
    |   |-- health_controller.py
    |   `-- medicao_controller.py
    |-- core
    |   `-- config.py
    |-- repositories
    |   `-- medicao_repository.py
    |-- services
    |   `-- medicao_service.py
    `-- schemas
        `-- medicao_schema.py
```

## Responsabilidade das pastas

A separação do projeto segue a ideia de manter cada arquivo com uma responsabilidade pequena e bem definida. Assim, uma mudança em regra de negócio, banco de dados ou rota HTTP tende a ficar isolada em uma única camada.

### `main.py`

Ponto de entrada da aplicação.

Deve conter apenas:

- criação da instância `FastAPI`;
- configurações gerais da API;
- registro dos controllers/routers.

Evite colocar regras de negócio, queries ou validações específicas nesse arquivo.

### `src/controllers`

Camada responsável pelos endpoints HTTP.

Deve conter:

- definição das rotas;
- parâmetros de path, query e body;
- status codes;
- chamadas para services;
- tratamento de erros HTTP.

Evite acessar banco de dados diretamente aqui. O controller deve coordenar a requisição, não executar a regra principal.

### `src/services`

Camada responsável pelas regras de negócio.

Deve conter:

- validações que dependem do contexto da aplicação;
- fluxo principal de cada funcionalidade;
- chamadas para repositories;
- combinação de dados quando uma funcionalidade precisar de mais de uma fonte.

Mantenha os services atômicos: cada método deve representar uma ação clara, como `registrar_medicao`.

### `src/repositories`

Camada responsável pelo acesso a dados.

Deve conter:

- consultas ao Supabase;
- inserts, updates, deletes e selects;
- nomes de tabelas;
- detalhes específicos do banco.

Evite colocar regra de negócio aqui. O repository deve saber como salvar ou buscar dados, mas não decidir o fluxo da funcionalidade.

### `src/schemas`

Camada responsável pelos contratos de entrada e saída da API.

Deve conter:

- schemas Pydantic para request body;
- schemas Pydantic para response;
- exemplos de campos;
- validações simples de formato e tipo.

Evite colocar chamadas de banco ou regras complexas nos schemas.

### `src/core`

Camada responsável por configurações compartilhadas da aplicação.

Deve conter:

- leitura de variáveis de ambiente;
- configurações globais;
- constantes de infraestrutura;
- objetos usados por várias camadas.

### `src/bd`

Camada responsável pela conexão com o banco.

Deve conter:

- criação do client do Supabase;
- configuração da conexão;
- funções auxiliares diretamente ligadas ao banco.

O ideal é que somente repositories usem essa camada diretamente.

## Configuração

Crie um arquivo `.env` com:

```env
SUPABASE_URL=
SUPABASE_KEY=
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar

```bash
fastapi dev main.py
```

ou:

```bash
uvicorn main:app --reload
```

A API fica disponível em:

```txt
http://localhost:8000
```

## Swagger

O Swagger já vem instalado junto com o FastAPI. Acesse:

```txt
http://localhost:8000/docs
```

Documentação alternativa:

```txt
http://localhost:8000/redoc
```

## Endpoints

### Status

```http
GET /
```

Resposta:

```json
{
  "message": "VoltEye API"
}
```

### Registrar medição

```http
POST /dispositivos/{dispositivo_id}/medicoes
```

Exemplo:

```bash
curl -X POST "http://localhost:8000/dispositivos/tomada-01/medicoes" \
  -H "Content-Type: application/json" \
  -d '{
    "corrente": 2.5,
    "tensao": 220,
    "potencia": 550,
    "timestamp": "2026-04-25T14:30:00Z"
  }'
```

Body:

```json
{
  "corrente": 2.5,
  "tensao": 220,
  "potencia": 550,
  "timestamp": "2026-04-25T14:30:00Z"
}
```
