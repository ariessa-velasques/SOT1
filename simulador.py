class Processo:
    def __init__(self, id, tempo_chegada, tempo_processamento):
        self.id = id
        self.tempo_chegada = tempo_chegada
        self.tempo_processamento = tempo_processamento
        self.tempo_restante = tempo_processamento  
        self.tempo_finalizacao = 0
        
def main():
    dados_processos = [
        (1, 3, 9),
        (2, 4, 15),
        (3, 7, 5),
        (4, 9, 12),
        (5, 15, 10) 
    ]
    
    #lista FIFO
    processos = [Processo(id, at, pt) for id, at, pt in dados_processos]
    #lista Round Robin
    processos_rr = [Processo(id, at, pt) for id, at, pt in dados_processos]
    
    print("=== SIMULAÇÃO FIFO ===")
    resultados_fifo = simular_fifo(processos)

    print("\nResultados FIFO:")
    print(f"{'Processo':<10} {'Chegada':<8} {'Processamento':<14} {'Finalização':<12} {'Tempo de Ciclo':<15}")
    
    tempo_ciclo_total_fifo = 0
    for processo in resultados_fifo:
        tempo_ciclo = processo.tempo_finalizacao - processo.tempo_chegada
        tempo_ciclo_total_fifo += tempo_ciclo
        print(f"P{processo.id:<9} {processo.tempo_chegada:<8} {processo.tempo_processamento:<14} "
              f"{processo.tempo_finalizacao:<12} {tempo_ciclo:<15.2f}")

    print("\n" + "="*60)

    print("\n=== SIMULAÇÃO ROUND ROBIN (Quantum=6) ===")
    resultados_rr = simular_round_robin(processos_rr)
    
    print("\nResultados Round Robin:")
    print(f"{'Processo':<10} {'Chegada':<8} {'Processamento':<14} {'Finalização':<12} {'Tempo de Ciclo':<15}")
    
    tempo_ciclo_total_rr = 0
    for processo in resultados_rr:
        tempo_ciclo = processo.tempo_finalizacao - processo.tempo_chegada
        tempo_ciclo_total_rr += tempo_ciclo
        print(f"P{processo.id:<9} {processo.tempo_chegada:<8} {processo.tempo_processamento:<14} "
              f"{processo.tempo_finalizacao:<12} {tempo_ciclo:<15.2f}")

    print("\n" + "="*60)

    print(f"{'ANÁLISE COMPARATIVA: FIFO vs ROUND ROBIN':^80}")
    print(f"{'Processo':<10} {'FIFO':<15} {'Round Robin':<15} {'Diferença':<15}")

    tempo_ciclo_medio_fifo = tempo_ciclo_total_fifo / len(resultados_fifo)
    tempo_ciclo_medio_rr = tempo_ciclo_total_rr / len(resultados_rr)

    fifo_ordenado = []
    for i in range(1, 6):
        for processo in resultados_fifo:
            if processo.id == i:
                fifo_ordenado.append(processo)

    rr_ordenado = []
    for i in range(1, 6):
        for processo in resultados_rr:
            if processo.id == i:
                rr_ordenado.append(processo)

    for i in range(len(fifo_ordenado)):
        ciclo_fifo = fifo_ordenado[i].tempo_finalizacao - fifo_ordenado[i].tempo_chegada
        ciclo_rr = rr_ordenado[i].tempo_finalizacao - rr_ordenado[i].tempo_chegada
        diferenca = ciclo_rr - ciclo_fifo
        
        print(f"P{fifo_ordenado[i].id:<9} {ciclo_fifo:<15.2f} {ciclo_rr:<15.2f} {diferenca:>+8.2f}")
    
    print("-"*55)
    print(f"{'MÉDIA':<10} {tempo_ciclo_medio_fifo:<15.2f} {tempo_ciclo_medio_rr:<15.2f} "
          f"{(tempo_ciclo_medio_rr - tempo_ciclo_medio_fifo):>+8.2f}")


def imprimir_estado(tempo_atual, processo_executando, fila_prontos):
    print(f"\n--- Tempo: {tempo_atual} ---")
    
    if processo_executando:
        print(f"Processo em execução: P{processo_executando.id} (resta: {processo_executando.tempo_restante})")
    else:
        print("CPU Ociosa")

    ids_na_fila = [f"P{p.id}" for p in fila_prontos]
    print(f"Fila de prontos: {ids_na_fila if ids_na_fila else 'Vazia'}")
    print("-" * 40)
    
def simular_fifo(processos_iniciais):
    tempo_atual = 0
    fila_prontos = []
    processos_finalizados = []
    processo_executando = None
    
    processos_a_chegar = list(processos_iniciais)

    while len(processos_finalizados) < len(processos_iniciais):
        for processo in processos_a_chegar[:]:
            if processo.tempo_chegada == tempo_atual:
                fila_prontos.append(processo)
                processos_a_chegar.remove(processo)
        
        if not processo_executando and fila_prontos:
            processo_executando = fila_prontos.pop(0)
        imprimir_estado(tempo_atual, processo_executando, fila_prontos)

        if processo_executando:
            processo_executando.tempo_restante -= 1
            if processo_executando.tempo_restante == 0:
                processo_executando.tempo_finalizacao = tempo_atual + 1
                processos_finalizados.append(processo_executando)
                processo_executando = None 

        tempo_atual += 1
        
    return processos_finalizados


def simular_round_robin(processos_iniciais, quantum=6):

    tempo_atual = 0
    fila_prontos = []
    processos_finalizados = []
    processo_executando = None
    tempo_executando = 0 

    processos_a_chegar = list(processos_iniciais)

    while len(processos_finalizados) < len(processos_iniciais):
        for processo in processos_a_chegar[:]:
            if processo.tempo_chegada == tempo_atual:
                fila_prontos.append(processo)
                processos_a_chegar.remove(processo)

        if processo_executando and tempo_executando >= quantum:
            fila_prontos.append(processo_executando)
            processo_executando = None
            tempo_executando = 0

        if not processo_executando and fila_prontos:
            processo_executando = fila_prontos.pop(0)
            tempo_executando = 0 

        imprimir_estado(tempo_atual, processo_executando, fila_prontos)

        if processo_executando:
            processo_executando.tempo_restante -= 1
            tempo_executando += 1

            if processo_executando.tempo_restante == 0:
                processo_executando.tempo_finalizacao = tempo_atual + 1
                processos_finalizados.append(processo_executando)
                processo_executando = None
                tempo_executando = 0

        tempo_atual += 1

    return processos_finalizados




if __name__ == "__main__":
    main()     
            