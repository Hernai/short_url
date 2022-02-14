import string
from urllib import request
import validators
from datetime import datetime
from hashlib import new
from random import choice
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from config.db import conn
from models.short_url import ShortUrl
from schemas.short_url import shortUrlEntity

short = APIRouter()

async def genetare_code(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    code = ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))

    code_found = await find_code(code)
    if code_found:
        genetare_code(8)
    else:
        return code


async def find_long_url(long_url: str):    
    url_found = conn.local.short_url.find_one({"long_url": long_url})
    return url_found


async def find_code(code: str):
    url_found = conn.local.short_url.find_one({"code": code})
    return url_found


@short.post('/short_url')
async def get_short_url(original_url: str, request: Request):
    if validators.url(original_url):    
        url_found = await find_long_url(original_url)

        if url_found:
            code = url_found['code']
        else:
            code = new_code = await genetare_code(8);
            new_url = dict(ShortUrl(long_url=original_url, code=new_code, created_at=datetime.now()))
            conn.local.short_url.insert_one(new_url).inserted_id
        
        return str(request.base_url) + code
    else:
        raise HTTPException(404, 'Is not Url')


@short.get('/{code}')
async def root(code: str):
    url_found = await find_code(code)
    if url_found:
        url = url_found['long_url']
        return RedirectResponse(url)
    else:
        raise HTTPException(404, 'Url Not Found')