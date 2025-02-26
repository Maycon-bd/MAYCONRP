def saudacao(nome="Mundo"):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
