# 🍔 RushBite - Delivery System v0.2.6

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Versão%20Estável-green?style=for-the-badge" alt="Status" />
  <a href="https://www.linkedin.com/in/nathan-ferreira01/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
</p>

---

## 📝 Sobre o Projeto
O **RushBite** é um ecossistema completo de delivery operando via terminal, focado em performance e experiência do usuário (UX). O projeto simula a interação real entre **Clientes** (que buscam, pedem e avaliam) e **Empresas** (que gerenciam cardápio, fila de pedidos e financeiro).

Nesta versão **v0.2.6**, alcançamos o patamar de comunicação bilateral e gestão logística avançada.

---

## 🔥 Novidades da v0.2.6.1 (Patch de Comunicação)

### 💬 Chat Bilateral Inteligente
Agora a distância entre a fome e a comida diminuiu!
- **Para o Cliente:** Canal direto para tirar dúvidas sobre o pedido.
- **Para a Empresa:** Interface de "Chat Rápido" via comandos (`c1`, `c2`) ou dentro dos detalhes do pedido.

### ⭐ Feedback & Avaliação
- Sistema de estrelas (1 a 5) para que o cliente avalie a experiência após a entrega.
- Histórico de avaliações visível para o lojista no painel de pedidos.

### 🚚 Logística Flexível de Endereço
- O cliente pode optar por usar o endereço salvo no perfil ou digitar um novo endereço específico para aquela entrega durante o checkout.

### 🧾 Impressão de Comandas
- Geração automática de arquivos `.txt` para cada pedido, permitindo que a empresa tenha um registro físico ou organizado para a "cozinha".

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Persistência de Dados:** JSON (Simulando um banco de dados NoSQL)
- **Interface:** CLI (Command Line Interface) com suporte a cores ANSI

---

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/NathnF0/SISTEMofORDERS-RUSHBITE-.git](https://github.com/NathnF0/SISTEMofORDERS-RUSHBITE-.git)
Entre na pasta:Bashcd "SISTEMofORDERS-RUSHBITE-"
Execute o app:Bashpython main.py
📸 Demonstração das FuncionalidadesFuncionalidadeDescriçãoPainel de OperaçõesGestão de cardápio, estoque e preços em tempo real.Checkout DinâmicoCálculo de taxas de entrega, cupons de desconto e escolha de modalidade.Dashboard FinanceiroVisualização de faturamento líquido e ticket médio da loja.Chat de PedidoHistórico completo de mensagens entre as duas pontas.👨‍💻 DesenvolvedorDesenvolvido com Python por Nathn.
