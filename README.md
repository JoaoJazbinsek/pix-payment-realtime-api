# API Pix em Tempo Real

API desenvolvida com Python e Flask para simular a criação de pagamentos Pix, geração de QR Code e confirmação de pagamento em tempo real utilizando WebSocket.

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de backend, API REST, banco de dados, geração de QR Code e comunicação em tempo real.

A aplicação permite criar um pagamento Pix, gerar um QR Code associado ao pagamento, consultar a página do pagamento e receber uma notificação em tempo real quando o pagamento é confirmado.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SocketIO
- SQLAlchemy
- SQLite
- QRCode
- HTML
- Git
- GitHub

## Funcionalidades

- Criar pagamento Pix
- Gerar QR Code do pagamento
- Salvar pagamento no banco de dados
- Consultar página do pagamento
- Confirmar pagamento
- Atualizar status do pagamento
- Enviar confirmação em tempo real via WebSocket

## Rotas da aplicação

### Criar pagamento Pix

`POST /payments/pix`

Corpo da requisição:

{
  "value": 50.00
}

### Buscar QR Code do pagamento

`GET /payments/pix/qr_code/<file_name>`

Essa rota retorna a imagem do QR Code gerada para o pagamento.

### Página do pagamento

`GET /payments/pix/<payment_id>`

Essa rota exibe a página do pagamento, mostrando o valor e o QR Code.

### Confirmar pagamento Pix

`POST /payments/pix/confirmation`

Corpo da requisição:

{
  "bank_payment_id": "id-do-pagamento",
  "value": 50.00
}

Quando o pagamento é confirmado, a aplicação atualiza o status no banco de dados e envia uma notificação em tempo real via WebSocket.

## Como executar o projeto

1. Clone o repositório:

`git clone https://github.com/JoaJazbinsek/pix-payment-realtime-api.git`

2. Entre na pasta do projeto:

`cd pix-payment-realtime-api`

3. Instale as dependências:

`pip install -r requirements.txt`

4. Execute o projeto:

`python app.py`

5. Acesse no navegador:

`http://127.0.0.1:5000`

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei conceitos como:

- Criação de APIs com Flask
- Uso de banco de dados com SQLAlchemy
- Modelagem de dados
- Geração de QR Code
- Organização de rotas
- Comunicação em tempo real com WebSocket
- Controle de versão com Git e GitHub

## Status do projeto

Projeto em desenvolvimento.

## Autor

João Vitor Jazbinsek

GitHub: JoaJazbinsek  
LinkedIn: joão-vitor-jazbinsek-leite-53143b236
