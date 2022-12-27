import datetime
import math

# import threading
import multiprocessing

def main():

    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matematico com {qtd_cores} cores")


    inicio = datetime.datetime.now()

    process = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processamento de {ini} até {fim}')
        process.append(multiprocessing.Process(target=computar, kwargs={'inicio': ini, 'fim': fim}))

    [pc.start() for pc in process]
    [pc.join() for pc in process]

    tempo = datetime.datetime.now() - inicio

    print(f'Tempo de execucao: {tempo.total_seconds():.2f} segundos')

def computar(fim, inicio =1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()

"""
Tempo de execucao: 4.02 segundos
"""