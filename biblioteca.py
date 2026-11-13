def cadastrar_livro(acervo: list, titulo: str, autor: str, ano: int) -> None:
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": "disponível"
    }
    acervo.append(livro)

def emprestar_livro(acervo: list, titulo_busca: str) -> None:
    for livro in acervo:
        if livro["titulo"].lower() == titulo_busca.lower():
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                print(f"Sucesso: O livro '{livro['titulo']}' foi emprestado.")
            else:
                print(f"Aviso: O livro '{livro['titulo']}' já se encontra emprestado.")
            return
    print(f"Erro: Livro '{titulo_busca}' não encontrado no acervo.")


def listar_por_status(acervo: list, status_desejado: str) -> None:
    filtrados = [livro for livro in acervo if livro["status"] == status_desejado]
    print(f"\n--- LIVROS {status_desejado.upper()}S ({len(filtrados)}) ---")
    if not filtrados:
        print("Nenhum livro encontrado nesta categoria.")
    for livro in filtrados:
        print(f"• {livro['titulo']} | Autor: {livro['autor']} ({livro['ano']})")


if __name__ == "__main__":
    biblioteca_leitura_viva = []

    cadastrar_livro(biblioteca_leitura_viva, "Clean Code", "Robert C. Martin", 2008)
    cadastrar_livro(biblioteca_leitura_viva, "Entendendo Algoritmos", "Aditya Bhargava", 2017)
    cadastrar_livro(biblioteca_leitura_viva, "Python Fluente", "Luciano Ramalho", 2015)
    cadastrar_livro(biblioteca_leitura_viva, "Arquitetura Limpa", "Robert C. Martin", 2017)

    emprestar_livro(biblioteca_leitura_viva, "Clean Code")
    emprestar_livro(biblioteca_leitura_viva, "Python Fluente")
    emprestar_livro(biblioteca_leitura_viva, "Clean Code")

    listar_por_status(biblioteca_leitura_viva, "emprestado")
    listar_por_status(biblioteca_leitura_viva, "disponível")