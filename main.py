alfabeto = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'
]

listaCaracter = []
novoNome = []

nome = input('Digite um texto para criptografar: ')

# Desmenbrando texto
for contador in range(1, len(nome) + 1):
  letra = nome[contador - 1]
  listaCaracter.append(letra)

# Criptografando texto
for i in range(len(listaCaracter)):
  for j in range(len(alfabeto)):
    if listaCaracter[i] == alfabeto[j]:
      novoCaracter = alfabeto[j + 3]
      novoNome.append(novoCaracter)

m = ''.join(novoNome)
print('Texto criptografado:', m)

del listaCaracter[:]
del novoNome[:]

nome = input('Digite um texto para descriptografar: ')

# Desmenbrando texto
for contador in range(1, len(nome) + 1):
  letra = nome[contador - 1]
  listaCaracter.append(letra)

# Desriptografando texto
for i in range(len(listaCaracter)):
  for j in range(len(alfabeto)):
    if listaCaracter[i] == alfabeto[j]:
      novoCaracter = alfabeto[j - 3]
      novoNome.append(novoCaracter)
      
m = ''.join(novoNome)
print('Texto descriptografado:', m)