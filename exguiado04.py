from collections import Counter
import heapq

print("Sistema de entregas - EntregaMax\n")

entregas = []
heap = []
for i in range(5):
    nome = input(f"Cliente {i+1}: ")
    bairro = input("Bairro: ")
    prioridade = int(input("Prioridade (1=Urgente, 2=Normal): "))

entrega = {"nome": nome, "bairro": bairro, "prioridade": prioridade}
entregas.append(entrega)

heapq.heappush(heap, (prioridade, entrega))

bairros = [e["bairro"] for e in entregas]
contagem = Counter(bairros)

print("\nQuantidade de entregas por bairro:")
for bairro, qtd in contagem.items():
    print(f"{bairro}: {qtd} entrega(s)")

print("\nEntrega mais urgente:")
prioridade, entrega = heapq.heappop(heap)
print(f"Cliente: {entrega['nome']}")
print(f"Bairro: {entrega['bairro']}")
print(f"Prioridade: {entrega['prioridade']}")
