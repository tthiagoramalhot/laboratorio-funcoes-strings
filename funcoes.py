def criptogra(texto, peso, opcao):
  criptografia = ''
  for i in texto:
    if opcao == 'CP':
      palavra = chr(ord(i) + peso)
    elif opcao == 'DP':
      palavra = chr(ord(i) - peso)
    criptografia += palavra
  return criptografia
