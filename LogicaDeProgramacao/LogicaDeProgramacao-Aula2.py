#region COMPARA NUMEROS
print("==================================================================================\n")
print("Digite 2 numeros para compara.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    print("IF \n")  
    num1 = input("Digite o primeiro número : ");
    while num1.isnumeric()!=True:
        num1 = input("Não é número. Digite o primeiro número :");
    num2 = input("Digite o segundo número : ");
    while num2.isnumeric()!=True:
        num2 = input("Não é número. Digite o segundo número : ");
    print("")

    if num1 == num2:
        print("Números iguais\n")
    else:
        print("Números diferentes\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region MAIOR DE IDADE
print("==================================================================================\n")
print ("Verificação de maioridade.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("IF\n")
    idade1 = int(input("Digite a idade: "));
    print("")

    if idade1 >= 18:
        print(idade1, " anos. Maior de idade\n")
    else:
        print(idade1, " anos. Menor de idade\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region TESTE NUMERO POSITIVO
print("==================================================================================\n")
print ("Verificação se número é positivo.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("elif\n")
    num3 = int(input("Digite um número: "));
    print("")
    if num3 > 0:
        print(num3," é positivo\n")
    elif num3 < 0:
        print(num3," é negativo\n")
    else:
        print(num3," é nulo\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region TESTE DE COR
print("==================================================================================\n")
print ("Verificação de cor.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("")
    print("elif\n")
    cor = input("Digite uma cor. Digite: VERMELHO, VERDE, AMARELO.").upper().strip();
    print("")
    # O .upper() transforma em maiusculo, e o .lower() em minusculo.
    # O .strip() retira os espaços antes e depois do texto digitado.
    if cor == "VERMELHO":
        print(cor, " - Pare\n")
    elif cor == "VERDE":
        print(cor.upper(), " - Acelera\n")
    elif cor == "AMARELO":
        print(cor.lower(), " - Atenção\n")
    else:
        print("Cor inválida\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Condicionais 1
print("==================================================================================\n")
print ("Verificação de número inteiro de 0 a 10.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("Condicionais\n")
    num4 = input("Digite uma numero inteiro: ");

    print("\n=====================1======================")
    while not num4.isdigit():
        num4 = input("Não é número, ou não é inteiro. Digite uma Numero inteiro :");
    num4=int(num4)
    if num4>=0 and num4 <= 10:
        print(num4, " é numero inteiro e entre 0 a 10.\n")
    else:
        print("Numero inválida - deve ser entre 0 e 10\n")

    print("=====================2======================")
    while True:
        num4 = input("Digite um número inteiro: ")
        if num4.isdigit():
            num4 = int(num4)
            if num4>=0 and num4 <= 10:
                print(num4, " é número inteiro e entre 0 a 10.\n")
            else:
                print(num4, " é número inteiro fora do intervalo de 0 e 10\n")
            break  # Sai do loop, pois um número inteiro foi inserido
        else:
            print("Não é número, ou não é inteiro. Tente novamente.")
    
    print("=====================3======================")        
    num4 = input("Digite um número inteiro: ")
    while num4.isnumeric()!=True :
        num4 = input("Não é número, ou não é inteiro. Digite uma Numero inteiro : ");
    num4=int(num4)
    if num4>=0 and num4 <= 10:
        print(num4, " Numero inteiro e entre 0 a 10.\n")
    else:
        print(num4, " é número inteiro fora do intervalo de 0 e 10\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Condicionais 2
print("==================================================================================\n")
print ("Verificação de S/N.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("Condicionais\n")
    sair = str(input("Deseja sair? (S/N) ")).lower().strip();
    print("")
    if sair == "s" or sair == "n":
        print("Operação válida\n")
        if sair == "s":
            print(f"Digitou {(sair)}. Tchau meu fi, vá com Deus\n")
        else: 
            print(f"Digitou {(sair)}. Continue usando o programa\n")
    else:
        print("Operação inválida\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Condicionais Match
print("==================================================================================\n")
print ("Verificação de cor com Match");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":
    print("Condicionais Match\n")
    cor1 = str(input("Digite um cor [Amarelo | Verde | Vermelho] :")).lower().strip()
    print("")
    match cor1:
        case "vermelho":
            print("Pare sinal ta fechado\n")
        case "verde":
            print("Segue em frente que o sinal ta aberto, vá simbora\n")
        case "amarelo":
            print("Preste atenção que o sinal já vai fechar\n")
        case _:
            print("Cor nula ou inválida\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 01
print("==================================================================================\n")
print("Imprimir o maior Número.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":  
    print("Digite dois números inteiros e imprima o maior deles.\n")
    numEx1_1 = int(input("Digite dois números : "))

    print("Digite 2 numeros para comparar:\n")
    numEx1_1 = int(input("Digite o primeiro número : \n"));
    print("")
    numEx1_2 = int(input("Digite o segundo número : \n"));
    if numEx1_1>numEx1_2:
        print("Numero 1 Maior\n")
    elif numEx1_1<numEx1_2:
        print("Numero 2 Maior\n")
    else:
        print("Numeros iguais\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 02
print("==================================================================================\n")
print("Verificação de valor positivo/negativo");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c":  
    print("Peça um valor e mostre na tela se o valor é positivo ou negativo.\n")
    numEx2 = float(input("Digite um números : "))
    print("")
    if numEx2>0:
        print(numEx2, " é positivo\n")
    elif numEx2<0:
        print(numEx2, " é negativo\n")
    else:
        print("O numero é zero\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 03
print("==================================================================================\n")
print("Verificação de masculino/feminino");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c": 
    print("Verifique se uma letra digitada é 'F' ou 'M' Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.\n")
    letraEx3 = str(input("Digite o sexo (F-Feminino ou M-Masculino) ")).upper().strip()
    print("")
    if letraEx3 == "M":
        print(letraEx3, " - Masculino\n")
    elif letraEx3 == "F":
        print(letraEx3, " - Feminino\n")
    else:
        print("Sexo Inválido\n")
    print("-------------------------")
    if letraEx3 == "f" or letraEx3 == "F":
        print("F - Femenino\n")
    elif letraEx3 == "m" or letraEx3 == "M":
        print("M - Masculino\n")
    else: 
        print("Sexo inválido\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 04
print("==================================================================================\n")
print("Verificação de vogal/consoante");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c": 
    print("Verifique se Faça um Programa que verifique se uma letra digitada é vogal ou consoante.\n")
    letraEx4 = str(input("Digite uma letra : ")).lower().strip()
    print("")

    if len(letraEx4)==1: 
        print("======================================")
        if letraEx4 in "aeiou":
            print("É Vogal\n")
        elif letraEx4 in "bcdfghjklmnpqrstvxywz":
            print("É Consoante\n")
        else:
            print("Nem vobgal nem consoante\n")

        print("======================================")
        print("Considera simbolo consoante")
        if letraEx4 == "a" or letraEx4 == "e" or letraEx4 == "i" or letraEx4 == "o" or letraEx4 == "u":
            print("Vogal\n")
        else:
            print("Nãp é vogal\n")
    else:
        print("Digite apenas 1 letra\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 05
print("==================================================================================\n")
print("Verificação de média de notas aluno");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c": 
    print("")
    print("Faça a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: ○ A mensagem 'Aprovado', se a média alcançada for maior ou igual a sete; ○ A mensagem 'Reprovado', se a média for menor do que sete;○ A mensagem 'Aprovado com Distinção', se a média for igual a dez.\n")
    print("Digite 2 notas :\n")
    nota1Ex5 = float(input("Digite a primeira nota : "));
    print("")
    nota2Ex5 = float(input("Digite a segunda nota : "));
    mediaEx5 = (nota1Ex5+nota2Ex5)/2;
    print("")
    print("Média : ", mediaEx5,"\n")
    print("")

    if mediaEx5<7:
        print("Reprovado\n")
    elif mediaEx5==10:
        print("Aprovado com Distinção\n")
    else:
        print("Aprovado\n")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 06
print("==================================================================================\n")
print("Verificação maior número.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
if pular == "c": 
    print("")
    print("Faça a leia três números e mostre o maior deles.\n")
    num1Ex6 = float(input("Digite o primeiro número: "));
    print("")
    num2Ex6 = float(input("Digite o segundo número: "));
    print("")
    num3Ex6 = float(input("Digite o terceiro número: "));
    print("")
    # print (max(num1Ex6,num2Ex6,num3Ex6));
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 07
print("==================================================================================\n")
print("Verificação menor e maior número.");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c": 
    print("Faça a leia três números e mostre o maior e o menor deles.\n")
    num1Ex7 = float(input("Digite o primeiro número: "));
    print("")
    num2Ex7 = float(input("Digite o segundo número: "));
    print("")
    num3Ex7 = float(input("Digite o terceiro número: "));
    print("")
    maior = max(num1Ex7, num2Ex7, num3Ex7);
    menor = min(num1Ex7, num2Ex7, num3Ex7);
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 08
print("==================================================================================\n")
print("Verificação de produto mais barato");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("")
if pular == "c": 
    print("Diga o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.\n")
    # Solicita o preço de três produtos
    precoProduto1 = float(input("Digite o preço do primeiro produto: "))
    precoProduto2 = float(input("Digite o preço do segundo produto: "))
    precoProduto3 = float(input("Digite o preço do terceiro produto: "))

    # Verifica qual produto é o mais barato
    if precoProduto1 < precoProduto2 and precoProduto1 < precoProduto3:
        produtoMaisBarato = "Produto 1"
        menorPreco = precoProduto1
    elif precoProduto2 < precoProduto1 and precoProduto2 < precoProduto3:
        produtoMaisBarato = "Produto 2"
        menorPreco = precoProduto2
    else:
        produtoMaisBarato = "Produto 3"
        menorPreco = precoProduto3

    # Exibe o resultado
    print(f"Comprar o {produtoMaisBarato}, que custa R${menorPreco:.2f}")

else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 09

print("==================================================================================\n")
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.").lower().strip();
print("Numeros em ordem decrescente");
if pular == "c": 
    print("Digite três números e mostre-os em ordem decrescente.")
    num1Ex9 = float(input("Digite o primeiro número: \n"))
    num2Ex9 = float(input("Digite o segundo número: \n"))
    num3Ex9 = float(input("Digite o terceiro número: \n"))

    print("Com lista:")
    # Cria uma lista com os números e a ordena em ordem decrescente
    numerosEx9 = [num1Ex9, num2Ex9, num3Ex9]
    numerosDecrescenteEx9 = sorted(numerosEx9, reverse=True)
    # Exibe os números em ordem decrescente
    print("Números em ordem decrescente:", numerosDecrescenteEx9,"\n")

    print("Sem lista:")
    # Encontra o número máximo
    maximo = max(num1Ex9, num2Ex9, num3Ex9)
    # Encontra o número mínimo
    minimo = min(num1Ex9, num2Ex9, num3Ex9)
    # O número do meio é aquele que não é o máximo nem o mínimo
    meio = (num1Ex9 + num2Ex9 + num3Ex9) - (maximo + minimo)
    # Exibe os números em ordem decrescente
    print("Números em ordem decrescente : \n", maximo, meio, minimo)

else:
    print("Pulou tarefa\n")
#endregion 

#region Exercicio 10
print("==================================================================================\n")
print("Digite o turno");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular == "c": 
    turno = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno): \n").lower().strip();
    while turno not in "mvn":
        turno = input("Só pode digitar (M-matutino, V-vespertino, N-noturno): \n").lower().strip();
        if turno == "m":
            print("Voce estuda de manhã. Bom Dia!\n")
        elif turno == "v":
            print("Voce estuda de terde. Boa Tarde!\n")
        elif turno == "n":
            print("Voce estuda de noite. Boa Noite!\n")
else:
    print("Pulou tarefa\n")

#endregion 

#region a definir

#endregion 


