# ========== PYTHON ==========

import heapq

print("Fila de atendimento da clínica VidaMais\n")

fila = []

for i in range(3):
    nome = input(f"Nome do paciente {i+1}: ")
    prioridade = int(input("Prioridade (1=Emergência, 2=Urgência, 3=Comum): "))
    heapq.heappush(fila, (prioridade, nome))

print("\nChamando o próximo paciente:")
proximo = heapq.heappop(fila)
print(f"Prioridade: {proximo[0]} - Paciente: {proximo[1]}")