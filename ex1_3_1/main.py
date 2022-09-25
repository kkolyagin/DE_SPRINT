import requests as req
from bs4 import BeautifulSoup
import time, random as rnd
import json
import tqdm

def headers():
    headers = dict()
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'
    return headers

data = {
    "data": []
}

for page in tqdm.tqdm(range(0,10)):
    page_url = f"https://hh.ru/search/vacancy?search_field=name&" \
               f"text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&" \
               f"no_magic=true&L_save_area=true&items_on_page=100&page={page}&"
    resp = req.get(page_url, headers=headers())
    soup = BeautifulSoup(resp.text, 'lxml')
    page_items = soup.find_all(class_="vacancy-serp-item-body")
    if len(page_items) != 0:
        for item_body in page_items:
            link = item_body.find(attrs={"data-qa": "serp-item__title"})
            item = {'title': link.text}

            region = item_body.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})
            item['region'] = region and region.text

            link_ref = req.get(link.attrs['href'], headers=headers())
            soup_item = BeautifulSoup(link_ref.text, 'lxml')

            salary = soup_item.find(attrs={"data-qa": "vacancy-salary"})
            salary.text.replace('\u202e', '').strip() if salary else None
            item['salary'] = salary and salary.text

            experience = soup_item.find(attrs={"data-qa": "vacancy-experience"})
            item['work experience'] = experience and experience.text

            data['data'].append(item)
            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)
            time.sleep(rnd.randint(1, 3))