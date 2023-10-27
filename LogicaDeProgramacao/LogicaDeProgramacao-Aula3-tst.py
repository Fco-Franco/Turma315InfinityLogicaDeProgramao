
#region Exercicio 02 Faça um programa para imprimir os números pares e impares entre numeros digitados . Utilize a função range() para criar a coleção de números.- 
print("Exercicio 02 - Faça um programa para imprimir os números pares e impares entre numeros digitados. Utilize a função range() para criar a coleção de números.")

num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

while num1 == 1 or num1.isdigit():
    num1 = input("Digite o primeiro numero novamente: ")
    num2 = input("Digite o segundo numero novamente: ")

for i in range(2,21,2):
    print(i)
print("\nMétodo correto")
for i in range(2,21):
    if i%2==0:
        print(i)
#endregion

#region Exercicio 03 - Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a função range() para criar a coleção de números.
print("Exercicio 03 - Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a função range() para criar a coleção de números.")
for i in range(1,20,2):
    print(i)
print("\nMétodo correto")
for i in range(1,20):
    if i %2 !=0:
        print(i)
#endregion

#region Exercicio 04 - Faça um programa para calcular a soma dos números de 1 a 100. Utilize a função range() para criar a coleção de números. 
# print("Exercicio 04 - Faça um programa para calcular a soma dos números de 1 a 5. Utilize a função range() para criar a coleção de números.")
# soma = 0
# for i in range(1,6):
#     print(i)
#     soma+=i
# print(soma)
#endregion

#region Exercicio 05 - Faça um programa para calcular a média de 4 números digitados.
# print("Exercicio 05 - Faça um programa para calcular a média de 4 números digitados.")
# soma = 0

# for i in range(4): 
#     num = int(input("Numero : "))
#     soma+=num
# print(soma)
# print(soma/i)
# soma = 0
# for i in range(1,11):
#     numero = float(input(f"Digite o {i}º número: "))
#     soma = soma + numero

# media = soma / 10

# print(f"A média dos números é {media}")

#endregion

#region Exercicio 06 - Faça um programa para verificar se um número é primo. Utilize a condicional IF dentro do laço FOR. 
# print("Exercicio 06 - Faça um programa para verificar se um número é primo. Utilize a condicional IF dentro do laço FOR")
# num = int(input("Numero: "))

# for i in range(2,(num+1)):
#     if (num/i) %2 !=0: 
#         print(f"{num} é primo")
#endregion

#region Exercicio 07 - Faça um programa para Imprimir os caracteres de uma string separadamente. 
# print("Exercicio 07 - Faça um programa para Imprimir os caracteres de uma string separadamente")
# digit = str(input("Digite: "))

# for i in digit:
#     print(i)
#endregion

#region Exercicio 08 - Faça um programa para contar quantas vogais existem em uma palavra. Utilize a condicional IF dentro do laço FOR. 
print("Exercicio 08 - Faça um programa para contar quantas vogais existem em uma palavra. Utilize a condicional IF dentro do laço FOR")
digit = str(input("Digite: "))
qtde = 0

for i in "aeiou":
        # i=+1
        qtde=+1

print(i)
#endregion

#region Exercicio 0 
# print("Exercicio 0")
# for i in range(2,21,2):
#     print(i)
#endregion