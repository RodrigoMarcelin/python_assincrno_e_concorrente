from typing import Generator

def fibonacci(n: int) -> Generator[int, None, None]:
    valor: int = 0
    proximo: int = 1

    while True:
        valor, proximo = proximo, valor + proximo
        yield valor

for n in fibonacci(10):
    print(n, end=', ')
    if n > 100:
        break

print('\nPronto!')