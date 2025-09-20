# Simulador de Escalonamento de Processos em Python

## Sobre o Projeto

Este projeto é um simulador desenvolvido em Python para estudar e visualizar o funcionamento de algoritmos de escalonamento de processos da CPU. Ele implementa os algoritmos **FIFO (First-In, First-Out)** e **Round Robin**, permitindo uma comparação direta de seu desempenho com base em um conjunto de processos pré-definido.

O objetivo é demonstrar de forma clara como cada algoritmo gerencia a fila de prontos e aloca o tempo de CPU, destacando os pontos fortes e fracos de cada abordagem.

## Funcionalidades

  * **Simulação de Algoritmos:** Implementação funcional dos escalonadores FIFO e Round Robin.
  * **Visualização Textual:** Exibição passo a passo do estado do sistema a cada segundo (tempo, processo na CPU, fila de prontos).
  * **Geração de Métricas:** Cálculo de tempos de finalização e turnaround para cada processo.
  * **Análise Comparativa:** Geração de uma tabela de resultados para facilitar a comparação entre os algoritmos.

## Como Executar

O projeto consiste em um único script Python. Para executá-lo:

1.  Certifique-se de ter o **Python 3** instalado em sua máquina.
2.  Salve o código em um arquivo, por exemplo, `simulador.py`.

## Algoritmos Implementados

### 1\. FIFO (First-In, First-Out)

É o algoritmo de escalonamento mais simples.

  * **Funcionamento:** Os processos são atendidos na ordem exata em que chegam na fila de prontos, de forma não-preemptiva. Uma vez que um processo começa a executar, ele não é interrompido até que seu tempo de execução termine.
  * **Analogia:** Uma fila de banco ou supermercado.

### 2\. Round Robin (RR)

É um algoritmo preemptivo projetado para sistemas de tempo compartilhado.

  * **Funcionamento:** Cada processo recebe uma pequena unidade de tempo de CPU chamada *quantum* (nesta simulação, `quantum = 4`). O processo executa por até um quantum. Se ele não terminar, é interrompido (preempção) e movido para o final da fila de prontos, e a CPU é alocada ao próximo processo.
  * **Vantagem:** Evita que processos longos bloqueiem processos curtos, proporcionando um tempo de resposta mais justo e rápido para sistemas interativos.


## A simulação foi executada com o seguinte conjunto de processos:

| Processo | Tempo de Chegada | Tempo de Processamento |
| :---: | :---: | :---: |
| P1 | 3 | 9 |
| P2 | 4 | 15 |
| P3 | 7 | 5 |
| P4 | 9 | 12 |
| P5 | 15 | 10 |

