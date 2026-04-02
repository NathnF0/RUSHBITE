from src.utils import GREEN, RED, YELLOW, RESET, BOLD, ITALIC, ler_float, exibir_cabecalho, pausar
from src.database import salvar_empresas

def rodar_menu_empresa(empresas):
    while True:
        exibir_cabecalho("🏢 MODO EMPRESA - ACESSO")
        print("1 - Fazer Login")
        print("2 - Criar Nova Loja")
        print("0 - Voltar ao Menu Principal")
        
        escolha = input(f"\n{BOLD}Escolha: {RESET}")

        if escolha == "1":
            exibir_cabecalho("🔐 LOGIN DE EMPRESA")
            nome = input("Nome da empresa: ").strip()
            senha = input("Senha: ").strip()
            
            if nome in empresas and empresas[nome]["senha"] == senha:
                print(f"\n{GREEN}✅ Login realizado com sucesso!{RESET}")
                pausar()
                
                # --- PAINEL INTERNO DA EMPRESA ---
                while True:
                    exibir_cabecalho(f"🏪 PAINEL: {nome.upper()}")
                    status = f"{GREEN}Publicada{RESET}" if empresas[nome].get("publicada") else f"{RED}Privada{RESET}"
                    print(f"Status Atual: {status}")
                    print("-" * 30)
                    print("1 - Adicionar Produto")
                    print("2 - Ver Meus Produtos")
                    print("3 - Personalizar Loja (Categoria/Logo)")
                    print("4 - Publicar/Ocultar Loja")
                    print("0 - Sair do Painel")
                    
                    op = input(f"\n{BOLD}Escolha: {RESET}")
                    
                    if op == "1":
                        exibir_cabecalho("➕ ADICIONAR PRODUTO")
                        p = input("Nome do Produto: ")
                        v = ler_float("Preço (R$): ")
                        empresas[nome]["produtos"][p] = v
                        salvar_empresas(empresas)
                        print(f"\n{GREEN}✅ Produto '{p}' adicionado!{RESET}")
                        pausar()
                        
                    elif op == "2":
                        exibir_cabecalho("📋 MEUS PRODUTOS")
                        produtos = empresas[nome]["produtos"]
                        if not produtos:
                            print(f"{YELLOW}Você ainda não tem produtos cadastrados.{RESET}")
                        else:
                            for i, (p, v) in enumerate(produtos.items(), 1):
                                print(f"{i}. {p.ljust(20)} - {YELLOW}R${v:.2f}{RESET}")
                        pausar()
                        
                    elif op == "3":
                        exibir_cabecalho("🎨 PERSONALIZAR LOJA")
                        d = empresas[nome]
                        print(f"{ITALIC}Deixe em branco para manter o atual.{RESET}\n")
                        
                        nova_cat = input(f"Categoria atual [{d.get('categoria', 'N/A')}]: ")
                        if nova_cat: empresas[nome]["categoria"] = nova_cat
                        
                        novo_logo = input(f"Logo/Emoji atual [{d.get('logo', '🍔')}]: ")
                        if novo_logo: empresas[nome]["logo"] = novo_logo
                        
                        salvar_empresas(empresas)
                        print(f"\n{GREEN}✅ Alterações salvas!{RESET}")
                        pausar()
                        
                    elif op == "4":
                        atual = empresas[nome].get("publicada", False)
                        empresas[nome]["publicada"] = not atual
                        salvar_empresas(empresas)
                        status_msg = "PUBLICADA" if not atual else "OCULTADA"
                        print(f"\n{YELLOW}📢 Sua loja agora está {status_msg}!{RESET}")
                        pausar()
                        
                    elif op == "0":
                        break
            else:
                print(f"\n{RED}❌ Erro: Nome ou senha incorretos.{RESET}")
                pausar()

        elif escolha == "2":
            exibir_cabecalho("📝 CRIAR NOVA LOJA")
            nome = input("Nome da nova empresa: ").strip()
            if nome in empresas:
                print(f"\n{RED}❌ Erro: Este nome já está em uso.{RESET}")
                pausar()
                continue
                
            senha = input("Crie uma senha: ")
            empresas[nome] = {
                "senha": senha, 
                "produtos": {}, 
                "publicada": False,
                "categoria": "Geral",
                "logo": "🏪"
            }
            salvar_empresas(empresas)
            print(f"\n{GREEN}✅ Loja criada! Agora faça o login para gerenciar.{RESET}")
            pausar()

        elif escolha == "0":
            break