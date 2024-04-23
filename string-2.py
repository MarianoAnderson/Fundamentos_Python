nome = "Anderson"
idade = 26
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 45.567

dados = { "nome": "Anderson", "idade": 26}

print(f'Meu nome é {nome}, tenho {idade} anos, sou {profissao} e minha linguagem é {linguagem}, saldo de {saldo: 3.1f}.')
print("nome: {nome} idade: {idade}".format(**dados))