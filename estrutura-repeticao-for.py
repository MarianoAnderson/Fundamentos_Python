texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()


#built-in range     i  stop  step
for numero in range(0, 51, 5):
    print(numero, end=" ")