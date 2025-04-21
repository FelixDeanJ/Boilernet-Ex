import os
import requests
from bs4 import BeautifulSoup

urls = [
    "https://ieeexplore.ieee.org/document/9984637"
]

output_folder = "raw_html"
os.makedirs(output_folder, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Loop setiap URL dan simpan sebagai gt_1.html, gt_2.html, ...
for idx, url in enumerate(urls, start=1):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            filename = f"gt_{idx}.html"
            output_path = os.path.join(output_folder, filename)

            with open(output_path, "w", encoding="utf-8") as file:
                file.write(soup.prettify())
            print(f"[✓] Disimpan: {output_path}")
        else:
            print(f"[✗] Gagal mengakses {url}, Status code: {response.status_code}")
    
    except Exception as e:
        print(f"[✗] Gagal scraping {url}: {e}")
