from datetime import datetime


def apresentacao():
    nome = input("Qual o nome do robo?")
    idade = int(input("Qual a minha idade?"))
    print(f"Olá! Me chamo {nome}")
    print(f"Eu fui criado em {datetime.now().year - idade}")


def conhecendo_user():
    usuario = input("Qual o seu nome usuário?")
    print(f"Prazer em conhecê-lo {usuario}!")


def advinha():
    print("Vou advinhar sua idade!")
    print("Digite o resto da divisão da sua idade por 3, 5 e 7.")
    print("Ou seja, o que sobra quando você divide sua idade por 3, 5 e 7")
    resto3 = int(input("Resto por 3"))
    resto5 = int(input("Resto por 5"))
    resto7 = int(input("Resto por 7"))
    idade = (resto3 * 70 + resto5 * 21 + resto7 * 15) % 105
    print(f"Sua idade é {idade}, você nasceu {datetime.now().year - idade}")


def contador():
    print('Digite um número para que eu o apresente de forma descrecente e crescente')
    numero = int(input('Número:'))
    print('ORDEM CRESCENTE')
    for x in range(0, numero + 1):
        print(x)

    print('ORDEM DESCRESCENTE')
    for x in range(numero, 0, -1):
        print(x)


def quiz():
    print('Pergunta: Qual é o planeta do nosso sistema solar conhecido como "Planeta Vermelho"?')
    print(
        """
        1. Júpiter
        2. Marte
        3. Vênus
        4. Saturno
        """)
    pergunta = int(input())
    if pergunta == 2:
        print(
            'Resposta correta!\nMarte, já que é o planeta do nosso sistema solar conhecido como o "Planeta Vermelho".')
    else:
        print('Resposta incorreta!\nA resposta correta é a opção 1. Marte, já que é o planeta do nosso sistema solar '
              'conhecido como o "Planeta Vermelho".')
