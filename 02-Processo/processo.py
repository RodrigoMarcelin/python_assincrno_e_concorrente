import multiprocessing

print(f'iniciando o proceso com nome: {multiprocessing.current_process().name}')

def faz_algo(valor):
    print(f'fazendo algo com o valor: {valor}')

def main():
    pc = multiprocessing.Process(target=faz_algo, args=('Pássaro',), name='Processo Geek')

    print(f'Iniciando o proceso com nome: {pc.name}')

    pc.start()
    pc.join()

if __name__ == '__main__':
    main()