import os
import subprocess
import platform
from time import sleep

def install_rich():
    try:
        import rich
        print('Biblioteca Rich Console já está instalada.')
    except ImportError:
        try:
            subprocess.check_call(['pip', 'install', 'rich'])
            print('Biblioteca Rich Console instalada com sucesso!')
        except subprocess.CalledProcessError:
            print('Erro ao instalar a biblioteca Rich Console.')
            exit(1)

install_rich()
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

console = Console(color_system="windows")

restaurantes = [{'nome':'Pizzeria Joao', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Pastelaria da Akemi', 'categoria':'Pastel', 'ativo':False},
                {'nome':'McDonalds', 'categoria':'Lanche', 'ativo':True}]

compatibleClear = lambda: print('\n'*100)

modoCompatibilidade = bool(0)

def exibir_nome_do_programa():
    texto = """
░█████╗░██╗░░██╗███████╗███████╗░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔════╝██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░█████╗░░██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░
██║░░██╗██╔══██║██╔══╝░░██╔══╝░░██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║███████╗██║░░░░░╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝
    """

    linhas = texto.strip().splitlines()
    for linha in linhas:
        texto_colorido = Text()
        for caractere in linha:
            cor = (ord(caractere) * 50) % 256  # Gera cores variadas
            texto_colorido.append(caractere, style=f"color({cor})")
        console.print(texto_colorido)
    print(""" """)

def exibir_opcoes():
    tabela = Table(show_header=False, box=None)
    tabela.add_row("[yellow]1.[/yellow]", "Cadastrar restaurante")
    tabela.add_row("[yellow]2.[/yellow]", "Listar restaurantes")
    tabela.add_row("[yellow]3.[/yellow]", "Ativar/Desativar restaurantes")
    tabela.add_row("[yellow]4.[/yellow]", "Sair")
    console.print(tabela,'')

def limpar_tela():
    if modoCompatibilidade == 0:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    else:
        compatibleClear()

def voltar_menu_principal():
    Prompt.ask("\n[wheat1]Aperte uma tecla para voltar ao menu principal[/wheat1]")
    main()

def finalizar_app():
    limpar_tela()
    print("Encerrando o app.")
    exit(0)

def cadastrar_novo_restaurante():
    '''Função responsável por cadastrar novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona o novo restaurante e categoria do mesmo no dicionário 'restaurantes'

    '''
    limpar_tela()
    console.print("[khaki1]Cadastro de novos restaurantes.[/khaki1]\n")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ").strip()
    if nome_do_restaurante:
        pass
    else:
        console.print("[bold red]O nome do restaurante não pode estar vazio![/bold red]")
        voltar_menu_principal()

    categoria_do_restaurante = Prompt.ask(f'Digite a categoria do restaurante [green3]{nome_do_restaurante}[/green3] que deseja cadastrar').strip()
    if categoria_do_restaurante:
        console.print(f"O restaurante [green3]{nome_do_restaurante}[/green3] na categoria [green3]{categoria_do_restaurante}[/green3] foi cadastrada com sucesso!")
    else:
        console.print(f"[bold red]A categoria do restaurante {nome_do_restaurante} não pode estar vazio![/bold red]")
        voltar_menu_principal()

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    voltar_menu_principal()

def listar_restaurantes():
    '''Função resposável por listar os restaurantes cadastrados
    
    Outputs:
    -Lista todos os itens dentro do dicionário 'restaurantes'
    
    '''
    limpar_tela()
    console.print('[khaki1]Listando os restaurantes.[/khaki1]\n')
    if not restaurantes:
        console.print("[bold red]Nenhum restaurante cadastrado.[/bold red]")
    else:
        tabela = Table(show_header=True, header_style="bold steel_blue3")
        tabela.add_column("Nome do Restaurante", style="bold white", width=30)
        tabela.add_column("Categoria", style="bold white", width=20)
        tabela.add_column("Status", style="bold yellow", justify="center")
        
        for item in restaurantes:
            status_text = "[green]Ativado[/green]" if item['ativo'] else "[red]Desativado[/red]"
            tabela.add_row(
                f"[white]{item['nome']}[/white]", 
                f"[yellow]{item['categoria']}[/yellow]",
                status_text)

    console.print(tabela)
    voltar_menu_principal()
    
def ativar_restaurante():
    '''Função responsável por ativar e desativar o status do restaurante
    
    Inputs:
    - Escolher restaurante que deseja ativar/desativar
    
    '''
    limpar_tela()
    console.print("[khaki1]Alterando o estado do restaurante.[/khaki1]\n")

    tabela1 = Table(show_header=True, header_style="bold steel_blue3")
    tabela1.add_column("Nome do Restaurante", style="white", width=30)
    tabela1.add_column("Status", style="bold yellow", justify="center")

    for item in restaurantes:
        nome_restaurante = item['nome']
        ativo = item['ativo']
        status = "[italic green1]Ativado[/italic green1]" if ativo else "[italic red1]Desativado[/italic red1]"
    
        tabela1.add_row(nome_restaurante, status)

    console.print(tabela1)
    print("")

    nome_restaurante = input("Digite o nome do restaurante: ").strip()
    restaurante_encontrado = False

    for i in restaurantes:
        if nome_restaurante == i['nome']:
            restaurante_encontrado = True
            i['ativo'] = not i['ativo']
            mensagem = f'O restaurante [green3]{nome_restaurante}[/green3] foi ativado com sucesso!' if i['ativo'] else f'O restaurante [green3]{nome_restaurante}[/green3] foi desativado com sucesso!'
            console.print(mensagem)
    if not restaurante_encontrado:
        console.print("[red1]O restaurante não foi encontrado.[/red1]")
    voltar_menu_principal()

def opcao_invalida():
    console.print("[red1]Opcão inválida.[/red1]\n")
    voltar_menu_principal()

def toggleModoCompatibilidade():
    global modoCompatibilidade
    
    if modoCompatibilidade == 0:
        modoCompatibilidade = bool(1)
        compatibleClear()
        print("O Modo de Compatibilidade foi ativado!")
        sleep(1.25)
        main()
    else:
        modoCompatibilidade = bool(0)
        compatibleClear()
        print("O Modo de Compatibilidade foi desativado!")
        sleep(1.25)
        main()
    
def escolher_opcoes():
    opcao_escolhida = input('Escolha uma opção: ')
    try:
        opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 0:
            toggleModoCompatibilidade()
        elif opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
            return
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
