from tinydb import TinyDB, Query
from src.config.constants import DB_FILE_PATH

db = TinyDB(DB_FILE_PATH)

def get_data(key: str) -> list:
    User = Query()
    result = db.search(User.key == key)
    if result:
        return  result[0]['value']
    else:
        return []

def insert_data(key, value):
    db.insert({'key': key, 'value': value})


def update_value(key, value):
    # Fetch current list of URLs, or create if not exists
    result = db.search(Query().key == key)
    if result:
        current_urls = result[0]['value']
        current_urls.append(value)
        db.update({'value': current_urls}, Query().key == key)
    else:
        db.insert({'key': 'urls', 'value': [value]})
