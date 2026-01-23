import random
from quiz.data import questions


print("Bem-vindo(a) ao Quiz Geek rápido!")

jogando = input("Você quer jogar?").lower()
acertos = 0

if jogando != "sim":
    print("Tudo bem! Talvez outra hora")
    print("Voltando a tela principal...")
    quit()
else:
    print("OK! Vamos lá!")
    print("Responda corretamente!!")

erros = [
    "Errado!",
    "Você errou!",
    "Resposta incorreta!",
    "Que pena!, incorreto!",
    "Ops, resposta errada!"
]

for q in questions:
    questao = input(q["questao"]).lower().strip()
    resposta_correta = q["answer"]

    if isinstance(resposta_correta, str) or isinstance(resposta_correta, list):
        if questao in resposta_correta:
            print("Correto!")
            acertos += 1
        else:
            print(random.choice(erros))

     # Se a resposta correta for uma string
    elif isinstance(resposta_correta, str):
        if questao == resposta_correta.lower():  # Verifica se a resposta do jogador é igual à resposta correta
            print("Correto!")
            acertos += 1
        else:
            print(random.choice(erros))  # Resposta errada, escolhe uma mensagem aleatória

# Resultado
soma = acertos/8 * 100
print("Você acertou " + str(acertos) + " das 8 perguntas!")
print(soma, "% de acerto.")

      