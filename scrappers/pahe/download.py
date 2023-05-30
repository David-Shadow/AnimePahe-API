import requests
from bs4 import BeautifulSoup
from scrappers.pahe.helper.main import get_cookies
from scrappers.pahe.helper.kwix import kwix_extractor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pahe_download(idx):
    # idx = "3ab9a35e-3cc4-6dac-6c47-042da51a20bf$0e9ac900494c3e18df6fcdd39c8fc0f978a05436745df190c0b734108d1963b3"
    download_url = kwix_extractor(idx)
    chrome_options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    print(download_url)
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get(download_url[0])

    token = ""
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    is_token = soup.find("input", attrs={"name": "_token"})
    if is_token:
        token = is_token.get("value")
    else:
        return {"results": "404 Not Found"}

    print("Getting cookies...")
    cookies = get_cookies(driver)
    driver.quit()

    headers = {
        'authority': 'kwik.cx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://kwik.cx',
        'referer': download_url[0],
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        '_token': token
    }

    response = requests.post(download_url[0].replace("/f/", "/d/"), cookies=cookies, headers=headers, data=data, allow_redirects=False)

    soup = BeautifulSoup(response.text, "html.parser")
    redirected = soup.find("a")

    if redirected:
        return {"sources":[{"url": redirected['href'], "quality":"720p"}, {"url": "Not Available", "quality":"1080p"}]}
    else:
        return {"sources": [{}]}

