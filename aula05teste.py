def main():
    print("Digite dua frases. digite sair para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)
    with open("meu arquivo.txt", "w") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")
    print("Arquivo original criado. Agora vamos manipular o dados.")
    dados_modificados = []
    with open("meu arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip() .upper()) 

    with open("meu arquivo alterado.txt", "w", encoding='utf-8') as arquivo_alterado:
        for linha in dados_modificados:
           arquivo_alterado.write(linha + "\n")
    print("um novo arquivo fo criado com o nome (arquivo_alterado) com os dados modificados")

if __name__ == "__main__":
    main()