import asyncio
from time import sleep

import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)

def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print(num)
    r = httpx.get('https://httpbin.org')
    print(r)
    

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('<title>Non-blocking</title><h1>Non-blocking HTTP request</h1><p>Exercício módulo 11</p><p>Esta view será executada em paralelo com o contador</p>')


def sync_view(request):
    http_call_sync()
    return HttpResponse('<title>Blocking</title><h1>Blocking HTTP request</h1><p>Exercício módulo 11</p><p>Esta view só será executada quando terminar o contador</p>')