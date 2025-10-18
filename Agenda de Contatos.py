#REGRAS
#Adicionar contatos
#Listar contatos
#Buscar contatos pelo nome
#Remover contato
#Sair do programa

#Olá mundo

def addContato(contatos):
    nome = input("Digite o nome da pessoa: ").title()
    while True:
        try:
            ddd = int(input("Digite o DDD: "))
            numero = int(input("Digite o número de celular: "))
        except ValueError:
            print("Erro, tente novamente. Digite apenas números")
            continue
        break
    obs = input("Campo reservado para observação: ")        
    novoCaderno={
    "Nome" : nome,
    "DDD" : ddd,
    "Número" : numero,
    "Observação" : obs    
    }
    print(f"O contato de {nome}, ({ddd}) {numero} foi adicionado com sucesso!")
    contatos.append(novoCaderno)
    return contatos
    
def listarContato(contatos):
    if not contatos:
        print("Não há contatos nessa agenda!")
    else:
        for indice, lista in enumerate(contatos, start=1):
            print(f"{indice} - Nome: {lista['Nome']}, CELL: ({lista['DDD']})  {lista['Número']}, Observação: {lista['Observação']}")
            
def buscarContato(contatos):
    if not contatos:
        print("Não há contatos nessa agenda!")
    if contatos == True:
        nome = input("Digite o nome da pessoa que deseja encontrar: ").title()
        encontrado = False
        for lista in contatos:
            if lista['Nome'] == nome:
                print("Contato encontrado com sucesso!")
                print(f"Nome: {lista['Nome']}, CELL: ({lista['DDD']})  {lista['Número']}, Observação: {lista['Observação']}")
                encontrado = True
                break
        if not encontrado:
            print("Não existe essa pessoa na agenda")
            
def deleteContato(contatos):
    if not contatos:
        print("Não há contatos nessa agenda!")
    if contatos == True:
        nome = input("Digite o nome da pessoa que deseja encontrar: ").title()
        encontrado = False
        for lista in contatos:
            if lista['Nome'] == nome:
                contatos.remove(lista)
                print(f"Contato de {nome} foi excluído com sucesso")
                encontrado = True
                break
        if not encontrado:
            print("Não existe essa pessoa na agenda")


        
cadernoContatos = []
usuario = input("Digite seu nome: ").title()
print(f"Seja bem-vindo {usuario}")

while True:
    print("\n ---MENU---")
    print("1 - Adicionar contatos")
    print("2 - Listar todos contatos")
    print("3 - Buscar pelo nome")
    print("4 - Deletar contatos")
    print("5 - Sair")
    
    try:
        opcao = int(input("Digite a opção que voce desejar ultilizar: "))
    except ValueError:
        print("Digite um número.")
        continue
    opcoes ={
    1 : addContato,
    2 : listarContato,
    3 : buscarContato,
    4 : deleteContato    
    }
    
    if opcao == 5:
        print("Saindo... até logo!")
        exit()
    if not opcao in opcoes:
        print("Erro, não existe essa opção. Tente novamente!")
    else:
        opcoes[opcao](cadernoContatos)