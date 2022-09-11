import asyncio

from logzero import logger

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

urls = [
    {
        "url": "https://mpkrass7-pokemon-battle-predictor-battle-simulator-publi-1q0brh.streamlitapp.com/",
        "name": "Pokemon Battle Predictor",
    },
    {
        "url": "https://mpkrass7-visual-ai-drag-and--visual-ai-drag-and-drop-app-o3kttv.streamlitapp.com/",
        "name": "Plant Disease Classifier",
    },
    {
        "url": "https://mpkrass7-aml-app-aml-app-dbokcc.streamlitapp.com/",
        "name": "AML App",
    },
    {
        "url": "https://mpkrass7-redesigned-octo-disco-streamlit-bigger-appapp-bd2mgm.streamlitapp.com/",
        "name": "Rolling Stone Top 500",
    },
    {
        "url": "https://mpkrass7-solid-octo-robot-migration-app-nabfxv.streamlitapp.com/",
        "name": "Migration App",
    },
    {
        "url": "https://liam-pasinato-utah-housing-market-1--utah-housing-0z8s0r.streamlitapp.com/",
        "name": "Utah Housing Market",
    },
    {"url": "https://thawing-peak-12115.herokuapp.com/", "name": "Shiny Pokemon DB"},
]


async def open_app(url, service):

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    logger.info(f"Opening {url['name']} at {url['url']}...")

    driver = webdriver.Chrome(service=Service(service), options=chrome_options)

    driver.get(url["url"])
    logger.info(f"{url['name']} is sleeping at {url['url']}...")
    await asyncio.sleep(30)
    driver.close()
    logger.info(f"Closed {url['name']} at {url['url']}")
    return 200


async def main(urls):
    service = ChromeDriverManager().install()
    await asyncio.gather(*(open_app(url, service) for url in urls))


if __name__ == "__main__":
    asyncio.run(main(urls))
