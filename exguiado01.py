# ========== PYTHON ==========

produtos = []
print("Cadastro de produtos do supermercado BomPreço\n")
for i in range(3):
    nome = input(f"Nome do produto {i+1}: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))

produto = {"nome": nome, "categoria": categoria, "preco": preco}
produtos.append(produto)
consulta = input("\nDigite o nome do produto para consultar: ")
encontrado = False

for p in produtos:
    if p.get("nome") == consulta:
        print("\nProduto encontrado:")
        print(f"Nome: {p.get('nome')}")
        print(f"Categoria: {p.get('categoria')}")
        print(f"Preço: R$ {p.get('preco')}")
        encontrado = True

if not encontrado:
    print("Produto não encontrado.")