from src.database import carregar_empresas
from src.telas.cliente import rodar_menu_cliente
from src.telas.empresa import rodar_menu_empresa
from src.utils import exibir_cabecalho, GREEN, RED, RESET, BOLD

def main():
    # 1. Carrega os dados (já com as empresas Premium que definimos)
    empresas = carregar_empresas()
    
    while True:
        # 2. Exibe o menu principal com limpeza de tela automática
        exibir_cabecalho("🍔 RUSHBITE - DELIVERY SYSTEM 🍟")
        
        print(f"{BOLD}Como deseja acessar o sistema?{RESET}")
        print("\n1 - Sou Cliente (Fazer Pedido)")
        print("2 - Sou Empresa (Gerenciar Loja)")
        print(f"{RED}0 - Sair do Programa{RESET}")
        
        opcao = input(f"\n{BOLD}Opção: {RESET}")
        
        if opcao == "1":
            rodar_menu_cliente(empresas)
        elif opcao == "2":
            rodar_menu_empresa(empresas)
        elif opcao == "0":
            # Limpa antes de sair para deixar o terminal do usuário organizado
            exibir_cabecalho("ATÉ LOGO!")
            print(f"{GREEN}Obrigado por usar o RushBite. Boas vendas!{RESET}\n")
            break
        else:
            print(f"\n{RED}❌ Opção inválida! Tente novamente.{RESET}")
            # Um pequeno delay ou input aqui para o usuário ler o erro antes de limpar
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()