
#region 3 Senha ======================================================================================
# print("\n==================================================================================\n")
# print("Tarefa gravar senha 3 com biblioteca re e retorno de erro");
# pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

# if pular == "c":
#     while True:
#         import re

#         senha = input("Digite sua senha de no máximo 6 dígitos, sendo: 1 letra minúscula, 1 maiúscula, 1 caracter especial, 1 número: ")
#         senhaInvalida = []

#         if not re.search(r"[a-z]", senha): #Verifica se a senha não contém pelo menos uma letra minúscula (de 'a' a 'z'). Se não contiver, o critério é adicionado à lista de critérios não atendidos.
#             senhaInvalida.append("deve conter pelo menos uma letra minúscula")
        
#         if not re.search(r"[A-Z]", senha): #Verifica se a senha não contém pelo menos uma letra maiúscula (de 'A' a 'Z'). Se não contiver, o critério é adicionado à lista de critérios não atendidos.
#             senhaInvalida.append("deve conter pelo menos uma letra maiúscula")
        
#         if not re.search(r"\d", senha):#Verifica se a senha não contém pelo menos um dígito (0-9). Se não contiver, o critério é adicionado à lista de critérios não atendidos.
#             senhaInvalida.append("deve conter pelo menos um dígito")

#         if not re.search(r"[@#$!]", senha): #Verifica se a senha não contém pelo menos um dos caracteres especiais - '@', '#', '$' ou '!'. Se não contiver, o critério é adicionado à lista de critérios não atendidos.
#             senhaInvalida.append("deve conter pelo menos um dos caracteres especiais - '@', '#', '$' ou '!'") 

#         if not len(senha) <= 6:#Verifica se o comprimento da senha tem 6 caracteres. Se não tiver, o critério é adicionado à lista de critérios não atendidos.
#             senhaInvalida.append("deve ter entre 1 e 8 caracteres de comprimento")

#         if not senhaInvalida: #Verifica se a lista senhaInvalida está vazia, ou seja, se a senha atende a todos os critérios.
#             print("Senha válida!")
#             break  # Sai do loop se a senha for válida
#         else:
#             print("Senha inválida. Os critérios não atendidos são:")
#             for crit in senhaInvalida:#Inicia um loop que percorre a lista de critérios não atendidos.
#                 print(f"- A senha {crit}.")#Imprime cada critério não atendido na lista, fornecendo uma mensagem ao usuário sobre quais critérios precisam ser atendidos.
# else:
#     print("Pulou tarefa\n")
#endregion

while True:
    import re

    senha = input("Digite sua senha de no máximo 6 dígitos, sendo: 1 letra minúscula, 1 maiúscula, 1 caracter especial, 1 número: ")

    # Use expressões regulares para verificar a senha
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!])[A-Za-z\d@#$!]{6}$", senha):
        print("\nA senha atende aos critérios especificados.\n")
        break
    else:
        print("\nA senha não atende aos critérios especificados.\n")