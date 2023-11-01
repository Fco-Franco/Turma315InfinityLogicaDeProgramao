#region - Programa que conta de 1 a 10 com While
# numero = 0
# while numero < 10:
#     print(numero)
#     numero = numero + 1
#     # numero += 1
#endregion

# region - FAÇA UM PROGRAMA QUE MOSTRE TODOS OS NÚMEROS DE 1 A 200 USANDO WHILE E DEPOIS USANDO FOR
# numero = 1
# while numero <= 200:
#     print(numero)
#     numero += 1

# for i in range(1,201):
#     print(i)
#endregion

# region FAÇA UM PROGRAMA QUE MOSTRE OS NÚMEROS DE 0 A 100 PORÉM MOSTRANDO APENAS AS DEZENAS utilizando WHILE E FOR
# valor = 0
# while valor <= 100:
#     print(valor)
#     valor = valor + 10

# #Utilizando FOR, RANGE
# for i in range(0,101,10):
#     print(i)

# valor = 0

# Utilizando matemática
# while valor <= 100:
#     if valor % 10 == 0:
#         print(valor)
#     valor = valor + 1
#endregion

#region - Programa que solicita que usuário digite um número, quando o número digitado for maior que 100 ele finaliza
# while True:
#     numero = int(input("Digite um número: "))   

#     if numero > 100:
#         break
#     else:
#         print(numero) 
#endregion

#region - Q1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# while True:
#     nota = float(input("Digite uma nota: "))

#     if nota >=0 and nota <=10:
#         print("Nota válida")
#         break
#     else:
#         print("Nota inválida, digite uma nota entre 0 e 10")
#endregion

#region Q2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# while True:
#     nome = str(input("Digite o nome de usuário: "))
#     senha = str(input("Digite a sua senha: "))

#     if nome != senha:
#         break
#     else:
#         print("Nome e senha não podem ser iguais!")
#endregion

# region Q3:Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 100;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# while True:
#     nome = str(input("Digite seu nome:"))
#     if len(nome) > 3:
#         break
#     else:
#         print("Digite um nome com no mínimo 3 caracteres")

# while True:
#     idade = int(input("Digite a sua idade: "))
#     if idade >= 0 and idade <=100:
#         break
#     else:
#         print("Digite uma idade entre 0 e 100")

# while True:
#     salario = float(input("Digite seu salário: "))
#     if salario > 0:
#         break
#     else:
#         print("Digite um salário maior que 0")

# while True:
#     sexo = str(input("Digite seu sexo: [M | F]")).upper()

#     if len(sexo) == 1:
#         if sexo == "M" or sexo == "F":
#             break
#         else:
#             print("Digite um sexo válido ou M ou F")
#     else:
#         print("Digite apenas uma letra")

# while True:
#     estado_civil = str(input("Digite seu estado civil: [S | C | V | D]")).upper()

#     if len(estado_civil) == 1:
#         if estado_civil == "C" or estado_civil == "S" or estado_civil == "V" or estado_civil == "D":
#             break
#         else:
#             print("Digite um estado civil correto.")
#     else:
#         print("Digite apenas uma letra")
#endregion

#region Q4: Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes 
# com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento. 

# paisA = int(input("Quantos habitantes esse país tem? "))
# paisB = int(input("Quantos habitantes esse outro país tem?"))
# paisA = 80000
# paisB = 100000
# ano = 0

# while paisA <= paisB:
#     paisA += paisA * 0.03
#     paisB += paisB * 0.015
#     ano += 1

# print(f"Pais A, ultrapassa Pais B em {ano} anos")

#endregion

#region - Q5: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
# while True:
#     paisA = int(input("Digite quantos habitantes esse pais tem?: "))
#     taxA = float(input("Quantos porcento esse País cresce ao ano?: "))
#     paisB = int(input("Digite quantos habitantes esse outro pais tem?: "))
#     taxB = float(input("Quantos porcento esse outro País cresce ao ano?: "))
    
#endregion

#region - Q6: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
# num = 0
# while num < 21:
#     print(num)
#     num += 1

#imprimindo os números lado a lado
# num = 0
# while num < 21:
#     print(num, end=', ')
#     num += 1
#endregion

#region Q7: Faça um programa que leia 5 números e informe o maior número.
#import random
#n1 = random.choice in range(1,101)
# n1 = int(input("Informe um número: "))
# n2 = int(input("Informe o 2ºnúmero: "))
# n3 = int(input("Informe o 3º número: "))
# n4 = int(input("Informe o 4º número: "))
# n5 = int(input("Informe o 5º número: "))
# while n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
#     print(f"o Número:{n1} é o maior número")
#     break
# while n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
#     print(f"o Número:{n2} é o maior número")
#     break
# while n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
#     print(f"o Número:{n3} é o maior número")
#     break
# while n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
#     print(f"o Número:{n4} é o maior número")
#     break
# while n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
#     print(f"o Número:{n5} é o maior número")
#     break
#endregion

#region - Q8: Faça um programa que leia 5 números e informe a soma e a média dos números.
while True:
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe o 2ºnúmero: "))
    n3 = float(input("Informe o 3º número: "))
    n4 = float(input("Informe o 4º número: "))
    n5 = float(input("Informe o 5º número: "))

    if n1 or n2 or n3 or n4 or n5 <= 0:
        print("Digite um número maior que zero!")
    
    while n1 and n2 and n3 and n4 and n5 > 0:
        soma = n1+n2+n3+n4+n5
        media = soma/5
        print(f"A soma dos números inseridos é:{soma} ") 
        print(f"E a media dos números  é:{media}") 
        break

#endregion

#region - Q9: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
num = 1
while num <= 50:
    if num %2 != 0:
        print(num)
    num += 1
#endregion
#region - DESAFIO: Loja de Doces
# PROBLEMA: Uma loja de doces vai lançar uma promoção onde sorteará um brinde entre 3 clientes do dia

# O SORTEIO: Ao registrar uma venda o caixa da loja pergunta nome, endereço e telefone do cliente e insere essas informações em uma aplicação que ficará executando durante todo o expediente da Loja (em processo de repetição)
# A aplicação deve guardar todas as ocorrências de informações sobre o cliente até que o caixa seja encerrado (você decide como será inserida a informação)
# ao final do expediente, o caixa informa na aplicação um cliente chamado "fim", e a aplicação, sorteará um dos clientes atendidos ao longo do dia;
# a aplicação informará na tela todos os os dados do cliente sorteado e se encerrará.

# ENTREGA: Deve ser entregue um fluxograma contendo a sequência lógica de instruções para a aplicação funcionar;
# A codificação em linguagem Python da solução do problema.


# import random
# lista = []
# while True:
#     nome = str(input("Digite seu nome: "))
#     if nome == "fim":
#         break
#     telefone = str(input("Digite seu telefone: "))
#     endereco = str(input("Digite seu endereco: "))
#     lista.append([nome, telefone, endereco])

# sorteado = random.choice(lista)

# sorteado2 = random.choice(lista)

# while sorteado[0] == sorteado2 [0]:
#     sorteado2 = random.choice(lista)

# sorteado3 = random.choice(lista)

# while sorteado[0] == sorteado3 [0] or sorteado2[0] == sorteado3[0]:
#     sorteado2 = random.choice(lista)

# print(f"""
#         Sorteado foi
#         Nome: {sorteado[0]}
#         Telefone: {sorteado[1]}
#         Endereço: {sorteado[2]}
# """)
#endregion
