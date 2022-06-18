minha_string = input('Digite uma string: ')
length = len(minha_string)
i = length
array_reverso = []

while i > 0:
    array_reverso += minha_string[i - 1]
    i = i - 1

string_reversa = ''.join(array_reverso)

print(string_reversa)