import asyncio, aiohttp

async def fetch_status(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                return f"{url}: {response.status}"
    except Exception as e:
        return f"{url} failed: {type(e).__name__}"

urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/404"]
results = asyncio.run(asyncio.gather(*(fetch_status(u) for u in urls)))
print("\n".join(results))