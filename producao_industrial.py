import heapq


def adicionar_ordem(fila_producao: list, codigo_peca: str, tempo_estimado: int, prioridade: int) -> None:

    ordem = (prioridade, tempo_estimado, codigo_peca)
    heapq.heappush(fila_producao, ordem)


def processar_todas_ordens(fila_producao: list) -> None:
    mapa_prioridade = {1: "URGENTE", 2: "NORMAL", 3: "BAIXA"}

    print(f"{' FILA DE PRODUÇÃO - METALPRO ':=^55}")
    passo = 1
    while fila_producao:
        prioridade, tempo, codigo = heapq.heappop(fila_producao)
        label_prio = mapa_prioridade.get(prioridade, "DESCONHECIDA")
        print(f"Ordem #{passo} -> Peça: {codigo:<10} | Prioridade: {label_prio:<8} | Tempo Est.: {tempo} min")
        passo += 1
    print("=" * 55)


if __name__ == "__main__":
    heap_metalpro = []

    adicionar_ordem(heap_metalpro, "EIXO-402", tempo_estimado=45, prioridade=2)
    adicionar_ordem(heap_metalpro, "ENGREN-01", tempo_estimado=30, prioridade=1)
    adicionar_ordem(heap_metalpro, "CHAPA-88", tempo_estimado=15, prioridade=2)
    adicionar_ordem(heap_metalpro, "PINO-12", tempo_estimado=10, prioridade=1)
    adicionar_ordem(heap_metalpro, "SUPORTE-05", tempo_estimado=60, prioridade=3)
    adicionar_ordem(heap_metalpro, "VALVULA-09", tempo_estimado=20, prioridade=1)

    processar_todas_ordens(heap_metalpro)