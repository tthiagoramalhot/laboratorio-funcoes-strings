import funcoes

opcao = input('Criptografar(CP) ou Descriptografar(DP) : ')
texto = input('Digite um tetxto : ')

cripTexto = funcoes.criptogra(texto, 4, opcao)
print(cripTexto)