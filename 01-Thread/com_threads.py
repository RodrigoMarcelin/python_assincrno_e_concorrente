from time import time


import time
import colorama

from threading import Thread
from queue import Queue


def gerador_de_dados(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush=True)
        time.sleep(1)
        queue.put(i)

def comsumidor_de_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dados {valor * 2} processado.', flush=True)
        time.sleep(1)
        queue.task_done()

if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Iniciando...', flush=True)
    queue = Queue()
    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=comsumidor_de_dados, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()