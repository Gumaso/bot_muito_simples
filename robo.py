from datetime import datetime
def apresentacao():
    nome = input("Qual o nome do robo?")
    idade = int(input("Qual a minha idade?"))
    print(f"Olá {nome}, prazer em conhecê-lo!")
    print(f"Eu fui criado em {datetime.now().year - idade}")