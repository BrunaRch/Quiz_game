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

# Primeira questão
questao = input("Qual é o nome da inteligência artificial que tenta eliminar a humanidade em O Exterminador do Futuro? ").lower().strip()

if questao == "skynet":
    print("Correto!")
    acertos += 1
else:
    print("Errado!")

# Segunda questão
questao = input("Qual foi o primeiro filme do Universo Cinematográfico Marvel (MCU)? ").lower().strip()

if questao == "homem de ferro":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")


# Terceira questão
questao = input("Qual é o nome do planeta natal dos Na’vi em Avatar? ").lower().strip()

if questao == "pandora":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Quarta questão
questao = input("Em Matrix, qual é a cor da pílula que Neo toma para acordar no “mundo real” ").lower().strip()

if questao == "vermelha" or questao == "vermelho":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Quinta questão
questao = input("Em O Senhor dos Anéis, qual é o nome da criatura que guarda o “meu precioso”? ").lower().strip()

if questao == "gollum":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Sexta questão
questao = input("Quem é o vilão principal em Os Vingadores de 2012? ").lower().strip()

if questao == "loki":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Sétima questão
questao = input("Quem destrói o segundo Império Galáctico? ").lower().strip()

if questao == "luke" or questao == "luke skywalker":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Oitava questão
questao = input("Qual o jedi verde mais icônico do universo? ").lower().strip()

if questao == "yoda" or questao == "mestre yoda":
    print("Correto!")
    acertos += 1
else:
    print("Você errou!")

# Resultado
soma = acertos/8 * 100
print("Você acertou " + str(acertos) + " das 8 perguntas!")
print(soma, "% de acerto.")

      