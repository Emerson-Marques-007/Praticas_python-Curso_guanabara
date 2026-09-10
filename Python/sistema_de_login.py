def menu():
    print('[1] - Cadastrar')
    print('[2] - Login')
    print('[3] - Sair')

    opcao = int(input('Digite um número: '))
    return opcao

def cadastrar():
    cadastros = {
        'usuario' : input('Cadastre o seu usuario: '),
        'senha' : input('Cadastre a senha: ')
    }

    usuario_correto = cadastros['usuario']
    senha_correta = cadastros['senha']

    return usuario_correto, senha_correta

def login(usuario_correto, senha_correta):

    tentativas = 3

    while tentativas > 0:
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')

        if usuario == usuario_correto and senha == senha_correta:
            print(f'Login, Realizado com Sucesso! \nBem Vindo! {usuario}')
            break
        else:
            tentativas -= 1

            if tentativas > 0:
                print(
                    f'Usuário ou senha incorretos! '
                    f'Você tem mais {tentativas} tentativa(s).'
                )
            else:
                print('Acesso bloqueado! Você esgotou suas 3 tentativas.')


usuario = ""
senha = ""

while True:

    opcao = menu()

    if opcao == 1:
        usuario, senha = cadastrar()
        print('Cadastro Realizado com sucesso!')
    elif opcao == 2:
        if usuario == "" or senha == "":
            print('Nenhum Cadastro encontrado')
        else:
            login(usuario, senha)
    elif opcao == 3:
        print('Fim do Programa!')
        break
    else:
        print('Opção invalida!')
