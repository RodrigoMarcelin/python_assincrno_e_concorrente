import datetime
import math

from concurrent.futures.process import ProcessPoolExecutor as Executor
import multiprocessing

def main():

    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matematico com {qtd_cores} cores")


    inicio = datetime.datetime.now()

    with Executor(max_workers=qtd_cores) as ex:
        for n in range(1, qtd_cores + 1):
            ini = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n} processamento de {ini} até {fim}')
            ex.submit(computar, inicio=ini, fim=fim)

  

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
Tempo de execucao: 3.98 segundos
"""