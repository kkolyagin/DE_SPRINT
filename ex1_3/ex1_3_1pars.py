import requests as req
from bs4 import BeautifulSoup
import time, random as rnd
import json
import tqdm
import re

def headers():
    headers = dict()
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'
    return headers

data = {
    "data": []
}
experiences={'noExperience':'3–6 лет','moreThan6':'более 6 лет','between1And3':'1–3 года','between3And6':'3–6 лет'}
for i in experiences.keys():
    for page in tqdm.tqdm(range(0,100)):
        page_url = f"https://hh.ru/search/vacancy?experience={i}&" \
                   f"search_field=name&search_field=company_name&search_field=description&" \
                   f"text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&" \
                   f"no_magic=true&L_save_area=true&items_on_page=20&customDomain=1&" \
                   f"page={page}&hhtmFrom=vacancy_search_list"
        resp = req.get(page_url, headers=headers())
        soup = BeautifulSoup(resp.text, 'lxml')
        page_items = soup.find_all(class_="vacancy-serp-item-body")
        if len(page_items) != 0:
            for item_body in page_items:
                link = item_body.find(attrs={"data-qa": "serp-item__title"})
                item = {'title': re.sub(r'(\u202e|\u0138)', r'', link.text)}

                region = item_body.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})
                item['region'] = region and re.sub(r'(\u202e|\u0138)', r'', region.text)

                link_ref = req.get(link.attrs['href'], headers=headers())
                soup_item = BeautifulSoup(link_ref.text, 'lxml')

                salary = soup_item.find(attrs={"data-qa": "vacancy-salary"})
                item['salary'] = salary and re.sub(r'(\u202e|\u0138)', r'', salary.text)

                experience = soup_item.find(attrs={"data-qa": "vacancy-experience"})
                item['work experience'] = experience and re.sub(r'(\u202e|\u0138)', r'',experience.text)

                data['data'].append(item)
                with open("data.json", "w") as file:
                    json.dump(data, file, ensure_ascii=False)
                #time.sleep(rnd.randint(1, 3)*0.5)
        else: break