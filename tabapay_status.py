#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

status_page = requests.get("https://developers.tabapay.net/status.html")

soup = BeautifulSoup(status_page.content, "html.parser")

status_table = soup.find("table", class_="tr")
headings = status_table.find_all("th", string=lambda text: text != "Environment")
statuses = status_table.find_all("td", class_="n1")

header_list = [heading.text.strip() for heading in headings ]
status_list = [status.text.strip().replace("✔ ", "") for status in statuses]

service_status = {}

for k, v in enumerate(header_list):
    service_status[v] = status_list[k]

print(service_status)