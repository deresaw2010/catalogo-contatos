# main.py

import contatos

def exibir_menu():
    print("\n--- MENU ---")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato por nome")
    print("4. Editar contato")
    print("5. Excluir contato")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contatos.adicionar_contato(nome, endereco, telefone, email)
            print("Contato adicionado com sucesso!")

        elif opcao == "2":
            lista = contatos.listar_contatos()
            if not lista:
                print("Agenda vazia.")
            else:
                print("\n--- CONTATOS ---")
                for i, c in enumerate(lista):
                    print(f"{i + 1}. {c['nome']} - {c['telefone']} - {c['email']}")

        elif opcao == "3":
            nome = input("Digite o nome para buscar: ")
            resultados = contatos.buscar_contato_por_nome(nome)
            if resultados:
                for c in resultados:
                    print(f"Nome: {c['nome']}")
                    print(f"Endereço: {c['endereco']}")
                    print(f"Telefone: {c['telefone']}")
                    print(f"Email: {c['email']}")
                    print("--------------")
            else:
                print("Contato não encontrado.")

        elif opcao == "4":
            nome = input("Digite o nome do contato a editar: ")
            print("Deixe em branco para manter o valor atual.")
            atual = contatos.buscar_contato_por_nome(nome)
            if not atual:
                print("Contato não encontrado.")
                continue
            contato = atual[0]
            novo_endereco = input(f"Novo endereço [{contato['endereco']}]: ") or contato['endereco']
            novo_telefone = input(f"Novo telefone [{contato['telefone']}]: ") or contato['telefone']
            novo_email = input(f"Novo email [{contato['email']}]: ") or contato['email']

            sucesso = contatos.editar_contato(nome, novo_endereco, novo_telefone, novo_email)
            if sucesso:
                print("Contato atualizado com sucesso.")
            else:
                print("Erro ao atualizar o contato.")

        elif opcao == "5":
            nome = input("Digite o nome do contato a excluir: ")
            if contatos.excluir_contato(nome):
                print("Contato excluído com sucesso!")
            else:
                print("Contato não encontrado.")

        elif opcao == "6":
            print("Saindo da agenda. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
