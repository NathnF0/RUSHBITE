import subprocess
import os

# Cores e Formatação
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

def limpar_console():
    """Limpa o terminal de forma moderna, evitando o aviso de 'deprecated'"""
    if os.name == 'nt':  # Windows
        subprocess.run("cls", shell=True)
    else:  # Linux/Mac
        subprocess.run("clear", shell=True)

def exibir_cabecalho(titulo):
    """Limpa a tela e exibe um cabeçalho padronizado e centralizado"""
    limpar_console()
    print(f"{YELLOW}{'=' * 50}{RESET}")
    print(f"{BOLD}{titulo.center(50)}{RESET}")
    print(f"{YELLOW}{'=' * 50}{RESET}\n")
def exibir_cabecalho(titulo):
    """Limpa a tela e exibe um cabeçalho padronizado e centralizado"""
    limpar_console()
    print(f"{YELLOW}{'=' * 50}{RESET}")
    print(f"{BOLD}{titulo.center(50)}{RESET}")
    print(f"{YELLOW}{'=' * 50}{RESET}\n")

def ler_float(mensagem):
    """Garante que o preço seja um número válido, aceitando vírgula ou ponto"""
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print(f"{RED}❌ Erro: Digite um valor numérico válido.{RESET}")

def pausar():
    """Pausa a execução para o usuário ler a mensagem antes de limpar a tela"""
    input(f"\n{ITALIC}Pressione Enter para continuar...{RESET}")