import asyncio, httpx
from time import sleep
from django.http import HttpResponse

async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print(num)
        r = httpx.get("https://httpbin.org")
        print(r)

async def async_views(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

def sync_views(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, world")
