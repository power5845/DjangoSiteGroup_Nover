import asyncio
import requests
from json import loads
from . import mongdb_manager,object_factory
from urllib import request as url_request
async def get_nover_data(size,urls):
    nover_list = []
    MBM = mongdb_manager.MongoBDManager()
    datas = await MBM.get_data(size)
    for i,item in enumerate(datas):
        novel = object_factory.Novel(
            hero_id=item["instance_id"],
            hero_name=item["name"],
            hero_title=item["title"],
            hero_profession=item["roles"],
            is_week_free =item["isWeekFree"],
            hero_keywords=item["keywords"],
            hero_alias=item["alias"],
            hero_url=urls[i],
        )
        nover_list.append(novel)
    return nover_list


async def get_hero_story(alias):
    alias_name = alias.lower()
    response =  url_request.urlopen(f"https://yz.lol.qq.com/v1/zh_cn/champions/{alias_name}/index.json")
    content = response.read().decode('utf-8')
    data = loads(content)

    hero_story = object_factory.HeroStory(
        hero_title= data['title'],
        hero_name=data['name'],
        hero_image=data['image']['uri'],
        hero_quote=data[]
    )

    hero_relateds =  data['related-champions']
    for related in hero_relateds:
        print(related["title"],related["slug"])

async def get_field_values(field):
    MBM = mongdb_manager.MongoBDManager()
    datas = await MBM.get_data_by_feild_limit(field)
    return  datas