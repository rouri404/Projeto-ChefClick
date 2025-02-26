# ChefClick

ChefClick é um programa para cadastro de restaurantes desenvolvido em Python. O projeto teve origem durante o curso "Python: crie a sua primeira aplicação" da Alura, sendo posteriormente aprimorado para incluir melhorias e refinamentos em relação à versão original ensinada no curso.

## Funcionalidades
- Cadastro de restaurantes
- Listagem de restaurantes cadastrados
- Atualização de informações dos restaurantes
- Exclusão de restaurantes do sistema
- [Modo de Compatibilidade](#modo-de-compatibilidade) (sem chamadas de comandos do SO, opcional)

## Tecnologias Utilizadas
- Python 3

## Como Executar o Projeto

### Requisitos
- Python 3 instalado no sistema

### Passos
1. Clone este repositório:
   ```sh
   git clone https://github.com/rouri404/Projeto-ChefClick.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd Projeto-ChefClick
   ```
3. Execute o script principal:
   ```sh
   python app.py
   ```

## Contribuição
Se você deseja contribuir para o ChefClick, fique à vontade para abrir issues ou enviar pull requests!

## Modo de Compatibilidade
Para habilitar o Modo de Compatibilidade, insira o dígito 0 no menu inicial. _(opção oculta/não listada)_

### Funcionamento:
Ao invés de usar chamadas de comando do Sistema Operacional, que pode causar problemas dependendo do OS usado, o Modo de Compatibilidade usa um outro método usando somente Python que limpa a tela do terminal.

#### Diferença entre o Modo de Compatibilidade e o Modo Padrão:
No Modo de Compatibilidade, após a limpeza da tela, o novo texto passa a ser escrito no final da janela do console/terminal, no Modo Padrão o novo texto é escrito no topo da janela do terminal.
