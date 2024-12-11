import os

def listar_arquivos():
    pasta = "Perfil"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    return arquivos

def criar_perfil():
    pasta = "Perfil"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    nome = input("Digite o nome do novo perfil: ")
    caminho_arquivo = os.path.join(pasta, f"{nome}.txt")
    if os.path.exists(caminho_arquivo):
        print(f"Erro: Já existe um perfil com o nome '{nome}'.")
        return
    with open(caminho_arquivo, "w") as arquivo:
        conteudo = input("Digite o conteúdo do perfil: ")
        arquivo.write(conteudo)
    print(f"Perfil '{nome}' criado com sucesso!")

def usar_perfil_existente():
    pasta = "Perfil"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    arquivos = listar_arquivos()
    if not arquivos:
        print("Nenhum perfil existente encontrado.")
        return

    print("Perfis disponíveis:")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    try:
        escolha = int(input("Escolha o número correspondente ao perfil: ")) - 1
        if 0 <= escolha < len(arquivos):
            with open(os.path.join(pasta, arquivos[escolha]), "r") as arquivo:
                conteudo = arquivo.read()
                print(f"Conteúdo do perfil '{arquivos[escolha]}':\n{conteudo}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        print("\n=== Gerenciador de Perfis ===")
        print("1. Criar novo perfil")
        print("2. Usar perfil existente")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_perfil()
        elif opcao == "2":
            usar_perfil_existente()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()