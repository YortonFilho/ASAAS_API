
# Automação para Extração de Dados da API ASAAS e Inserção no Banco de Dados Oracle

## Descrição

Automação em Python para extrair e tratar dados da API do ASAAS, e importa-los para o banco de dados Oracle SQL. 

Projeto feito usando módulos e funções, para facilitar tanto a manutenção quanto a implementação de novos endpoints no futuro.

## Módulos

A estrutura do projeto é dividida nos seguintes módulos:

- **config**: Responsável por testar e verificar as variáveis de ambiente necessárias para o funcionamento do projeto.
- **data_base**: Contém funções relacionadas ao banco de dados, como conexão (`db_connection`) e inserção de dados.
- **data_extractor**: Implementa as funções de extração de dados da API ASAAS.
- **data_process**: Contém funções para tratamento de dados, como normalização (expansão) e renomeação de colunas.
- **logger**: Contém a função para gerar logs.

Cada módulo é projetado para ser independente, permitindo fácil manutenção e adição de novos recursos.

## Variáveis de Ambiente

Para rodar o projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu arquivo `.env`:

'DB_NAME': Nome do banco de dados

'DB_USER': Usuário/login do banco de dados

'DB_PASSWORD': Senha do banco de dados

'API_URL': URL base da API.

'API_KEY': Chave token de acesso à API.


## Como Rodar o Projeto

1. **Clone o Repositório**

```bash
git clone https://github.com/YortonFilho/ASAAS_API.git
cd ASAAS_API
```

2. **Crie um ambiente virutal**

```bash
python -m venv venv
.\venv\Scripts\activate
```
    
3. **Instale as Dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as Variáveis de Ambiente**

Crie um arquivo .env na raiz do projeto, caso ele não exista, 
e adicione as variáveis necessárias (veja a seção "Variáveis de Ambiente").

5. **Faça os ajustes necessários no arquivo main**

Coloque o nome da tabela que gostaria de atualizar, o restante do endpoint e os parâmetros de data.

6. **Execute o projeto**

```bash
python main.py
```