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
    
    processos = [Processo(id, at, pt) for id, at, pt in dados_processos]
    
    resultados_fifo = simular_fifo(processos)
    for processo in resultados_fifo:
        print(f"ID do processo: {processo.id}, Tempo de chegada: {processo.tempo_chegada}, Tempo de processamento: {processo.tempo_processamento}, Tempo final: {processo.tempo_finalizacao} ")

def imprimir_estado(tempo_atual, processo_executando, fila_prontos):
    print(f"\n--- Tempo: {tempo_atual} ---")
    
    if processo_executando:
        print(f"Processo em execução: P{processo_executando.id} (resta: {processo_executando.tempo_restante})")
    else:
        print("CPU Ociosa")

    ids_na_fila = [f"P{p.id}" for p in fila_prontos]
    print(f"Fila de prontos: {ids_na_fila if ids_na_fila else 'Vazia'}")
    print("-" * 20)
    
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

if __name__ == "__main__":
    main()     
            