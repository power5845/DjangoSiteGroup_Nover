# -*- coding: utf-8 -*-
from random import  randint
from django.shortcuts import render
from django.http import HttpResponse,Http404
from Tools.data_processing import get_nover_data,get_field_values
import chardet

# Create your views here.
async def index(requet):
    size = 65
    url_list = []
    alias_datas = await get_field_values("alias")
    _index = 0
    while len(url_list) < size:
        _id = randint(10000,99999)
        _alias = alias_datas[_index]
        url =f"/books/{_id}/"
        _index = _index + 1
        if url in url_list:
            continue
        url_list.append(url)
    datas = await get_nover_data(size, url_list)

    for data in datas:
        data.hero_title = data.hero_title[0]
        data.hero_name = data.hero_name[0]
        data.hero_url = data.hero_url[0] + data.hero_alias+ "/"
        data.hero_img_url_small = data.hero_img_url_small[0]
        data.hero_profession = data.hero_profession[0][0]
    return render(requet,"index.html",{"datas":datas,"title":"英雄联盟小说站"})

async def books(request,num,name):
    datas = await get_field_values("alias")

    if name in datas:
        return render(request,"book.html")
    else:
        return render(request,"404.html")