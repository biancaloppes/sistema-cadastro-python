clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o email do cliente: ")

    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"Cliente {i}")
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"Email: {cliente['email']}")
            print("-" * 20)

while True:
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.\n")
