def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0) #posicionando cursor no início
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor = float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\Alysson 4º bimestre\\Aulas 16-11-23\\entrada.txt")
    print (valores)
    return sum(valores)

#Exercícios
def maior_valor_arquivo():
    valores = leitura("C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\Alysson 4º bimestre\\Aulas 16-11-23\\entrada.txt")
    return max(valores)
        
def multiplica_valores_arquivo():
    valores = leitura("C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\Alysson 4º bimestre\\Aulas 16-11-23\\entrada.txt")
    temp = 1
    for i in valores:
        temp = temp * i
    return temp   

if __name__=="__main__":
    resultado = soma_valores_arquivo()
    print (f"A soma dos valores dos arquivos são: {resultado}")

    maior = maior_valor_arquivo()
    print (f"O maior valor do arquivo é: {maior}")

    multiplicacao = multiplica_valores_arquivo()
    print (f"A multiplicação entre os valores dos arquivos são: {multiplicacao}")
