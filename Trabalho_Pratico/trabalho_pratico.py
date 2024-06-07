import csv
from tabulate import tabulate

# Estruturas de Dados
usuarios = {}
produtos = []
servicos = []

# Funções para manipulação de arquivos
def carregar_usuarios():
    try:
        with open('usuarios.csv', 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                id = int(linha['id'])
                usuarios[id] = {"nome": linha['nome'], "senha": linha['senha'], "permissao": linha['permissao']}
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Nenhum usuário carregado.")

def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome', 'senha', 'permissao'])
        for id, dados in usuarios.items():
            escritor.writerow([id, dados['nome'], dados['senha'], dados['permissao']])

def carregar_produtos():
    try:
        with open('produtos.csv', 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                produto = {"codigo": int(linha['codigo']), "nome": linha['nome'], "preco": float(linha['preco']), "quantidade": int(linha['quantidade'])}
                produtos.append(produto)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Nenhum produto carregado.")

def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['codigo', 'nome', 'preco', 'quantidade'])
        for produto in produtos:
            escritor.writerow([produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']])

def carregar_servicos():
    try:
        with open('servicos.csv', 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                servico = {"codigo": int(linha['codigo']), "nome": linha['nome'], "preco": float(linha['preco']), "duracao": linha['duracao']}
                servicos.append(servico)
    except FileNotFoundError:
        print("Arquivo de serviços não encontrado. Nenhum serviço carregado.")

def salvar_servicos():
    with open('servicos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['codigo', 'nome', 'preco', 'duracao'])
        for servico in servicos:
            escritor.writerow([servico['codigo'], servico['nome'], servico['preco'], servico['duracao']])

# Funções de Usuários
def buscar_usuario(id=None, nome=None):
    for uid, usuario in usuarios.items():
        if (id is not None and uid == id) or (nome is not None and usuario['nome'] == nome):
            cabecalhos = ["ID", "Nome", "Permissão"]
            tabela_usuarios = [[uid, usuario['nome'], usuario['permissao']] ]
            print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
            return
    print("Usuario não encontrado.")

def adicionar_usuario(id, nome, senha, permissao):
    if id in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[id] = {"nome": nome, "senha": senha, "permissao": permissao}
        salvar_usuarios()
        print("Usuario adicionado com sucesso!")

def listar_usuarios():
    cabecalhos = ["ID", "Nome", "Permissão"]
    tabela_usuarios = [[id, dados['nome'], dados['permissao']] for id, dados in usuarios.items()]
    print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))

def atualizar_usuario(id, nome=None, senha=None, permissao=None):
    if id in usuarios:
        
        if nome:
            usuarios[id]['nome'] = nome
        if senha:
            usuarios[id]['senha'] = senha
        if permissao:
            usuarios[id]['permissao'] = permissao
        salvar_usuarios()
        print("Dados do usuario atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def remover_usuario(id):
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios()
        print("Dados do usuario removido com sucesso!")
    else:
        print("Usuário não encontrado.")

# Funções de Produtos 
def adicionar_produto(codigo, nome, preco, quantidade):
    for produto in produtos:
        if produto['codigo'] == codigo:
            print("Produto já existe.")
            return
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos()
    print("Produto adicionado com sucesso!")

def listar_produtos():
    cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
    tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']] for produto in produtos]
    print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))

def atualizar_produto(codigo, nome=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto['codigo'] == codigo:
            if nome:
                produto['nome'] = nome
            if preco:
                produto['preco'] = preco
            if quantidade:
                produto['quantidade'] = quantidade
            salvar_produtos()
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def remover_produto(codigo):
    global produtos
    produtos = [produto for produto in produtos if produto['codigo'] != codigo]
    salvar_produtos()
    print("Produto removido com sucesso!")

def buscar_produto(codigo=None, nome=None):
    for produto in produtos:
        if (codigo and produto['codigo'] == codigo) or (nome and produto['nome'] == nome):
            cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
            tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
            print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
            return
    print("Produto não encontrado.")

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
    tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']] for produto in produtos_ordenados ]
    print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])
    cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
    tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']] for produto in produtos_ordenados ]
    print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))

