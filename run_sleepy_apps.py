import asyncio
import time

from logzero import logger

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

urls = [
    {
        "url": "https://pokepredict.streamlit.app/",
        "name": "Pokemon Battle Predictor"
    },
    {
        "url": "https://drplantclassifier.streamlit.app/",
        "name": "Plant Disease Classifier"
    },
    {
        "url": "https://amlbuddy.streamlit.app/",
        "name": "AML App"
    },
    {
        "url": "https://rolling-stonalytics.streamlit.app/",
        "name": "Rolling Stone Top 500"
    },
    {
        "url": "https://statesmigrate.streamlit.app/",
        "name": "Migration App"
    },
    {
        "url": "https://utah-house-pricing.streamlit.app/",
        "name": "Utah Housing Market"
    },
    {
        "url": "https://detroit911.streamlit.app/",
        "name": "Detroit 911 Calls"
    },
    {
        "url": "https://inference-test.streamlit.app/",
        "name": "Inference Test"
    },
    {
        "url": "https://complybuddy.streamlit.app/",
        "name": "Comply Buddy"
    },
    {"url": "https://marshallp.shinyapps.io/ShinyPokemonDB/", "name": "Shiny Pokemon"},
]


async def open_app(url, service):

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    logger.info(f"Opening {url['name']} at {url['url']}...")

    driver = webdriver.Chrome(service=Service(service), options=chrome_options)

    # Go to url
    driver.get(url["url"])
    logger.info(f"{url['name']} is sleeping at {url['url']}...")

    # Wait for 2 minutes and let function execute for other apps in the mean time
    await asyncio.sleep(120)

    # Close the browser
    driver.close()
    logger.info(f"Closed {url['name']} at {url['url']}")
    return 200


async def main(urls):
    """Open webpage on list of urls concurrently"""
    service = ChromeDriverManager().install()
    start = time.time()
    # Run everything concurrently
    await asyncio.gather(*(open_app(url, service) for url in urls))
    logger.info(f"Finished in {time.time() - start} seconds")


if __name__ == "__main__":
    asyncio.run(main(urls))
