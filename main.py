# Agenda de contatos
agenda = []

def exibir_menu():
    print("\n--- MENU ---")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato por nome")
    print("4. Editar contato")
    print("5. Excluir contato")
    print("6. Sair")

def adicionar_contato():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contato = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    
    agenda.append(contato)
    print(f"Contato de {nome} adicionado com sucesso!")

def listar_contatos():
    if not agenda:
        print("Agenda vazia.")
        return
    
    print("\n--- CONTATOS ---")
    for i, contato in enumerate(agenda):
        print(f"{i + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def buscar_contato():
    nome = input("Digite o nome para buscar: ")
    encontrados = [c for c in agenda if c['nome'].lower() == nome.lower()]
    
    if encontrados:
        for c in encontrados:
            print(f"Nome: {c['nome']}")
            print(f"Endereço: {c['endereco']}")
            print(f"Telefone: {c['telefone']}")
            print(f"Email: {c['email']}")
            print("--------------")
    else:
        print("Contato não encontrado.")

def editar_contato():
    nome = input("Digite o nome do contato a editar: ")
    for contato in agenda:
        if contato['nome'].lower() == nome.lower():
            print("Deixe em branco para manter o valor atual.")
            novo_endereco = input(f"Novo endereço [{contato['endereco']}]: ") or contato['endereco']
            novo_telefone = input(f"Novo telefone [{contato['telefone']}]: ") or contato['telefone']
            novo_email = input(f"Novo email [{contato['email']}]: ") or contato['email']
            
            contato['endereco'] = novo_endereco
            contato['telefone'] = novo_telefone
            contato['email'] = novo_email
            
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato a excluir: ")
    for i, contato in enumerate(agenda):
        if contato['nome'].lower() == nome.lower():
            del agenda[i]
            print("Contato excluído com sucesso!")
            return
    print("Contato não encontrado.")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-6): ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        editar_contato()
    elif opcao == "5":
        excluir_contato()
    elif opcao == "6":
        print("Saindo da agenda. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
