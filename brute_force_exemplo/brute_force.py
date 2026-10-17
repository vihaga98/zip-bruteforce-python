import zipfile


NOME_ARQUIVO = "final.zip"
zip_file = zipfile.ZipFile(NOME_ARQUIVO, "r")


def extrair_arquivo_zip_com_senha(senha: str) -> bool:
    try:
        zip_file.extractall(path=".", pwd=senha.encode("utf-8"))
        return True
    except:  # noqa
        pass
    return False


#Tentativa de 3 carcteres

numeros = "0123456789"
caracteres_maiusculos = "ABCDEFGHIJKLMNOPQRSTUVYXWZ"
caracteres_minusculos = "abcdefghijklmnopqrstuvyxwz"
alfabeto_total = numeros + caracteres_maiusculos + caracteres_minusculos

def senha_secreta():
    for posicao1 in alfabeto_total:
        for posicao2 in alfabeto_total:
            for pocisao3 in alfabeto_total:
                for posicao4 in alfabeto_total:
                    for posicao5 in alfabeto_total:
                        senha = posicao1 + posicao2 + pocisao3 + posicao4 + posicao5
                        print(f"testando {senha}")
                        if extrair_arquivo_zip_com_senha(senha):
                            print(senha)
                            return

senha_secreta()       