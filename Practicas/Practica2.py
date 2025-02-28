import string

abecedario = list(string.ascii_lowercase)

for i in range(len(abecedario), 0, -1):
    if i % 3 == 0:
        del abecedario[i - 1]

print("Lista modificada:", abecedario)
