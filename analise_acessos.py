from collections import Counter


def analisar_logs_acesso(logs_usuarios: list[str]) -> None:
    if not logs_usuarios:
        print("Nenhum log registrado.")
        return

    contagem_acessos = Counter(logs_usuarios)
    total_acessos = sum(contagem_acessos.values())

    usuario_top, qtd_top = contagem_acessos.most_common(1)[0]

    print(f"{' RELATÓRIO DE ACESSOS - DATASECURE ':=^48}")
    print(f"Total de acessos registrados : {total_acessos}")
    print(f"Usuário mais ativo           : {usuario_top} ({qtd_top} acessos)")
    print("-" * 48)

    print("RANKING COMPLETO DE ACESSOS:")
    for posicao, (usuario, acessos) in enumerate(contagem_acessos.most_common(), start=1):
        percentual = (acessos / total_acessos) * 100
        print(f"{posicao}º lugar | {usuario:<18} | {acessos:2d} acessos ({percentual:5.1f}%)")
    print("=" * 48)


if __name__ == "__main__":
    logs_sistema = [
        "yuri.santos", "sarah.pessoa", "luis.soeiro", "yuri.santos",
        "marcio.freire", "yuri.santos", "marcus.cunha", "sarah.pessoa",
        "yuri.santos", "luis.soeiro", "ana.lima", "sarah.pessoa"
    ]

    analisar_logs_acesso(logs_sistema)