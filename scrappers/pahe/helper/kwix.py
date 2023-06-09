import requests
from bs4 import BeautifulSoup

def kwix_extractor(idx):
    idx = idx.replace("$", "/")

    r = requests.get(f"https://animepahe.ru/play/{idx}")
    soup = BeautifulSoup(r.text, 'html.parser')

    links = []
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            links.append(href)
    print(links)
#     filtered_links = [link for link in links if link.startswith("https://pahe.win")]
#     g = requests.get(filtered_links[1])
#     soup = BeautifulSoup(g.text, 'html.parser')
#     urls = soup.find_all('a', href=lambda href: href and 'https://kwik.cx/f/' in href)
#     download_url = []
#     for url in urls:
#         download_url.append(url['href'])

#     return download_url
