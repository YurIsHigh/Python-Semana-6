# ========== PYTHON ==========

import heapq

tarefas = []
heapq.heappush(tarefas, (1, "Urgente"))
heapq.heappush(tarefas, (3, "Normal"))
heapq.heappush(tarefas, (2, "Importante"))

print(heapq.heappop(tarefas))

'''
========== PORTUGOL ==========
algoritmo "fila_prioridade_heap_simulada"

var
    tarefas: vetor[1..3][1..2]  // 
[prioridade][descricao]
    i, menor_pos: inteiro
    menor_prioridade: inteiro

inicio
    // Inserindo tarefas (simulando heappush)
    tarefas[1][1] <- 1
    tarefas[1][2] <- "Urgente"
    tarefas[2][1] <- 3
    tarefas[2][2] <- "Normal"
    tarefas[3][1] <- 2
    tarefas[3][2] <- "Importante"
    // continua no slide seguinte
'''