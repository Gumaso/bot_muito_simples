from datetime import datetime
def apresentacao():
    nome = input("Qual o nome do robo?")
    idade = int(input("Qual a minha idade?"))
    print(f"Olá! Me chamo {nome}")
    print(f"Eu fui criado em {datetime.now().year - idade}")

def conhecendo_user():
    usuario = input("Qual o seu nome usuário?")
    print(f"Prazer em conhecê-lo {usuario}!")