# print("Numero de 1 a 10 com for e com while")
# n=1
# print("Numeros de 1 a 10 com for")
# for n in range (1,10):
#     print(n)

# n=1
# print("Numeros de 1 a 10 com while")
# while n <= 10:
#     print(n)
#     n = n+1

# print("===============================================")
# print("Numeros de 1 a 100  com for e com while dezenas")
# n=10

# print("Numeros de 1 a 100 com for")
# for n in range (0,101,10):
#     print(n)

# n=10
# print("Numeros de 1 a 100 com while")
# while n <= 100:
#     print(n)
#     n = n+10

# print("===============================================")
# print("Numeros de 1 a 100  com for e com while dezenas")
# n=10

# print("Numeros de 1 a 100 com for")
# for n in range (0,101):
#     if n%10==0:
#         print(n)

# n=10
# print("Numeros de 1 a 100 com while")
# while n <= 100:
#     if n%10==0:
#         print(n)
#         n = n+10

# print("===============================================")
# print("peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.")

# nota = float(input("Digite uma nota de o a 10: "));

# while True:
#     if   0 <= nota <= 10:
#         print("Nota : ", nota)
#         break
#     else:
#         nota = float(input("Nota invalida. Digite uma nota de o a 10: "));


# print("===============================================")
# print("leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.")

# nome = str(input("Digite um nome: "));
# senha = str(input("Digite um senha: "));

# while True:
#     if   senha != nome:
#         print("\nNome : ", nome)
#         print("Senha : ", senha)
#         break
#     else:
#         print("\nNome igual a senha. ");
#         nome = str(input("Digite novamente: "));
#         senha = str(input("Digite novamente: "));

# print("===============================================")
# print("leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.")

# while True:
#     nome = input("Digite um nome: ");
#     senha = input("Digite um senha: ");
#     if   senha != nome:
#         print("\nNome : ", nome)
#         print("Senha : ", senha)
#         break
#     else:
#         print("\nNome igual a senha. ");

# print("===============================================")
# print("leia e valide as seguintes informações:\n",
#       "Nome: maior que 3 caracteres; \n",
#       "Idade: entre 0 e 150; \n",
#       "Salário: maior que zero; \n",
#       "Sexo: 'f' ou 'm'; \n",
#       "Estado Civil: 's', 'c', 'v', 'd';\n")

# while True:
#     while True:
#         nome = str(input("Digite um nome (maior que 3 caracteres) : "));
#         if len(nome) > 3:
#             break
#         else:
#             print("Idade invalida. \n");

#     while True:
#         idade = int(input("Digite Idade (entre 0 e 150) : "));
#         if  0>= idade <=150:
#             break
#         else:
#             print("\n Idade invalido. ")

#     while True:
#         salario = float(input("Digite Salário (maior que zero) : "));
#         if  salario >=0:
#             break
#         else:
#             print("\n salario invalido. ")

#     while True:
#         sexo = str(input("Digite Sexo ('f' ou 'm') : ")).lower;
#         if  len(sexo)!=1 or sexo !="f" and sexo !="f":
#             break
#         else:
#             print("\n sexo invalido. ")

#     while True:
#         estCivil = str(input("Digite Estado Civil ('s', 'c', 'v', 'd'): ")).lower;
#         if len(estCivil) or estCivil in "scvd":
#             break
#         else:
#             print("\nEstado civil invalido ")


#     print("\n Nome: ",nome );
#     print("\n idade: ",idade );
#     print("\n salario: ",salario );
#     print("\n sexo: ",sexo );
#     print("\n Estado Civil: ",estCivil );
    
print("===============================================")
print("Desafio\n")

venda=[];
codigo=1;
while True:
    while codigo <= 7:
    fazerVenda = str(input("Quer cadastrar uma venda(s/n) ? "));
    if len(fazerVenda) ==1 and fazerVenda=="s":
        nome=str(input("Digite nome: "));
        telefone=int(input("Digite telefone: "));
        endereco=input("Digite endereco: ");
        venda1 =[
            codigo, nome , telefone, endereco 
        ]
        codigo=codigo+1;
         break
    else:
        print("Idade invalida. \n");
    print(venda);

