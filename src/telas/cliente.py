from datetime import datetime
from src.utils import GREEN, RED, YELLOW, RESET, BOLD, ITALIC, exibir_cabecalho, pausar

def rodar_menu_cliente(empresas):
    exibir_cabecalho("🛒 MODO CLIENTE - RUSHBITE")
    
    # Filtra lojas que têm produtos e estão publicadas
    lojas_disponiveis = {nome: dados for nome, dados in empresas.items() if dados["produtos"] and dados.get("publicada", False)}

    if not lojas_disponiveis:
        print(f"{YELLOW}Aguarde... Nenhuma loja disponível no momento. 😴{RESET}")
        pausar()
        return

    print(f"{BOLD}Lojas disponíveis:{RESET}\n")
    for i, (nome, dados) in enumerate(lojas_disponiveis.items(), 1):
        horario = dados.get("horario", {"abertura": "00:00", "fechamento": "23:59"})
        abertura, fechamento = horario.get("abertura"), horario.get("fechamento")
        hora_atual = datetime.now().strftime("%H:%M")
        
        status = f"{GREEN}● Aberto{RESET}" if abertura <= hora_atual <= fechamento else f"{RED}○ Fechado{RESET}"
        
        print(f"{BOLD}{i} - {dados.get('logo', '')} {nome.upper()} ({dados.get('categoria', '')}) - {status}{RESET}")
        print(f"   {ITALIC}{dados.get('descricao', '')}{RESET}")
        print(f"   Horário: {abertura} - {fechamento}\n")

    while True:
        try:
            opcao_loja = int(input(f"{BOLD}Escolha uma loja (ou 0 para voltar): {RESET}"))
            if opcao_loja == 0: return
            if 1 <= opcao_loja <= len(lojas_disponiveis): break
            print(f"{RED}Opção inválida.{RESET}")
        except ValueError:
            print(f"{RED}Digite um número válido.{RESET}")

    loja_escolhida = list(lojas_disponiveis.keys())[opcao_loja - 1]
    cardapio = lojas_disponiveis[loja_escolhida]["produtos"]

    # --- TELA DE CARDÁPIO ---
    exibir_cabecalho(f"🍴 CARDÁPIO: {loja_escolhida.upper()}")
    
    if not cardapio:
        print(f"{YELLOW}Esta loja ainda não tem produtos cadastrados.{RESET}")
        pausar()
    else:
        for i, (produto, preco) in enumerate(cardapio.items(), 1):
            print(f"{i}. {produto.ljust(20)} - {YELLOW}R${preco:.2f}{RESET}")

        carrinho = []
        while True:
            try:
                opcao_item = int(input(f"\n{BOLD}Escolha o item (ou 0 para finalizar): {RESET}"))
                if opcao_item == 0: break
                
                if not (1 <= opcao_item <= len(cardapio)):
                    print(f"{RED}Opção inválida.{RESET}")
                    continue
                
                item_escolhido = list(cardapio.keys())[opcao_item - 1]
                quantidade = int(input(f"Quantidade de {item_escolhido}: "))
                if quantidade <= 0: continue
                
                carrinho.append((item_escolhido, quantidade))
                print(f"\n✅ {GREEN}{item_escolhido} adicionado!{RESET}")
                
            except ValueError:
                print(f"{RED}Entrada inválida.{RESET}")

        if not carrinho:
            print(f"\n{YELLOW}Carrinho vazio. Voltando...{RESET}")
            pausar()
            return

        # --- TELA DE RESUMO ---
        exibir_cabecalho("🧾 RESUMO DO PEDIDO")
        total = 0
        for item, qtd in carrinho:
            preco = cardapio[item]
            subtotal = preco * qtd
            total += subtotal
            print(f"• {item.ljust(15)} x{qtd} = {YELLOW}R${subtotal:.2f}{RESET}")
        
        print(f"\n{BOLD}TOTAL A PAGAR: {GREEN}R${total:.2f}{RESET}")
        print(f"\n{ITALIC}Pedido enviado para a loja!{RESET}")
        pausar()