def vender_produto(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
            tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
            print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
            print("\nO produto está correto?")
            print("1. Sim")
            print("2. Não")
            p_c = int(input("Digite uma opção: "))
            if p_c == 1:
                quantidade = int(input("Quantidade vendida: "))
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    salvar_produtos()
                    print(f"\nVenda realizada com sucesso! Restam {produto['quantidade']} unidades do produto '{produto['nome']}'.")
                else:
                    print("Quantidade insuficiente em estoque.")
            return
    print("Produto não encontrado.")

# Função para verificar nomes iguais e somar quantidades
def verificar_e_somar_produtos():
    nome_to_produto = {}
    produtos_para_remover = []
    
    for produto in produtos:
        nome = produto["nome"]
        if nome in nome_to_produto:
            cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
            tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
            print("Produto duplicado:")
            print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
        if nome in nome_to_produto:
            produto_existente = nome_to_produto[nome]
            produto_existente["quantidade"] += produto["quantidade"]
            produtos_para_remover.append(produto)
        else:
            nome_to_produto[nome] = produto
    
    for produto in produtos_para_remover:
        produtos.remove(produto)
    
    salvar_produtos()
    print("Produtos duplicados verificados e somados.")

# Funções de Serviços 
def adicionar_servico(codigo, nome, preco, duracao):
    for servico in servicos:
        if servico['codigo'] == codigo:
            print("Serviço já existe.")
            return
    servicos.append({"codigo": codigo, "nome": nome, "preco": preco, "duracao": duracao})
    salvar_servicos()
    print("Serviço adicionado com sucesso!")

def listar_servicos():
    cabecalhos = ["Código", "Nome", "Preço", "Duração"]
    tabela_servicos = [[servico['codigo'], servico['nome'], servico['preco'], servico['duracao']] for servico in servicos]
    print(tabulate(tabela_servicos, headers=cabecalhos, tablefmt="pretty"))

def atualizar_servico(codigo, nome=None, preco=None, duracao=None):
    for servico in servicos:
        if servico['codigo'] == codigo:
            if nome:
                servico['nome'] = nome
            if preco:
                servico['preco'] = preco
            if duracao:
                servico['duracao'] = duracao
            salvar_servicos()
            print("Serviço atualizado com sucesso!")
            return
    print("Serviço não encontrado.")

def remover_servico(codigo):
    global servicos
    servicos = [servico for servico in servicos if servico['codigo'] != codigo]
    salvar_servicos()
    print("Serviço removido com sucesso!")

def buscar_servico(codigo=None, nome=None):
    for servico in servicos:
        if (codigo and servico['codigo'] == codigo) or (nome and servico['nome'] == nome):
            # Definindo os cabeçalhos da tabela
            cabecalhos = ["Código", "Nome", "Preço", "Duração"]
            # Convertendo a lista de dicionários em uma lista de listas
            tabela_servicos = [[servico['codigo'], servico['nome'], servico['preco'], servico['duracao']]]
            # Imprimindo a tabela
            print(tabulate(tabela_servicos, headers=cabecalhos, tablefmt="pretty"))
            return
    print("Serviço não encontrado.")

# Autenticar usuários
def autenticar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    
    for usuario in usuarios.values():
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo, {nome}!")
            print(f"Sua permissão é: {usuario['permissao']}")
            return usuario['permissao']
    
    print("Usuário ou senha incorretos. Tente novamente.")
    return None

def liberar_acesso(permissao):
    if permissao == "administrador":
        menu_administrador()
    elif permissao == "funcionario":
        menu_funcionario()
    elif permissao == "estagiario":
        menu_estagiario()
    elif permissao == "cliente":
        menu_cliente()
    else:
        print("Permissão desconhecida.")

def menu_cliente():
    while True:
        print("Esses são os serviços disponibilizados pela nossa empresa:")
        print("\n1. Buscar produtos")
        print("2. Buscar serviços")
        print("3. Ver lista de produtos")
        print("4. Ver lista de serviços")
        print("5. Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            print("Saindo...")
            break
        executar_opcao_cliente(opcao)


def menu_administrador():
    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Serviços")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        executar_opcao_administrador(opcao)
        if opcao == '4':
            print("Saindo...")
            break
    
def menu_funcionario():
    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Serviços")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        executar_opcao_funcionario(opcao)
        if opcao == '4':
            print("Saindo...")
            break
        

def menu_estagiario():
    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Serviços")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        executar_opcao_estagiario(opcao)
        if opcao == '4':
            print("Saindo...")
            break
    

def executar_opcao_cliente(opcao):
    if opcao == 1:
        buscar_produto(nome=input("Digite o nome do produto: "))
    elif opcao == 2:
        buscar_servico(nome=input("Digite o nome do serviço: "))
    elif opcao == 3:
        listar_produtos()
    elif opcao == 4:
        listar_servicos()
    else:
        print("Opção inválida!")

def executar_opcao_administrador(opcao):
    if opcao == '1':
        menu_usuarios()
    elif opcao == '2':
        menu_produtos()
    elif opcao == '3':
        menu_servicos()
    else:
        print("Opção inválida!")

def menu_usuarios():
    while True:
        print("\n1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Remover Usuário")
        print("5. Buscar Usuário")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            id = int(input("ID: "))
            nome = input("Nome: ")
            senha = input("Senha: ")
            permissao = input("Permissão: ")
            adicionar_usuario(id, nome, senha, permissao)
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            id = int(input("ID: "))
            cabecalhos = ["ID", "Nome", "Permissão"]
            tabela_usuarios = [[id, usuarios[id]['nome'], usuarios[id]['permissao']] ]
            print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
            nome = input("\nNovo Nome (deixe em branco para manter): ")
            senha = input("Nova Senha (deixe em branco para manter): ")
            permissao = input("Nova Permissão (deixe em branco para manter): ")
            atualizar_usuario(id, nome, senha, permissao)
        elif opcao == '4':
            id = int(input("ID: "))
            cabecalhos = ["ID", "Nome", "Permissão"]
            tabela_usuarios = [[id, usuarios[id]['nome'], usuarios[id]['permissao']] ]
            print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
            print("Deseja remover o usuario?")
            print("1. Sim")
            print("2. Não")
            r_user = int(input("Digite uma opção: "))
            if r_user == 1:
                remover_usuario(id)
        elif opcao == '5':
            criterio = input("Buscar por (1) ID ou (2) Nome? ")
            if criterio == '1':
                id = int(input("ID: "))
                buscar_usuario(id=id)
            elif criterio == '2':
                nome = input("Nome: ")
                buscar_usuario(nome=nome)
        elif opcao == '6':
            break
        else:
            print("Opção inválida!")

def menu_produtos():
    while True:
        print("\n1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Ordenar Produtos por Nome")
        print("7. Ordenar Produtos por Preço")
        print("8. Vender Produto")
        print("9. Verificar duplicatas de Produto")
        print("10. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(codigo, nome, preco, quantidade)
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            codigo = int(input("Código: "))
            for produto in produtos:
                if produto['codigo'] == codigo:
                    cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
                    tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
                    print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
                    print("\nO produto está correto?")
                    print("1. Sim")
                    print("2. Não")
                    p_a = int(input("Digite uma opção: "))
                    if p_a == 1:
                        nome = input("Novo Nome (deixe em branco para manter): ")
                        preco = input("Novo Preço (deixe em branco para manter): ")
                        quantidade = input("Nova Quantidade (deixe em branco para manter): ")
                        atualizar_produto(codigo, nome, float(preco) if preco else None, int(quantidade) if quantidade else None)
        elif opcao == '4':
            codigo = int(input("Código: "))
            remover_produto(codigo)
        elif opcao == '5':
            criterio = input("Buscar por (1) Código ou (2) Nome? ")
            if criterio == '1':
                codigo = int(input("Código: "))
                buscar_produto(codigo=codigo)
            elif criterio == '2':
                nome = input("Nome: ")
                buscar_produto(nome=nome)
        elif opcao == '6':
            ordenar_produtos_por_nome()
        elif opcao == '7':
            ordenar_produtos_por_preco()
        elif opcao == '8':
            codigo = int(input("Código: "))
            vender_produto(codigo)
        elif opcao == '9':
            verificar_e_somar_produtos()
        elif opcao == '10':
            break
        else:
            print("Opção inválida!")

def menu_servicos():
    while True:
        print("\n1. Adicionar Serviço")
        print("2. Listar Serviços")
        print("3. Atualizar Serviço")
        print("4. Remover Serviço")
        print("5. Buscar Serviço")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            duracao = input("Duração: ")
            adicionar_servico(codigo, nome, preco, duracao)
        elif opcao == '2':
            listar_servicos()
        elif opcao == '3':
            codigo = int(input("Código: "))
            nome = input("Novo Nome (deixe em branco para manter): ")
            preco = input("Novo Preço (deixe em branco para manter): ")
            duracao = input("Nova Duração (deixe em branco para manter): ")
            atualizar_servico(codigo, nome, float(preco) if preco else None, duracao)
        elif opcao == '4':
            codigo = int(input("Código: "))
            remover_servico(codigo)
        elif opcao == '5':
            criterio = input("Buscar por (1) Código ou (2) Nome? ")
            if criterio == '1':
                codigo = int(input("Código: "))
                buscar_servico(codigo=codigo)
            elif criterio == '2':
                nome = input("Nome: ")
                buscar_servico(nome=nome)
        elif opcao == '6':
            break
        else:
            print("Opção inválida!")
    
        print("Opção inválida.")

def executar_opcao_funcionario(opcao):
    if opcao == '1':
        while True:
            print("\n1. Adicionar Usuário")
            print("2. Listar Usuários")
            print("3. Atualizar Usuário")
            print("4. Remover Usuário")
            print("5. Buscar Usuário")
            print("6. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                id = int(input("ID: "))
                nome = input("Nome: ")
                senha = input("Senha: ")
                permissao = input("Permissão: ")
                adicionar_usuario(id, nome, senha, permissao)
            elif opcao == '2':
                listar_usuarios()
            elif opcao == '3':
                id = int(input("ID: "))
                cabecalhos = ["ID", "Nome", "Permissão"]
                tabela_usuarios = [[id, usuarios[id]['nome'], usuarios[id]['permissao']] ]
                print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
                nome = input("\nNovo Nome (deixe em branco para manter): ")
                senha = input("Nova Senha (deixe em branco para manter): ")
                permissao = input("Nova Permissão (deixe em branco para manter): ")
                atualizar_usuario(id, nome, senha, permissao)
            elif opcao == '4':
                id = int(input("ID: "))
                cabecalhos = ["ID", "Nome", "Permissão"]
                tabela_usuarios = [[id, usuarios[id]['nome'], usuarios[id]['permissao']] ]
                print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
                print("Deseja remover o usuario?")
                print("1. Sim")
                print("2. Não")
                r_user = int(input("Digite uma opção: "))
                if r_user == 1:
                    remover_usuario(id)
            elif opcao == '5':
                criterio = input("Buscar por (1) ID ou (2) Nome? ")
                if criterio == '1':
                    id = int(input("ID: "))
                    buscar_usuario(id=id)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_usuario(nome=nome)
            elif opcao == '6':
                break
            else:
                print("Opção inválida!")
    elif opcao == '2':
        while True:
            print("\n1. Adicionar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Buscar Produto")
            print("6. Ordenar Produtos por Nome")
            print("7. Ordenar Produtos por Preço")
            print("8. Vender Produto")
            print("9. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                codigo = int(input("Código: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                adicionar_produto(codigo, nome, preco, quantidade)
            elif opcao == '2':
                listar_produtos()
            elif opcao == '3':
                codigo = int(input("Código: "))
                for produto in produtos:
                    if produto['codigo'] == codigo:
                        cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
                        tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
                        print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
                        print("\nO produto está correto?")
                        print("1. Sim")
                        print("2. Não")
                        p_a = int(input("Digite uma opção: "))
                        if p_a == 1:
                            nome = input("Novo Nome (deixe em branco para manter): ")
                            preco = input("Novo Preço (deixe em branco para manter): ")
                            quantidade = input("Nova Quantidade (deixe em branco para manter): ")
                            atualizar_produto(codigo, nome, float(preco) if preco else None, int(quantidade) if quantidade else None)
            elif opcao == '4':
                codigo = int(input("Código: "))
                remover_produto(codigo)
            elif opcao == '5':
                criterio = input("Buscar por (1) Código ou (2) Nome? ")
                if criterio == '1':
                    codigo = int(input("Código: "))
                    buscar_produto(codigo=codigo)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_produto(nome=nome)
            elif opcao == '6':
                ordenar_produtos_por_nome()
            elif opcao == '7':
                ordenar_produtos_por_preco()
            elif opcao == '8':
                codigo = int(input("Código: "))
                vender_produto(codigo)
            elif opcao == '9':
                break
            else:
                print("Opção inválida!")
    elif opcao == '3':
        while True:
            print("\n1. Adicionar Serviço")
            print("2. Listar Serviços")
            print("3. Atualizar Serviço")
            print("4. Remover Serviço")
            print("5. Buscar Serviço")
            print("6. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                codigo = int(input("Código: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                duracao = input("Duração: ")
                adicionar_servico(codigo, nome, preco, duracao)
            elif opcao == '2':
                listar_servicos()
            elif opcao == '3':
                codigo = int(input("Código: "))
                nome = input("Novo Nome (deixe em branco para manter): ")
                preco = input("Novo Preço (deixe em branco para manter): ")
                duracao = input("Nova Duração (deixe em branco para manter): ")
                atualizar_servico(codigo, nome, float(preco) if preco else None, duracao)
            elif opcao == '4':
                codigo = int(input("Código: "))
                remover_servico(codigo)
            elif opcao == '5':
                criterio = input("Buscar por (1) Código ou (2) Nome? ")
                if criterio == '1':
                    codigo = int(input("Código: "))
                    buscar_servico(codigo=codigo)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_servico(nome=nome)
            elif opcao == '6':
                break
            else:
                print("Opção inválida!")
    else:
        print("Opção inválida!")
        
def executar_opcao_estagiario(opcao):
    if opcao == '1':
        while True:
            print("\n1. Adicionar Usuário")
            print("2. Listar Usuários")
            print("3. Atualizar Usuário")
            print("4. Buscar Usuário")
            print("5. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                id = int(input("ID: "))
                nome = input("Nome: ")
                senha = input("Senha: ")
                permissao = input("Permissão: ")
                adicionar_usuario(id, nome, senha, permissao)
            elif opcao == '2':
                listar_usuarios()
            elif opcao == '3':
                id = int(input("ID: "))
                cabecalhos = ["ID", "Nome", "Permissão"]
                tabela_usuarios = [[id, usuarios[id]['nome'], usuarios[id]['permissao']] ]
                print(tabulate(tabela_usuarios, headers=cabecalhos, tablefmt="pretty"))
                nome = input("\nNovo Nome (deixe em branco para manter): ")
                senha = input("Nova Senha (deixe em branco para manter): ")
                permissao = input("Nova Permissão (deixe em branco para manter): ")
                atualizar_usuario(id, nome, senha, permissao)
            elif opcao == '4':
                criterio = input("Buscar por (1) ID ou (2) Nome? ")
                if criterio == '1':
                    id = int(input("ID: "))
                    buscar_usuario(id=id)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_usuario(nome=nome)
            elif opcao == '5':
                break
            else:
                print("Opção inválida!")
    elif opcao == '2':
        while True:
            print("\n1. Adicionar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Buscar Produto")
            print("6. Ordenar Produtos por Nome")
            print("7. Ordenar Produtos por Preço")
            print("8. Vender Produto")
            print("9. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                codigo = int(input("Código: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                adicionar_produto(codigo, nome, preco, quantidade)
            elif opcao == '2':
                listar_produtos()
            elif opcao == '3':
                codigo = int(input("Código: "))
                for produto in produtos:
                    if produto['codigo'] == codigo:
                        cabecalhos = ["Código", "Nome", "Preço", "Quantidade"]
                        tabela_produtos = [[produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']]]
                        print(tabulate(tabela_produtos, headers=cabecalhos, tablefmt="pretty"))
                        print("\nO produto está correto?")
                        print("1. Sim")
                        print("2. Não")
                        p_a = int(input("Digite uma opção: "))
                        if p_a == 1:
                            nome = input("Novo Nome (deixe em branco para manter): ")
                            preco = input("Novo Preço (deixe em branco para manter): ")
                            quantidade = input("Nova Quantidade (deixe em branco para manter): ")
                            atualizar_produto(codigo, nome, float(preco) if preco else None, int(quantidade) if quantidade else None)
            elif opcao == '4':
                codigo = int(input("Código: "))
                remover_produto(codigo)
            elif opcao == '5':
                criterio = input("Buscar por (1) Código ou (2) Nome? ")
                if criterio == '1':
                    codigo = int(input("Código: "))
                    buscar_produto(codigo=codigo)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_produto(nome=nome)
            elif opcao == '6':
                ordenar_produtos_por_nome()
            elif opcao == '7':
                ordenar_produtos_por_preco()
            elif opcao == '8':
                codigo = int(input("Código: "))
                vender_produto(codigo)
            elif opcao == '9':
                break
            else:
                print("Opção inválida!")
    elif opcao == '3':
        while True:
            print("\n1. Adicionar Serviço")
            print("2. Listar Serviços")
            print("3. Atualizar Serviço")
            print("4. Buscar Serviço")
            print("5. Voltar")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                codigo = int(input("Código: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                duracao = input("Duração: ")
                adicionar_servico(codigo, nome, preco, duracao)
            elif opcao == '2':
                listar_servicos()
            elif opcao == '3':
                codigo = int(input("Código: "))
                nome = input("Novo Nome (deixe em branco para manter): ")
                preco = input("Novo Preço (deixe em branco para manter): ")
                duracao = input("Nova Duração (deixe em branco para manter): ")
                atualizar_servico(codigo, nome, float(preco) if preco else None, duracao)
            elif opcao == '4':
                criterio = input("Buscar por (1) Código ou (2) Nome? ")
                if criterio == '1':
                    codigo = int(input("Código: "))
                    buscar_servico(codigo=codigo)
                elif criterio == '2':
                    nome = input("Nome: ")
                    buscar_servico(nome=nome)
            elif opcao == '5':
                break
            else:
                print("Opção inválida!")
    else:
        print("Opção inválida!")

# Carregar dados ao iniciar o sistema
carregar_usuarios()
carregar_produtos()
carregar_servicos()

if __name__ == "__main__":
    print("Olá, seja bem-vindo ao sistema da Livraria Acadêmica")
    print("Entre com seu login e senha")
    
    permissao = None
    while permissao is None:
        permissao = autenticar_usuario()

    liberar_acesso(permissao)

