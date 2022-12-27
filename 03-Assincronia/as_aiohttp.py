import asyncio
import aiofiles
import aiohttp
import bs4

async def pegar_links():
    links =[]
    async with aiofiles.open('links.txt') as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links

async def pegar_html(link):
    print(f'Pegando html de {link}')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resposta:
            resposta.raise_for_status()

            return await resposta.text()

def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    title = title.text.split('|')[0].strip()
    return title


async def imprimir_titulos():
    links = await pegar_links()

    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))

    for tarefa in tarefas:
        html = await tarefa
        title = pegar_titulo(html)
        print(f'Curso {title}')

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(imprimir_titulos())
    el.close()

if __name__ == '__main__':
    main()