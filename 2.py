numero = int(input('Digite um número: '))
cont = 0
ultimo_termo = 0
penultimo_termo = 0
aux = 0
pertence = 0
while ultimo_termo <= numero:
    if(ultimo_termo == numero):
        print('O número informado pertence à sequência!')
        pertence = 1
        break
    if (cont == 1):
        ultimo_termo = 1
        penultimo_termo = 0
    else:
        aux = ultimo_termo
        ultimo_termo = ultimo_termo + penultimo_termo
        penultimo_termo = aux
    cont += 1

if pertence == 0:
    print('O número informado não pertence à sequência!')
    