from src.config.constants import TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN, URL_KEY
from src.procedures.telegram_sender import send_to_telegram
from src.procedures.olx_searcher import search_olx_apartments
from src.dao.tinydb_dao import get_data, update_value
import time

counter = 0
while True:
    try:

        appartments = search_olx_apartments(city='krakow', min_price=1000, max_price=2200, num_rooms='two')
        for detail in appartments:
            time.sleep(1)
            try:
                urls_list = get_data(URL_KEY)
                if detail['url'] not in urls_list:
                    message = f"{detail['name']} with price: {detail['price']} url: {detail['url']}"
                    send_to_telegram(message,TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
                    update_value(URL_KEY, detail['url'])
                    print(get_data(URL_KEY))
                    print(urls_list)
            except:
                continue
    except Exception as e:
        print(e)
    counter +=1
    print(f"INTERATION: {counter}")
    time.sleep(60)