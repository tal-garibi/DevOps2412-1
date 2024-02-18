from datetime import datetime

import requests

print(datetime.now())

response = requests.get("https://github.com")
urls = ["https://github.com",
        "https://google.com",
        "https://linkedin.com"]
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print("github is up")