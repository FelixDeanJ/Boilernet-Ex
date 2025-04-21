from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time

urls = [
    "https://ieeexplore.ieee.org/document/9984637",
    "https://ieeexplore.ieee.org/document/9984637",
    "https://ieeexplore.ieee.org/document/9984637"
]

output_folder = "raw_html"
os.makedirs(output_folder, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for idx, url in enumerate(urls, start=1):
    try:
        print(f"[•] Mengakses: {url}")
        driver.get(url)

        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        filename = f"gt_{idx}.html"
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(soup.prettify())

        print(f"[✓] Disimpan sebagai: {output_path}")

    except Exception as e:
        print(f"[✗] Gagal scraping {url}: {e}")

driver.quit()
