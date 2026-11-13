from collections import Counter
import heapq


class SistemaChamadosTechMaster:
    def __init__(self):
        self.heap_chamados = []
        self.contador_setores = Counter()
        self.sequencia_chegada = 0
        self.mapa_prioridades = {
            1: "CRÍTICO",
            2: "ALTO",
            3: "MÉDIO",
            4: "BAIXO"
        }

    def abrir_chamado(self, setor: str, descricao: str, prioridade: int) -> None:
        if prioridade not in self.mapa_prioridades:
            raise ValueError("Prioridade inválida. Use valores de 1 (crítico) a 4 (baixo).")

        self.sequencia_chegada += 1
        chamado_dict = {
            "id": self.sequencia_chegada,
            "setor": setor,
            "descricao": descricao,
            "prioridade": prioridade
        }

        self.contador_setores[setor] += 1

        heapq.heappush(self.heap_chamados, (prioridade, self.sequencia_chegada, chamado_dict))

    def exibir_chamado_mais_urgente(self) -> None:
        if not self.heap_chamados:
            print("Nenhum chamado na fila.")
            return

        _, _, mais_urgente = self.heap_chamados[0]
        prio_texto = self.mapa_prioridades[mais_urgente["prioridade"]]
        print(f"\n[CHAMADO MAIS URGENTE]: #{mais_urgente['id']} ({prio_texto}) - Setor: {mais_urgente['setor']} | {mais_urgente['descricao']}")

    def exibir_estatisticas_setores(self) -> None:
        print("\n--- CHAMADOS POR SETOR ---")
        for setor, qtd in self.contador_setores.items():
            print(f"• {setor:<15}: {qtd} chamado(s)")

        if self.contador_setores:
            setor_lider, total_lider = self.contador_setores.most_common(1)[0]
            print(f"\n[SETOR COM MAIS CHAMADOS]: {setor_lider} ({total_lider} chamados)")

    def exibir_todos_ordenados(self) -> None:
        print("\n--- FILA COMPLETA ORDENADA POR PRIORIDADE ---")

        copia_heap = list(self.heap_chamados)
        while copia_heap:
            prio, _, chamado = heapq.heappop(copia_heap)
            prio_texto = self.mapa_prioridades[prio]
            print(f"Prioridade {prio} ({prio_texto:<7}) | ID #{chamado['id']:02d} | Setor: {chamado['setor']:<12} | {chamado['descricao']}")

if __name__ == "__main__":
    sistema = SistemaChamadosTechMaster()

    sistema.abrir_chamado("Financeiro", "Erro ao emitir nota fiscal", 2)
    sistema.abrir_chamado("Infraestrutura", "Servidor principal fora do ar", 1)
    sistema.abrir_chamado("RH", "Solicitação de ajuste no ponto", 3)
    sistema.abrir_chamado("Financeiro", "Planilha de fluxo travando", 4)
    sistema.abrir_chamado("Infraestrutura", "Switch do 2º andar sem rede", 1)
    sistema.abrir_chamado("Financeiro", "Sistema bancário não autentica", 2)

    sistema.exibir_chamado_mais_urgente()
    sistema.exibir_estatisticas_setores()
    sistema.exibir_todos_ordenados()