def saudacao(nome="Mundo"):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    while True:
        nome = input("Digite seu nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            print("Até logo!")
            break
        print(saudacao(nome))
