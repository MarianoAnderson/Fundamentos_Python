MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a carteira de motorista")

if idade < MAIOR_IDADE:
    print("Não pode tirar a carteira de motorista")   


if idade >= MAIOR_IDADE:
    print("Pode tirar a carteira de motorista")
else:
    print("Não pode tirar a carteira de motorista")   


if idade >= MAIOR_IDADE:
    print("Pode tirar a carteira de motorista")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas")
else:
    print("Não pode tirar a carteira de motorista")   