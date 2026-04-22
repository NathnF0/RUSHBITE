# 🍔 RushBite: The Terminal Delivery Engine (v0.3.0 Stable)

> **A "zero-crash" NoSQL Delivery ecosystem built for performance and reliability.**

O **RushBite** é um ecossistema de PDV (Ponto de Venda) e Delivery de alta performance que opera inteiramente via terminal. Mais do que um script, é uma solução de engenharia modular projetada para escalabilidade, com tratamento de exceções rigoroso e uma experiência de usuário (UX) inspirada em interfaces modernas.

---

## 💎 O que há de novo na v0.3.0 (The Shield Update)

Esta versão marca a transição do projeto para o estado **Production Ready**. 
- **🛡️ Data Shielding:** Implementação de tratamento de tipos e buscas seguras (`.get()`) em todo o núcleo, eliminando `KeyErrors`.
- **🔄 State Sync:** Sincronização em tempo real entre memória do sistema e persistência JSON.
- **🎟️ Rush Loyalty 2.0:** Loja de cupons integrada com travas de nível (Bronze, Prata, Ouro) e validação de saldo de XP.
- **📍 Structured Logistics:** Motor de endereçamento que suporta objetos geográficos complexos.

---

## 🔥 Funcionalidades de Elite

### 👤 Jornada do Cliente (Customer Experience)
* **🛒 Smart Shopping:** Cardápio dinâmico com auto-hide de itens sem estoque.
* **⭐ Rush Loyalty System:** Barra de progresso visual e evolução de nível baseada em gamificação.
* **🎟️ Coupon Marketplace:** Resgate de descontos via XP com geração de códigos criptográficos únicos.
* **📦 Order Tracking:** Histórico de pedidos com filtragem inteligente por status.

### 🏢 Gestão Empresarial (Business Intelligence)
* **📈 Dashboard Analytics:** Ranking de produtos e KPIs de faturamento bruto/líquido.
* **📦 Stock Master:** Inventário dinâmico com suporte a itens ilimitados.
* **🔔 Live Queue:** Fila de produção em tempo real com alteração de status via terminal.

---

## 🏗️ Arquitetura do Sistema

O projeto segue o padrão **Modular Monolith**, garantindo que a lógica de interface (View) esteja separada do motor de persistência (Data).

```text
rushbite/
├── main.py              # Bootstrap & Auth System (Identity Provider)
├── src/
│   ├── database.py      # NoSQL Engine (JSON Persistence Layer)
│   ├── utils.py         # UI/UX Core, ANSI Engine & Helpers
│   └── telas/
│       ├── cliente.py   # Customer Journey & Gamification Logic
│       └── empresa.py   # Admin Panel & BI Dashboards
└── data/                # Database Storage (.json files)
🚀 Deployment Rápido
Clone o Motor:

Bash
git clone [https://github.com/NathnF0/RUSHBITE.git](https://github.com/NathnF0/RUSHBITE.git)
Setup:

Bash
cd rushbite
Ignite:

Bash
python main.py
📈 Roadmap de Evolução
[x] v0.2.8 - BI, Fidelidade e Endereço Estruturado.

[x] v0.3.0 - Refatoração Crítica: Estabilidade, Sincronização de Dados e Loja de Cupons.

[ ] v0.3.5 — UX & Analytics: Sistema de Avaliações (Stars), Comentários nos Pedidos e Gráficos de Venda via Matplotlib/Terminal.

[ ] v0.4.0 - Sistema Multiusuário com Rastreamento de Entregadores.

[ ] v0.5.0 — Global Scale: Suporte a Multi-lojas e API de Integração Externa.

🤝 Contribuição e Engenharia
Contribuições que visam otimizar o consumo de memória ou melhorar o motor de busca NoSQL são bem-vindas.

Faça um Fork do projeto.

Crie uma Branch (git checkout -b feature/AmazingFeature).

Dê o Commit (git commit -m 'Add some AmazingFeature').

Push (git push origin feature/AmazingFeature).

Abra um Pull Request.

📜 Licença
Distribuído sob a licença MIT.

Desenvolvido com ☕, 🐍 e muita persistência por Nathn.
