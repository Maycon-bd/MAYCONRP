def saudacao(nome="Mundo"):
    return f"Olá, {nome}!"

def contar_caracteres(nome):
    return f"Seu nome tem {len(nome)} caracteres."

if __name__ == "__main__":
    while True:
        nome = input("Digite seu nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            print("Até logo!")
            break
        print(saudacao(nome))
        print(contar_caracteres(nome))
