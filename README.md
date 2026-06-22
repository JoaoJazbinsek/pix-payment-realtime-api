# API Pix em Tempo Real

API desenvolvida com Python e Flask para simular a criação de pagamentos Pix, geração de QR Code e confirmação de pagamento em tempo real utilizando WebSocket.

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de backend, APIs REST, banco de dados, geração de QR Code e comunicação em tempo real.

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
- Consultar dados do pagamento
- Exibir página de pagamento
- Confirmar pagamento
- Enviar confirmação em tempo real via WebSocket

## Rotas da aplicação

### Criar pagamento Pix

```http
POST /payments/pix
