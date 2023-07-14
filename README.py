lista_produtos = []
relatorio_vendas = []


def ler_produtos():
    with open("produtos_cadastrados.txt", "r", encoding="utf-8") as produtos:
        produto = {}
        for linha in produtos:
            if linha.strip():
                chave, valor = linha.strip().split(" - ")
                if chave == "codigo" or chave == "estoque":
                    valor = int(valor)
                elif chave == "preço":
                    valor = float(valor)
                produto[chave] = valor
            else:
                if produto:
                    lista_produtos.append(produto)
                    produto = {}
        if produto:
            lista_produtos.append(produto)


def cadastro_produtos(nome, codigo, estoque, preco):
    lista_produtos.append({"nome": nome, "codigo": codigo, "estoque": estoque, "preço": preco})


def salva_produtos():
    with open("produtos_cadastrados.txt", "w", encoding="utf-8") as produtos:
        for produto in lista_produtos:
            for chave, valor in produto.items():
                produtos.write(chave + " - " + str(valor) + "\n")
            produtos.write("\n")


def relatorio_txt():
    with open("relatorio_vendas.txt", "w", encoding="utf-8") as relatorio_vendass:
        relatorio_vendass.write("Relatório de Vendas\n")
        relatorio_vendass.write("-------------------\n")
        for venda in relatorio_vendas:
            relatorio_vendass.write("Produto: " + venda["produto"]["nome"] + "\n")
            relatorio_vendass.write("Quantidade: " + str(venda["quantidade"]) + "\n")
            relatorio_vendass.write("Valor Total: " + str(venda["valor_total"]) + "\n")
            relatorio_vendass.write("-------------------\n")


def editar(nome):
    print("1 - para alterar o código\n2 - para alterar o estoque\n3 - para alterar o preço")
    op = int(input("Digite a sua opção: "))
    produto_encontrado = False
    for produto in lista_produtos:
        if produto["nome"] == nome:
            produto_encontrado = True
            if op == 1:
                novo_codigo = int(input("Digite o novo código: "))
                produto["codigo"] = novo_codigo
                salva_produtos()
                print("Código alterado com sucesso!")
            elif op == 2:
                novo_estoque = int(input("Digite o novo estoque: "))
                produto["estoque"] = novo_estoque
                salva_produtos()
                print("Estoque alterado com sucesso!")
            elif op == 3:
                novo_preco = float(input("Digite o novo preço: "))
                produto["preço"] = novo_preco
                salva_produtos()
                print("Preço alterado com sucesso!")
            else:
                print("Opção inválida!")
            break
    if not produto_encontrado:
        print("Produto não encontrado")


def remover():
    pesquisa_produto = input("Digite o nome do produto: ")

    for i in range(len(lista_produtos) - 1, -1, -1):
        if pesquisa_produto == lista_produtos[i]["nome"]:
            lista_produtos.pop(i)
            print("Produto removido com sucesso!")
            salva_produtos()
            break
    else:
        print("O produto não foi encontrado")


def comprar(nome):
    quantidade = int(input("Quantidade de itens que deseja comprar: "))
    produto_encontrado = False
    for produto in lista_produtos:
        if nome == produto["nome"]:
            produto_encontrado = True
            if quantidade <= produto["estoque"]:
                valor_total = quantidade * produto["preço"]
                produto["estoque"] -= quantidade
                print("Compra realizada com sucesso!")
                relatorio_vendas.append({"produto": produto, "quantidade": quantidade, "valor_total": valor_total})
                salva_produtos()
                break
            else:
                print("Produto sem estoque")
    if not produto_encontrado:
        print("Produto não encontrado")


ler_produtos()

while True:
    print("     MENU DE OPÇÕES.    ")
    print("1 - Para cadastrar um novo produto")
    print("2 - Para mostrar todos os produtos")
    print("3 - Para editar dados do produto")
    print("4 - Para remover produto")
    print("5 - Para comprrar")
    print("6 - Relatório de vendas")
    print("7 - Sair")
    op = int(input("Digite a opção: "))

    if op == 1:
        nome = input("Informe o nome do produto: ")
        codigo = int(input("Digite o código do produto: "))
        estoque = int(input("Quantidade em estoque do produto: "))
        preco = float(input("Informe o preço do produto: "))

        cadastro_produtos(nome, codigo, estoque, preco)
        salva_produtos()

    elif op == 2:
        print("Produtos cadastrados:")
        for produto in lista_produtos:
            print("Nome:", produto["nome"])
            print("Código:", produto["codigo"])
            print("Estoque:", produto["estoque"])
            print("Preço:", produto["preço"])
            print()

    elif op == 3:
        pesquisa_produto = input("Informe o nome do produto que deseja editar: ")
        editar(pesquisa_produto)

    elif op == 4:
        remover()

    elif op == 5:
        pesquisa_produto = input("Informe o nome do produto que deseja comprar: ")
        comprar(pesquisa_produto)

    elif op == 6:
        relatorio_txt()
        print("Relatório de vendas gerado com sucesso!")

    elif op == 7:
        break

    else:
        print("Opção inválida!")
