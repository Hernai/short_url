import imp


import datetime

def shortUrlEntity(item) -> dict:
    return{
        'id': str(item['id']),
        'long_url': item['long_url'],
        'code': item['code'],
        'created_at': item['created_at']
    }