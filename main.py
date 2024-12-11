import os

pre_set = """ 
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 10)
time.sleep(1)

def main():
    # Função principal
    driver.get("https://www.google.com")
"""

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
        arquivo.write(pre_set)  # Arquivo criado com o código base
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
            while True:
                print("\n=== Gerenciador de Perfis ===")
                print("1. Exibir conteúdo")
                print("2. Executar conteúdo")
                print("3. Sair")
                opcao = input("Escolha uma opção: ").strip()

                if opcao == '1':
                    with open(os.path.join(pasta, arquivos[escolha]), "r") as arquivo:
                        conteudo = arquivo.read()
                        print(f"Conteúdo do perfil '{arquivos[escolha]}':\n{conteudo}")
                elif opcao == '2':
                    with open(os.path.join(pasta, arquivos[escolha]), "r") as arquivo:
                        conteudo = arquivo.read()
                        try:
                            exec(conteudo)  # Executa o código Python contido no arquivo
                        except Exception as e:
                            print(f"Erro ao executar o código: {e}")
                elif opcao == '3':
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
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
