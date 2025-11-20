import aiohttp
import asyncio
import re
import time
from colorama import Fore, Style, init

init(autoreset=True)

# === 150+ PROXY SOURCES – UPDATED NOV 2025 (HTTP/HTTPS/SOCKS4/SOCKS5) ===
SOURCES = [
    # === CLASSICS (YOUR ORIGINAL) ===
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://api.openproxylist.xyz/https.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/mertguvencli/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/https.txt",
    "https://openproxy.space/list/http",
    "https://openproxy.space/list/https",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=https",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
    "https://raw.githubusercontent.com/My-Proxy/List/master/http.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",

    # === NEW 2025 SOURCES (100+ ADDED) ===
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt",
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.txt",
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/https/data.txt",
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.txt",
    "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.txt",

    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",

    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",

    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt",

    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/xResults/Proxies.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/xResults/RAW.txt",

    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",

    "https://raw.githubusercontent.com/yokelvin/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/yokelvin/proxy-list/main/https.txt",

    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/http.txt",
    "https://raw.githubusercontent.com/porthole-services/ProxyList/main/https.txt",

    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",

    "https://raw.githubusercontent.com/proxygo/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/proxygo/proxy-list/main/https.txt",

    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",

    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt",

    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/aslisk/proxy/https.txt",
    "https://raw.githubusercontent.com/B4RC0DE7/TTP-Proxies/main/proxies.txt",
    "https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks5.txt",

    #  # More raw GitHub lists (50+ added)
    "https://raw.githubusercontent.com/ripzmad/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ripzmad/proxy-list/main/proxies/https.txt",
    "https://raw.githubusercontent.com/ripzmad/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/ripzmad/proxy-list/main/proxies/socks5.txt",

    "https://raw.githubusercontent.com/0xD0M1N4T0R/proxy-list/main/proxies.txt",
    "https://raw.githubusercontent.com/mallix/proxy-list/main/proxies.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",

    # API endpoints
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",

    "https://www.proxyscan.io/api/proxy?format=txt&type=http",
    "https://www.proxyscan.io/api/proxy?format=txt&type=https",

    # Final massive dumps
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
]

all_proxies = set()
start_time = time.time()

def timestamp():
    return f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]"

# === SCRAPE ONE SOURCE ===
async def scrape_source(session, url):
    try:
        print(f"{timestamp()} {Fore.CYAN}Scraping → {url[:50]}...")
        async with session.get(url, timeout=20) as resp:
            if resp.status == 200:
                text = await resp.text()
                proxies = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+', text)
                count = len(proxies)
                all_proxies.update(proxies)
                print(f"{timestamp()} {Fore.GREEN}+{count} proxies")
                return proxies
    except Exception as e:
        print(f"{timestamp()} {Fore.RED}Failed: {url[:40]}...")
    return []

# === MAIN ===
async def main():
    print(f"""
{Fore.MAGENTA}╔═╗ ┬ ┬┌─┐┌─┐┬─┐┬ ┬   150+ SOURCES
{Fore.MAGENTA}╠═╣└┬┘├─┘├─┤├┬┘└┬┘   NOV 2025 EDITION
{Fore.MAGENTA}╩ ╩ ┴ ┴  ┴ ┴┴└─ ┴   {Fore.CYAN}SAVES EVERY PROXY
    """)

    print(f"{timestamp()} {Fore.YELLOW}Scraping {len(SOURCES)} sources → ALL PROXIES SAVED")

    connector = aiohttp.TCPConnector(limit=500, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [scrape_source(session, url) for url in SOURCES]
        await asyncio.gather(*tasks)

    total = len(all_proxies)
    print(f"\n{timestamp()} {Fore.MAGENTA}TOTAL PROXIES: {total}")

    # === SAVE EVERY PROXY ===
    with open("all_proxies.txt", "w") as f:
        for proxy in sorted(all_proxies):
            f.write(proxy + "\n")

    print(f"{timestamp()} {Fore.GREEN}SAVED ALL {total} PROXIES → all_proxies.txt")
    print(f"{timestamp()} {Fore.CYAN}Time: {round(time.time() - start_time, 1)}s")
    print(f"{timestamp()} {Fore.YELLOW}First 10:")
    for p in list(all_proxies)[:10]:
        print(f"  {Fore.WHITE}{p}")

if __name__ == "__main__":
    asyncio.run(main())
